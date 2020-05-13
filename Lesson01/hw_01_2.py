# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Домашнее задание к уроку 1                                                                                        #
#                                                                                                                   #
# Задание №2                                                                                                        #
# По введенным пользователем координатам двух точек вывести уравнение прямой, которая проходит через эти точки.     #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


def input_coordinates():
    """
    Спрашивает у пользователя координаты двух точек, приводит введённые пользователем строки к числовому формату,
    проводит проверку типов и возвращает список координат и результат проверки типов введенных пользователем данных

    :return: list Список координат; bool True - введены верные данные, False - пользователь ввёл текст или околесицу
    """
    coords = []
    coords.append(input('Введите координату X для первой точки: '))
    coords.append(input('Введите координату Y для первой точки: '))
    coords.append(input('Введите координату X для второй точки: '))
    coords.append(input('Введите координату Y для второй точки: '))
    res = []
    for coord in coords:
        try:
            res.append(int(coord))
        except ValueError:
            try:
                res.append(float(coord))
            except ValueError:
                return res, False
    return res, True


def linear_equation(a_x, a_y, b_x, b_y):
    """
    Принимает координаты двух точек и вычисляет уравнение прямой, которую можно описать через эти точки.

    :param a_x: int or float, Координата X точки А
    :param a_y: int or float, Координата Y точки А
    :param b_x: int or float, Координата X точки B
    :param b_y: int or float, Координата Y точки B
    :return: str, Текст с уравнением прямой.
    """
    try:
        k = (b_y - a_y) / (b_x - a_x)
        b = a_y - k * a_x
        # В случае, если результатом решения является целое число для k и/или b, то приводим к целому (для красоты)
        if k % 1 == 0:
            k = int(k)
        if b % 1 == 0:
            b = int(b)
        if b > 0:
            return f'Уравнение прямой:\n\ty = {round(k, 2)}x+{round(b, 2)}'
        elif b == 0:
            return f'Уравнение прямой:\n\ty = {round(k, 2)}x'
        else:
            return f'Уравнение прямой:\n\ty = {round(k, 2)}x{round(b, 2)}'
    except ZeroDivisionError:
        return 'У обоих точек одинаковые координаты'


def print_result(coords, type_check_flag):
    """
    Получает список координат и результат проверки типов. Если пользователь ввёл валидные данные, то запускает
    вычисление уравнения прямой и выводит результат в консоль, а если нет, то сообщает, что пользователь ошибся
    на этапе ввода данных.

    :param coords: list Список координат
    :param type_check_flag: bool Соответствуют-ли типы введенных пользователем данных числовым.
    """
    if type_check_flag == True:
        print(f'\nТочка А: ({coords[0]}:{coords[1]}), Точка Б: ({coords[2]}:{coords[3]})')
        print(linear_equation(coords[0], coords[1], coords[2], coords[3]))
    else:
        print('\nВы должны были ввести целое число, либо десятичную дробь.\nВ качестве разделителя десятичной дроби '
              'используется точка, например 5.0')


if __name__ == '__main__':
    print('Lesson 1 task 2\n')
    coords, type_check_flag = input_coordinates()
    print_result(coords, type_check_flag)

