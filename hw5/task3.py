# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

def RLE_coding(data):
    prev_letter = data[:1]
    result = ""
    count = 1
    data1 = data[1:]
    for char in data1:
        if char  == prev_letter:
            count +=1
            
        if prev_letter !=char :
            result += str(count) + prev_letter
            count = 1
            prev_letter = char 
       
    else:
        result += str(count) + prev_letter      
            
        return result       

# 3a4b2c3b
def uncoding (data):
    result = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else: 
            result += char * int(count) 
            count = ''   
    return result    



file = open("file1.txt", 'r')
data = file.read()

file.close()

compress = RLE_coding(data)
print(compress)

decompress = uncoding(compress)

print(decompress)
