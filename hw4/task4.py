# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 

import random

k = int(input(" input k "))

list = []
for i in range(1,k+1):
    x = round(random.randint(1,100))
    list.append(x)

print(list)

result_str = ""
while k > 0:
    for i in range(len(list)):
     
        result_str += f" {list[i]} * x^{k} + "
        k-=1    

   
print(f"{result_str[:-17]} + {random.randint(1,100)} ")       


