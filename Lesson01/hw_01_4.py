# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Домашнее задание к уроку 1                                                                                        #
#                                                                                                                   #
# Задание №4                                                                                                        #
# Пользователь вводит две буквы. Определить их порядковый номер в алфавите и рассчитать число букв между ними.      #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


def alphabet(char_index):
    """
    Так чисто для себя по приколу сделал, чтоб понять где там эти буквы находятся. Возвращает либо алфавит, либо False

    :param char_index: номер буквы в UTF-8
    :return: str Алфавит or bool False
    """
    if char_index >= 97:
        if char_index <= 122:
            print('english')
            return ''.join([chr(i) for i in range(97, 123)])
        elif char_index >= 1072:
            if char_index <= 1103:
                print('russian')
                return ''.join([chr(i) for i in range(1072, 1104)])
            else:
                return False
        else:
            return False


def input_chars():
    """
    Спрашивает у пользователя по очереди две буквы, приводит введённые пользователем строки к номеру буквы в кодировке
    UTF-8, проверяет на то, что пользователь каждый раз вводил по одной букве

    :return: list Список номеров букв or bool False - пользователь ввёл несколько букв, или околесицу.
    """
    inp_chars = []
    inp_chars.append(input('Введите первую букву: ').lower())
    inp_chars.append(input('Введите вторую букву: ').lower())
    res = []
    for char in inp_chars:
        try:
            res.append(ord(char))
        except TypeError:
            return False
    return res


def check_alpabets(chars_list):
    """
    Проверяет находятся-ли две буквы в одном алфавите.

    :param chars_list: list of str Список с двумя номерами символов для анализа
    :return: str 'ENG' если обе буквы английского алфавита or str 'RUS' если русского or bool False При ошибке ввода
    """
    if chars_list[0] >= 97:
        if chars_list[0] <= 122:
            if chars_list[1] >= 97:
                if chars_list[1] <= 122:
                    return 'ENG'
                else:
                    return False
            else:
                return False
        elif chars_list[0] >= 1072:
            if chars_list[0] <= 1103:
                if chars_list[1] >= 1072:
                    if chars_list[1] <= 1103:
                        return 'RUS'
                    else:
                        return False
                else:
                    return False
        else:
            return False


def count_indexes_and_distance(chars_list, alphabet):
    """
    Принимает список с буквами, название алфавита и выводит в консоль Номера букв и сколько букв между ними, либо
    сообщает пользователю об ошибке ввода.

    :param chars_list: list of str Список с двумя номерами символов
    :param alphabet: str название алфавита or bool False если пользователь ввел некорректные значения
    """
    if alphabet == False:
        print('Вы должны были ввести две буквы Русского (без "ё") ИЛИ Английского алфавита')
    if alphabet == 'ENG':
        first = chars_list[0] - 96
        print(f'Первая буква № {first}')
        second = chars_list[1] - 96
        print(f'Вторая буква № {second}')
        if first > second:
            distance = first - second - 1
        elif first < second:
            distance = second - first - 1
        else:
            distance = 0
        print(f'Между ними {distance} букв')
    elif alphabet == 'RUS':
        first = chars_list[0] - 1071
        print(f'Первая буква № {first}')
        second = chars_list[1] - 1071
        print(f'Вторая буква № {second}')
        if first > second:
            distance = first - second - 1
        elif first < second:
            distance = second - first - 1
        else:
            distance = 0
        print(f'Между ними {distance} букв')


if __name__ == '__main__':
    print('Lesson 1 task 4')
    chars_list = input_chars()
    alphabet = check_alpabets(chars_list)
    count_indexes_and_distance(chars_list, alphabet)
