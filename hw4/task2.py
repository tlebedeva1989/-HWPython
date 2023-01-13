# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 


def is_prime(x):
    for i in range(2, int((x//2)+1)):
        if x % i == 0:
            return False
    return True

n = int(input( "input a number "))
result = ""


for num in range(2, n+1):
    
    if is_prime(num) == True:       
        if n % num == 0:
                            
            result += f" {num} *"
            n /= num
            num = 2
        else:
            num +=1        
    else: num +=1        
    if is_prime(n) == True: break

result += f" {n}"

print(result[:-2])
