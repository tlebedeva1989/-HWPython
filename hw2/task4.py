# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input(' input a number '))

S = 0
i = 2
while i <= n:
    S +=i
    i+=2
print(f' сумма всех четных чисел от 1 до {n} равна {S}')    