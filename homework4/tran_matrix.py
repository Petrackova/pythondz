"""
Напишите функцию для транспонирования матрицы
"""
import random
import numpy as np


def matrix1(s: int, q: int) -> list:
    matrix = [[0] * q for _ in range(s)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(0, 100)

    print('Исходная матрица')
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()
    print()
    return matrix


def print_trans(arr: list):
    print('Транспонированная матрица')
    for c in range(m):
        for r in range(n):
            print(arr[r][c], end=' ')
        print()


n, m = int(input()), int(input())
new_matrix = matrix1(n, m)
print_trans(new_matrix)

# Вариант 2
print()
matrix2 = matrix1(n, m)
new_matrix2 = np.transpose(matrix2)
print('Транспонированная матрица')
print(new_matrix2)