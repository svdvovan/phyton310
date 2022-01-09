import random
import os
# rnd = random.randrange(0, 100, 1)
# userNumber = 0
# count = 0
# while userNumber != rnd:
#     # print(rnd)
#     userNumber = int(input("введите число"))
#     count += 1
#     if userNumber > rnd:
#         print("введенное число больше загаданного")
#     elif userNumber < rnd:
#         print("введенное число меньше загаданного")
# print(f'количество попыток {count}')
from os.path import getsize, join

"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли в списке число, которое является индексом элемента "odd". Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""


def odd_ball(arr):
    num = arr.index("odd")
    for i in arr:
        if i == num:
            return True
    else:
        return False


# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
# print(odd_ball(["even", 10, "odd", 2, "even"]))  # True

"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
 Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""


def find_sum(n):
    sd = [i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0]
    print(sum(sd))


# find_sum(5)  # return 8 (3 + 5)
# find_sum(10)  # return 33 (3 + 5 + 6 + 9 + 10)

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]  # ["Ryan", "Mark", "John", "Paul"]


def get_names(names):
    # for i in names:
    #     if len(i) == 4:
    #         print(i+"ok")
    sd = [i for i in names if len(i) == 4]
    print(sd)


# get_names(names)
# print(os.environ, end='\n')
# os.startfile(r'F:/logo fitlife.png')

# tree = os.walk('f:/git')
for root1, dirs, files in os.walk('F:\calibre'):
    # print(root)
    # # for _dir in dirs:
    # #     print(_dir)
    # #
    # for _file in files:
    #     print('    '+_file)
    print(root1, "consumes", end=" ")
    print(sum(getsize(join(root1, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")


