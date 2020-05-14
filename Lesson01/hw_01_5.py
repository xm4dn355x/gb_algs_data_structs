# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Домашнее задание к уроку 1                                                                                        #
#                                                                                                                   #
# Задание №5                                                                                                        #
# Пользователь вводит номер буквы в алфавите. Определить какая это буква.                                           #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


def alphabet():
    """
    Генерирует алфавит

    :return: str Русский алфавит с буквой Ё
    """
    return ''.join([chr(i) for i in range(1072, 1078)]) + chr(1105) + ''.join(chr(i) for i in range(1078, 1104))


def input_char():
    """
    Спрашивает у пользователя букву русского алфавита, проверяет на то, что это одна буква русского алфавита и
    возвращает эту букву в случае правильного ввода, либо возвращает False в случае неудачи

    :return: str буква русского алфавита or bool False - пользователь ввёл не то, что нужно.
    """
    char = input('Введите одну букву русского алфавита (включая Ё): ').lower()
    char_index = 0
    try:
        char_index = ord(char)
        if char_index >= 1072:  # Здесь в UTF-8 начинается русский алфавит
            if char_index <= 1103:  # А здесь он заканчивается
                return char
            elif char_index == 1105:    # А это буква Ё
                return char
            else:
                return False
        else:
            return False
    except TypeError:
        del (char_index)
        return False


def get_char_alphabet_index(char):
    alph = alphabet()
    if char == False:
        print('Нужно было ввести одну букву русского алфавита.')
    else:
        char_index = alph.index(char) + 1
        print(f"Порядковый номер буквы {char} является {char_index}")


if __name__ == '__main__':
    print('Lesson 1 task 5')
    """
    Чтоб не городить проверку на два алфавита будем использовать только русский, но чтоб было немного интересней,
    то в этот раз с буквой Ё
    """
    char = input_char()
    get_char_alphabet_index(char)
