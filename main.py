import os
import random
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("   A B C D E F G")
    print("  ----------------")
    for i, row in enumerate(board, start=1):
        print(f"{i}| {' '.join(row)}")
    print()

def is_valid_coordinate(coord):
    return len(coord) == 2 and coord[0].isalpha() and coord[1].isdigit()

def convert_coordinate(coord):
    col = ord(coord[0].upper()) - ord('A')
    row = int(coord[1]) - 1
    return row, col

def place_ship(board, ship_size):
    direction = random.choice(['horizontal', 'vertical'])

    if direction == 'horizontal':
        row = random.randint(0, 6)
        col = random.randint(0, 7 - ship_size)
        if all(board[row][col+i] == 'O' for i in range(ship_size)):
            for i in range(ship_size):
                board[row][col + i] = 'S'
            return True

    elif direction == 'vertical':
        row = random.randint(0, 6 - ship_size)
        col = random.randint(0, 6)
        if all(board[row+i][col] == 'O' for i in range(ship_size)):
            for i in range(ship_size):
                board[row + i][col] = 'S'
            return True

    return False

def place_ships(board):
    ships = [3, 2, 2, 1, 1, 1, 1]  # размеры кораблей
    for ship_size in ships:
        placed = False
        while not placed:
            placed = place_ship(board, ship_size)

def check_hit(board, row, col):
    return board[row][col] == 'S'

def check_ship_sunk(board, row, col):
    """Проверяет, потоплен ли корабль по заданным координатам."""
    
    ship_size = 1  # Предполагаем, что корабль состоит из одной ячейки
    direction = None

    # Проверка для горизонтального корабля
    for i in range(col + 1, 7):
        if board[row][i] == 'S':
            ship_size += 1
            direction = 'горизонтальный'
        else:
            break

    for i in range(col - 1, -1, -1):
        if board[row][i] == 'S':
            ship_size += 1
            direction = 'горизонтальный'
        else:
            break

    # Проверка для вертикального корабля
    if direction is None:
        for i in range(row + 1, 7):
            if board[i][col] == 'S':
                ship_size += 1
                direction = 'вертикальный'
            else:
                break

        for i in range(row - 1, -1, -1):
            if board[i][col] == 'S':
                ship_size += 1
                direction = 'вертикальный'
            else:
                break

    # Проверка, все ли части корабля подбиты
    if direction == 'горизонтальный':
        for i in range(col, col + ship_size):
            if board[row][i] != 'X':
                return False
    elif direction == 'вертикальный':
        for i in range(row, row + ship_size):
            if board[i][col] != 'X':
                return False

    return True  # Корабль потоплен

def update_board(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = '☠️'  # Отмечаем потопленный корабль (используем эмодзи черепа для визуального отличия)

        if not any('S' in row for row in board):  # Проверка, все ли корабли потоплены
            time.sleep(2)
            print("Все корабли потоплены!")  # Обновленное сообщение о потоплении всех кораблей
            return True  # Возвращаем True, если все корабли потоплены

        print("Ура! Вы попали в корабль!")
        time.sleep(0.5)

        if check_ship_sunk(board, row, col):  # Проверка, потоплен ли конкретный корабль
            print("Корабль потоплен!")
            time.sleep(1)
    else:
        board[row][col] = 'M'  # Отмечаем промах
        print("Промах! Корабль не подбит.")
        time.sleep(1)

    return False  # Возвращаем False, если не все корабли потоплены

def play_battleship():
    player_name = input("Введите имя на английском языке: ")
    board_size = 7
    board = [['O' for _ in range(board_size)] for _ in range(board_size)]

    place_ships(board)

    shots = 0  # обнуляем количество выстрелов для каждой новой игры

    while True:
        clear_screen()
        print("    Морской бой")
        print("  ----------------")
        print_board(board)
        shot_coord = input("Введите координаты (пример: A1): ")

        if not is_valid_coordinate(shot_coord):
            print("Неверный ввод. Пожалуйста, введите правильные координаты.")
            time.sleep(2)
            continue

        row, col = convert_coordinate(shot_coord)

        if not (0 <= row < board_size and 0 <= col < board_size):
            print("Неверные координаты. Выстрел был за пределами поля боя.")
            time.sleep(2)
            continue

        if board[row][col] in ['X', 'M']:
            print("Вы уже стреляли по этой клетке.")
            time.sleep(2)
            continue

        shots += 1
        if update_board(board, row, col):
            clear_screen()
            print_board(board)
            print(f"Поздравляем, {player_name}! Вы потопили все корабли за {shots} выстрелов.")
            time.sleep(2)
            break

    play_again = input("Хотите начать заново? (yes/no): ").lower()
    return player_name, shots, play_again

def display_statistics(player_statistics):
    player_statistics.sort(key=lambda x: x[1])  # Сортируем по количеству выстрелов
    print("\nСтатистика игроков:")
    print("--------------------")
    for i, (name, shots) in enumerate(player_statistics, start=1):
        print(f"{i}. {name}: {shots} выстрелов")

def main():
    player_statistics = []

    while True:
        player_name, shots, play_again = play_battleship()
        player_statistics.append((player_name, shots))

        if play_again == 'no':
            display_statistics(player_statistics)
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
