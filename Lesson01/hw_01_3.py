# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Домашнее задание к уроку 1                                                                                        #
#                                                                                                                   #
# Задание №3                                                                                                        #
# Написать программу, которая генерирует в указанном диапазоне:                                                     #
# а. случайное целое число.                                                                                         #
# b. случайное вещественное число.                                                                                  #
# c. случайный символ.                                                                                              #
# Для каждого из трех случаев пользователь задает свои границы диапазона. Если надо получить случайный символ       #
# от "a" до "f", вводятся эти символы. Программа должна вывести на экран любой символ алфавита от "a" до "f"        #
# включительно.                                                                                                     #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from random import randint, uniform


def input_data():
    """
    Спрашивает у пользователя два значение и проводит проверку типов и возвращает список для построения диапазона, либо
    отрецательный результат проверки типов введенных пользователем данных

    :return: list Список чисел; bool False - пользователь ввёл текст или околесицу
    """
    rng = []
    rng.append(input('Введите начало диапазона: '))
    rng.append(input('Введите конец диапазона: '))
    res = []
    for r in rng:
        try:
            res.append(int(r))
        except ValueError:
            try:
                res.append(float(r))
            except ValueError:
                try:
                    res.append(chr(ord(r)))
                except TypeError:
                    return False
    if res[0] == res[1]:
        return False
    elif type(res[0]) == type(res[1]):
        return sorted(res)
    else:
        return False


def check_alpabets(letters):
    """
    Проверяет находятся-ли две буквы в одном алфавите.

    :param chars_list: list of str Список с двумя буквами
    :return: bool True если буквы состоят в одном алфавите False буквы находятся в разных алфавитах
    """
    chars_list = []
    for l in letters:
        chars_list.append(ord(l))

    if chars_list[0] >= 97:
        if chars_list[0] <= 122:
            if chars_list[1] >= 97:
                if chars_list[1] <= 122:
                    return True
                else:
                    return False
            else:
                return False
        elif chars_list[0] >= 1072:
            if chars_list[0] <= 1103:
                if chars_list[1] >= 1072:
                    if chars_list[1] <= 1103:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


def totaly_accurate_randomizer(rng):
    """
    Получает диапазон из двух чисел/дробей/символов, рандомно выбирает значение в диапазоне и выводит его в консоль.

    :param rng: list список из двух int/float/str
    :return: bool
    """
    rand = ''
    if rng == False:
        print('Милсдарь, Вы неправильный диапазон указали')
    elif isinstance(rng[0], int):
        rand = randint(rng[0], rng[1])
    elif isinstance(rng[0], float):
        rand = round(uniform(rng[0], rng[1]), 2)
    elif isinstance(rng[0], str):
        if check_alpabets(rng):
            rand = chr(randint(ord(rng[0]), ord(rng[1])))
        else:
            print('Вы должны были ввести буквы одного алфавита')
            return False
    print(f"\nНаш рандомайзер из Вашего диапазона от {rng[0]} до {rng[1]} выбрал {rand}")
    return True


if __name__ == '__main__':
    print('Lesson 1 task 3')
    print('Введите по очереди два значения. Либо две буквы, либо две цифры, либо две десятичные дроби')
    rng = input_data()
    totaly_accurate_randomizer(rng)

