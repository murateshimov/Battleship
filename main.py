import os
import random
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ожидание 1сек при неправильном вводе
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
    ships = [3, 2, 2, 1, 1, 1, 1]  # корабли
    for ship_size in ships:
        placed = False
        while not placed:
            placed = place_ship(board, ship_size)

def check_hit(board, row, col):
    return board[row][col] == 'S'

def update_board(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'  # попадание

        if not any('S' in row for row in board):
            time.sleep(2)
            return True  # все корабли подбиты

        print("Ура! Вы попали в корабль!")
        time.sleep(1)

    else:
        board[row][col] = 'M'  # промах
        print("Промах! Корабль не подбит.")
        time.sleep(2)
    return False





def play_battleship():
    player_name = input("Введите имя на английском языке: ")
    board_size = 7
    board = [['O' for _ in range(board_size)] for _ in range(board_size)]

    place_ships(board)

    shots = 0  # сброс выстрелов для каждой новой игры

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
            time.sleep(3)
            break

    play_again = input("Хотите начать занаво? (yes/no): ").lower()

    if not play_again:
        print(f"Thanks for playing, {player_name}! Your score is {shots} shots.")
    return play_again == 'yes'

if __name__ == "__main__":
    while play_battleship():
        pass
