# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

BEGIN = -1000
END = 1000


def write_to_file(num_lines: int, file_name):
    f = open(file_name, 'a', encoding='utf-8')
    for i in range(num_lines):
        random_int = random.randint(BEGIN, END)
        random_float = random.uniform(BEGIN, END)
        f.write(f'{random_int}|{random_float}\n')
    f.close()


write_to_file(100, 'numbers.txt')
