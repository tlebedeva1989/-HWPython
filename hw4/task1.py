# Пользователь вводит число, Вам необходимо вывести
#  число Пи с той точностью знаков после запятой, 
#  сколько указал пользователь(БЕЗ round())

import math

n = int(input("input a number "))

result = str(math.pi)

print(result[0:n+2])