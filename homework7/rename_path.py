"""
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

import os

__all__ = ['rename_file']


def rename_file(new_name: str, count_number: int, extension: str, new_extension: str, save_name: list[int]):
    count = 1
    for file in os.listdir('./'):
        if file.endswith(extension):
            start, end = save_name
            filename = file.split('.')[0][start:end] + new_name + str(count).zfill(count_number)
            count += 1
            os.rename(file, f'{filename}.{new_extension}')


if __name__ == '__main__':
    rename_file('hello', 2, 'txt', 'md', [3, 6])
    rename_file('bye', 7, 'jpg', 'cvs', [0, 3])
    rename_file('world', 0, 'doc', 'txt', [1, 4])
