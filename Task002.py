# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint

def num_of_candies(name):
    a = int(input(f'{name}, укажите количество конфет, которое возьмете за этот ход (от 1 до 28): '))
    while a < 1 or a > 28:
        a = int(input(f'{name}, вы ввели неверное число, повторите попытку: '))
    return a


def output_intermediate_result(name, count):
    print(f'На столе осталось {count} конфет. Ход переходит к игроку {name}.')

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
value = 2021
deal = randint(0,2)
if deal:
    print(f'Первым ходит {player1}')
else:
    print(f'Первым ходит {player2}')

while value != 0:
    if deal:
        value -= num_of_candies(player1)
        deal = False
        output_intermediate_result(player2, value)
    else:
        value -= num_of_candies(player2)
        deal = True
        output_intermediate_result(player1, value)

if deal:
    print(f'Выиграл {player2}')
else:
    print(f'Выиграл {player1}')