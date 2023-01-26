# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

lst = [12,'sadf', 5643]

string_list = list(filter(lambda x: type(x) == str, lst))
digit_list = list(filter(lambda x: type(x) == int, lst))
print(string_list)
print(digit_list)