# f = open('text_data.txt')
# print(f)
# print(list(f))
############################################################################
# f = open('text_data.txt', 'r', encoding='utf-8')
# print(f)
# print(list(f))
############################################################################
# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write('Окончание файла\n')
# f.close()
############################################################################
# f = open('bin_data', 'wb', buffering=64)
# f.write(b'X' * 1200)
# f.close()
############################################################################
# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()
# f = open('data.txt', 'r', encoding='utf-8')
# # print(list(f))  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# f.close()
# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()
############################################################################
# with open('text_data.txt', 'r+', encoding='utf-8') as f:
#     print(list(f))
# # print(f.write('Пока'))  # ValueError: I/O operation on closedfile.
############################################################################
# with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
#         open('bin_data', 'rb') as f2, \
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))
############################################################################
# with (
#         open('text_data.txt', 'r+', encoding='utf-8') as f1,
#         open('bin_data', 'rb') as f2,
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))
############################################################################
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     print(list(f))
############################################################################
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     res = f.read()
#     print(f'Читаем первый раз\n{res}')
#     res = f.read()
#     print(f'Читаем второй раз\n{res}')
############################################################################
# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.read(SIZE):
#         print(res)
############################################################################
# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline(SIZE):
#         print(res)
############################################################################
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')
############################################################################
# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         print(line.replace('\n', ''))
############################################################################
# text = 'Lorem ipsum dolor sit amet, consectetur adipisicingelit.'
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
#     print(f'{res = }\n{len(text) = }')
############################################################################
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(line)
#         print(f'{res = }\n{len(line) = }')
############################################################################
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res = }\n{len(line) = }')
############################################################################
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     f.writelines('\n'.join(text))
############################################################################
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, file=f)
############################################################################
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, end='\n***\nKyle\n', file=f)
############################################################################
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'w', encoding='utf-8') as f:
#     print(f.tell())
#     for line in text:
#         f.write(f'{line}\n')
#         print(f.tell())
#     print(f.tell())
# print(f.tell())     # ValueError: I/O operation on closed file.
############################################################################
# last = before = 0
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f'{last = }, {before = }')
#     print(f'{f.seek(before, 0) = }')
#     f.write('\n'.join(text))
############################################################################
# last = before = 0
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f.seek(before, 0))
#     print(f.truncate())
############################################################################
# size = 50
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     print(f.truncate(size))
############################################################################
import os
from pathlib import Path
print(os.getcwd())
print(Path.cwd())
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
