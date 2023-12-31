# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
import string

MIN_VOWELS: int = 1
MIN_LENGTH: int = 4
MAX_LENGTH: int = 7
VOWELS = {'a', 'e', 'u', 'i', 'o'}


def __generate_name__():
    name: str = ''
    name_len = random.randint(MIN_LENGTH, MAX_LENGTH)
    for i in range(name_len):
        name += name.join(random.choice(string.ascii_letters))
    name = name.lower()
    name_letters_set = set(name)
    if VOWELS.isdisjoint(name_letters_set):
        change_letters = random.randint(MIN_VOWELS, MIN_LENGTH)
        list_name = list(name)
        list_vowels = list(VOWELS)
        for i in range(change_letters):
            rand_ind = random.randint(0, len(name) -1)
            rand_vowel = random.randint(0, 4)
            vowel = list_vowels[rand_vowel]
            list_name[rand_ind] = vowel
        name = ''.join(list_name)
    name = name.capitalize()
    return name


def __write_to_file__(names):
    f = open('names.txt', 'a', encoding='utf-8')
    for name in names:
        f.write(f'{name}\n')
    f.close()


def generate_files():
    list_name = list()
    for i in range(100):
        list_name.append(__generate_name__())
    __write_to_file__(list_name)


if __name__ == "__main__":
    generate_files()
