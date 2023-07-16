# Задание
# ✔ Решить задачи, которые не успели решить на семинаре.
# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
#   исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import random
from pathlib import Path
import os


def rename_files(number_of_numbers: int, file_extensions: list, range_of_original_name: list, name=''):
    paths = Path(Path().cwd())
    count: int = 0
    for file in paths.iterdir():
        extension = file.suffix[1:]
        if file.is_file() and (extension in file_extensions):
            truncate_name = random.randint(range_of_original_name[0], range_of_original_name[1])
            new_name = file.stem[:truncate_name]
            new_name += name
            count, num = __count__(count, number_of_numbers)
            new_name += num
            new_name += '.' + extension
            file.rename(new_name)


def __count__(count: int, number_of_numbers: int):
    number = count
    number += 1
    number_str = str(number)
    buff = ''.join('0' for _ in range(len(number_str), number_of_numbers))
    return count, buff + number_str


if __name__ == "__main__":
    rename_files(3, ['txt'], [2, 4], 'Ren')
