# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:

# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5


n = int(input("input a number "))

i = 2
f = 0
while i < n+1:
    if n % i == 0:
        print(f'наименьший натуральный делитель числа {n} - {i}')
        f =1
    else:    
        i+=1 
    if f == 1:  break   
  


