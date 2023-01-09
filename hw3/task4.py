# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("input a number "))
result = n
ostatok = n
str = ""
while result > 1:
    if result % 2 == 0:
        result //= 2
        str = str + "0"
    else:
        result //=2
        str = str + "1"   
str = str + "1"       

str = str[::-1]
print(str)    
        
