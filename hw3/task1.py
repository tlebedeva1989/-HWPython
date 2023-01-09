# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input("input a number "))

list = []
for i in range(1,n+1):
    x = random.randint(1,15)
    list.append(x)

print (list)

def SumOfEl(lst:list):
    S = 0


    for i in range(1, len(lst), 2):
        S += lst[i]
       
    
    return S   

print(SumOfEl(list))        
