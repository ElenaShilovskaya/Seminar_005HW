# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def num_of_candies(name):
    a = int(input(f'{name}, и сколько конфет ты возьмешь сейчас? Помни, их можно взять от 1 до 28: '))
    while a < 1 or a > 28:
        a = int(input(f'{name}, вы ввели неверное число, повторите попытку: '))
    return a


def output_intermediate_result(name, num,  count, name2):
    print(f'{name} взял {num} конфет. На столе осталось {count} конфет. \nХод переходит к игроку {name2}.')

player1 = input('Введите Ваше имя: ')
player2 = 'Хомяк'
value = 100
print(f'Ну а я {player2}. И я хочу сыграть с тобой в игру... На столе лежит {value} конфет. Попробуй обнулить количество своим последним ходом...')
optimal_num = 29
deal = randint(0,2)
if deal:
    print(f'Первым ходит {player1}')
else:
    print(f'Первым ходит {player2}')

while value > 28:
    if deal:
        num = num_of_candies(player1)
        value -= num
        deal = False
        output_intermediate_result(player1, num, value, player2)
    else:
        num = value%optimal_num
        value -= num
        deal = True
        output_intermediate_result(player2, num, value, player1)
while value != 0:
    if deal:
        num = num_of_candies(player1)
        while num > value:
            num = int(input(f'На столе нет {num} конфет, повторите попытку: '))
        value -= num
        deal = False
        output_intermediate_result(player1, num, value, player2)
    else:
        num = value
        value -= num
        deal = True
        output_intermediate_result(player2, num, value, player1)


if deal:
    print(f'Выиграл {player2}')
else:
    print(f'Выиграл {player1}')