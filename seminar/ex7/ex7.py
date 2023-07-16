# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
from pathlib import Path
import shutil


def sort_files():
    paths = Path(Path().cwd())
    dict_directories = {}
    set_files: set = set()
    for obj in paths.iterdir():
        print(obj)
        if obj.is_file():
            set_files.add(obj)

    for directory in paths.iterdir():
        if directory.is_dir():
            abs_path = str(directory)
            dict_directories[abs_path] = []
            for file in set_files:
                if file.suffix[1:] == directory.stem:
                    dict_directories[abs_path].append(file)

    for directory, list_file in dict_directories.items():
        for file in list_file:
            shutil.move(file, directory)


if __name__ == "__main__":
    sort_files()

