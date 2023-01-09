# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input("input a number "))

list = []
for i in range(1,n+1):
    x = random.randint(1,15)
    list.append(x)

print (list)

list1 = []
for i in range(len(list)//2 + len(list) % 2):
    P = 1
    P = list[i] * list[-i-1]
    list1.append(P)


print(list1)