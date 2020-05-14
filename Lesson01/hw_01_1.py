# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Домашнее задание к уроку 1                                                                                        #
#                                                                                                                   #
# Задание №1                                                                                                        #
# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5 побитовый      #
# сдвиг вправо и влево на 2 знака.                                                                                  #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


if __name__ == '__main__':
    print('Lesson 1 task 1')
    # Два числа
    a = 5
    b = 6
    # Их двоичной представление
    print(f'Двоичное представление 5 = {bin(a)}')
    print(f'Двоичное представление 6 = {bin(b)}')
    # Логические операции
    bit_or = a | b
    bit_and = a & b
    bit_xor = a ^ b
    bit_not_a = ~ a
    bit_not_b = ~ b
    bit_shift_left = a << 2
    bit_shift_right = a >> 2
    # Вывод в консоль этой красоты
    print()
    print(f"Результат побитового OR:\t {bin(bit_or)}\t {bit_or}")
    print(f"Результат побитового AND:\t {bin(bit_and)}\t {bit_and}")
    print(f"Результат побитового XOR:\t {bin(bit_xor)}\t {bit_xor}")
    print(f"Результат побитового NOT для 5:\t {bin(bit_not_a)}\t {bit_not_a}")
    print(f"Результат побитового NOT для 6:\t {bin(bit_not_b)}\t {bit_not_b}")
    print(f"Результат сдвига 5 влево на 2 знака:\t {bin(bit_shift_left)}\t {bit_shift_left}")
    print(f"Результат сдвига 5 вправо на 2 знака:\t {bin(bit_shift_right)}\t {bit_shift_right}")