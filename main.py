import os
import random

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
    row = random.randint(0, 6 if direction == 'vertical' else 9)
    col = random.randint(0, 9 if direction == 'horizontal' else 6)

    if direction == 'horizontal' and col + ship_size <= 7 and all(board[row][col + i] == 'O' for i in range(ship_size)):
        for i in range(ship_size):
            board[row][col + i] = 'S'
        return True
    elif direction == 'vertical' and row + ship_size <= 7 and all(board[row + i][col] == 'O' for i in range(ship_size)):
        for i in range(ship_size):
            board[row + i][col] = 'S'
        return True
    return False

def place_ships(board):
    ships = [3, 2, 2, 1, 1, 1, 1]  # Sizes of ships
    for ship_size in ships:
        placed = False
        while not placed:
            placed = place_ship(board, ship_size)

def check_hit(board, row, col):
    return board[row][col] == 'S'

def update_board(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'  # Hit
        if not any('S' in row for row in board):
            return True  # All ships sunk
    else:
        board[row][col] = 'M'  # Miss
    return False

def play_battleship():
    player_name = input("Enter your name: ")
    board_size = 7
    board = [['O' for _ in range(board_size)] for _ in range(board_size)]

    place_ships(board)

    shots = 0  # Reset shots for each new game

    while True:
        clear_screen()
        print("Battleship Game")
        print("----------------")
        print_board(board)
        shot_coord = input("Enter your shot coordinates (e.g., A1): ")

        if not is_valid_coordinate(shot_coord):
            print("Invalid input. Please enter a valid coordinate.")
            continue

        row, col = convert_coordinate(shot_coord)

        if not (0 <= row < board_size and 0 <= col < board_size):
            print("Invalid coordinates. Shot outside the battlefield.")
            continue

        if board[row][col] in ['X', 'M']:
            print("You've already shot at this cell. Try again.")
            continue

        shots += 1
        if update_board(board, row, col):
            clear_screen()
            print_board(board)
            print(f"Congratulations, {player_name}! You sank all the ships in {shots} shots.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if not play_again:
        print(f"Thanks for playing, {player_name}! Your score is {shots} shots.")
    return play_again == 'yes'

if __name__ == "__main__":
    while play_battleship():
        pass
