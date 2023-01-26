# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

lst = [int(i) for i in input("Введите список целых чисел через пробел: ").split()]
print(lst)
lst = list(filter(lambda x: x > 9 and x < 100, lst))
print(lst)