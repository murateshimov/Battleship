import os
import random

# Функция для создания пустого игрового поля
def create_board():
    board = []
    for _ in range(7):
        board.append([' '] * 7)
    return board