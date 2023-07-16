# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random
import string
import os
from pathlib import Path


def write_to_file(file_extention, directory, name_min=6, name_max=30, bite_min=256, bite_max=4096, num_files=42):
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for i in range(num_files):
        file = None
        file_name: str = str()
        bites = random.randbytes(bite_max - bite_min)
        name_length = random.randint(name_min, name_max)
        for j in range(name_length):
            file_name += file_name.join(random.choice(string.ascii_letters))
        file_name_extention = directory + '/' + file_name + '.' + file_extention
        obj = Path(file_name_extention)
        if obj.exists():
            continue
        else:
            file = open(directory + '/' + file_name + '.' + file_extention, 'a', encoding='utf-8')
            file.write(f'{bites}\n')
            file.close()


if __name__ == "__main__":
    write_to_file('txt', '/Users/ainur/PycharmProjects/7-seminar/seminar/ex6/dir', num_files=5)
