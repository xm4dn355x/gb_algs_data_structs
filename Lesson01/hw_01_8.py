# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Домашнее задание к уроку 1                                                                                        #
#                                                                                                                   #
# Задание №8                                                                                                        #
# Вводятся три разных числа. Найти, какой из них является средним (больше одного, но меньше другого).               #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import statistics


def input_numbers():
    """
    Спрашивает у пользователя три числа и приводит введённые пользователем строки к числовому формату,
    проводит проверку типов и возвращает список координат и результат проверки типов введенных пользователем данных

    :return: list Список чисел; bool True - введены верные данные, False - пользователь ввёл текст или околесицу
    """
    numbers = []
    numbers.append(input('Введите первое число: '))
    numbers.append(input('Введите второе число: '))
    numbers.append(input('Введите третье число: '))
    res = []
    for nbr in numbers:
        try:
            res.append(int(nbr))
        except ValueError:
            try:
                res.append(float(nbr))
            except ValueError:
                return res, False
    return res, True


def middle_number(numbers: list, type_check_flag: bool):
    """
    Получает список чисел, флаг правильности введенных значений и возвращает медианное значение из списка чисел.

    :param numbers: list of numbers
    :param type_check_flag: bool
    """
    if type_check_flag == True:
        print(f'Медианное значение равно: {statistics.median(numbers)}')
    else:
        print('\nВы должны были ввести целое число, либо десятичную дробь.\nВ качестве разделителя десятичной дроби '
              'используется точка, например 5.0')


if __name__ == '__main__':
    print('Lesson 1 task 8')
    numbers, type_check_flag = input_numbers()
    middle_number(numbers, type_check_flag)