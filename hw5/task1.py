# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)\

import random

candy = 120
bot_move = 0
player_move = 0
count_bot = 0
count_player = 0
max_candy_move = 28

while (candy != 0):
    
    player_move = int(input(f"Введите количество конфет, которое хотите взять, но не более  {max_candy_move} :") )
    
    if  1 <= player_move <= max_candy_move : 
        count_player = 1
        count_bot = 0
        candy -= player_move

        if candy < 28: max_candy_move = candy    
        print(f"на столе осталось {candy} конфет ")

        if candy == 0: print('you WIN!');   break
        bot_move = random.randint(1,max_candy_move)
        candy -= bot_move
        count_bot = 1
        count_player = 0

        if candy < 28: max_candy_move = candy
        print(f"Бот взял {bot_move} конфет, на столе осталось {candy} конфет ")
        
        if candy == 0 : print('bot WIN!')
        
    elif   1 > player_move > 28: print(f" Возьмите {max_candy_move} ")

      

    
        


