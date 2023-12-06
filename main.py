import os
import random

# Функция для создания пустого игрового поля
def create_board():
    board = []
    for _ in range(7):
        board.append([' '] * 7)
    return board

# Функция для вывода игрового поля на экран
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   A B C D E F G")
    for i, row in enumerate(board):
        print(i + 1, end="  ")
        for cell in row:
            print(cell, end=" ")
        print()