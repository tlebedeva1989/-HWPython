# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 

import random

k = int(input(" input k "))

list = []
for i in range(1,k+2):
    x = round(random.randint(1,100))
    list.append(x)

print(list)

result_str = ""

for i in range(0,len(list)+1):
    
    while k > 0:
        result_str = f" {list[i]} * x^{k} + "
        k -=1    

print(result_str)       


