


def log_in1(F_name, S_name, Phone, Info):
    with open('phonebook1.txt', 'a', encoding="utf-8") as data:
        data.write(F_name + '\n'+ S_name + '\n' + Phone + '\n' + Info + '\n' + '__________________________________________' + '\n ' )
    with open('phonebook2.txt', 'a', encoding="utf-8") as d2:
        d2.write(f"{F_name}, {S_name}, {Phone}, {Info}; \n ")

# def log_in2(F_name, S_name, Phone, Info):
#     with open('phonebook2.txt', 'a', encoding="utf-8") as data:
#         data.write(f"{F_name}, {S_name}, {Phone}, {Info}; \n ")

def log_out1():
    with open('phonebook1.txt', 'r', encoding="utf-8") as data:
       return data.readlines()

def log_out2():
    with open('phonebook2.txt', 'r', encoding="utf-8") as data:
        return data.readlines()        