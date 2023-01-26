# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

digit = list([c for c in (input(" input a number: "))])
result = list(int(i) for i in (filter(lambda x: x.isdigit(), digit)))
print(sum(result))