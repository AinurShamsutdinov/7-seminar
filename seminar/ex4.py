# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


import random
import string


def write_to_file(file_extention, name_min=6, name_max=30, bite_min=256, bite_max=4096, num_files=2):
    for i in range(num_files):
        file_name: str = str()
        bites = random.randbytes(name_max - name_min)
        for j in range(name_min, random.randint(name_min, name_max)):
            file_name = file_name.join(random.choice(string.ascii_letters))
        file_name_extention = file_name + '.' + file_extention

        file = open(file_name_extention, 'a', encoding='utf-8')
        file.write(f'{bites}\n')
        file.close()


write_to_file('txt')
