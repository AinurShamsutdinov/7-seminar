#Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def write_to_file(name_num):
    f = open('result.txt', 'a', encoding='utf-8')
    for item in name_num:
        f.write(f'{item}\n')
    f.close()


def multiply():
    list_name_mult: list = list()
    list_nums: list = list()
    list_names: list = list()
    max_length: int = int()
    with open('names.txt', 'r+', encoding='utf-8') as f1, open('numbers.txt', 'rb') as f2:
        list_names = list(f1)
        list_nums = list(f2)
    if len(list_nums) > len(list_names):
        max_length = len(list_nums)
    else:
        max_length = len(list_names)
    for i in range(max_length):
        mult = None
        name = None
        if i < len(list_nums) - 1:
            line: str = str(list_nums[i])
            num_1 = None
            num_2 = None
            nums = line.split('|')
            num_1 = int(nums[0][2:])
            last_simbols = len(nums[1]) - 3
            num_2 = float(nums[1][:last_simbols])
            mult = num_1 * num_2
        if i < len(list_names):
            name = list_names[i]
            name = name[:len(name) - 1]
        list_name_mult.append(f'{name}\t{mult}')
    return list_name_mult


names_numbers = multiply()
write_to_file(names_numbers)
