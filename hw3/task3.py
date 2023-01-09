# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input("input a number "))

list = []
for i in range(1,n+1):
    x = round(random.uniform(1,15),2)
    list.append(x)

print (list)

for i in range(len(list)):
    list[i] = round((list[i] % 1), 2)

print(list)    

max = list[0]
min = list[0]

for i in range(len(list)):
    if list[i] > max:
        max = list[i]
    elif list[i] < min:
        min = list[i]

print (f" разница между максимальной и минимальной дробными частями элементов списка равна {max-min} ")       
 


