# Задайте последовательность чисел. Напишите программу,
#  которая выведет список элементов, которые не имели повторов в исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1


import random
n = int(input("input a number "))

list = []
for i in range(1,n+1):
    x = random.randint(1,15)
    list.append(x)

print (list)

result_list = []

for i in list:
    if list.count(i) > 1:
        continue
    else: 
        result_list.append(i)

print(result_list)

