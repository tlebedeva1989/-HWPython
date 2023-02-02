from models import (view_info as vi, save_info1 as si1)


    
def input_info():
    First_name = input("Введите фамилию: ")
    Second_name = input("Введите имя: ")
    Phone = input("введите номер: ")
    Info = input("Введите доп.информацию: ")
    return (First_name, Second_name, Phone, Info)


def choice_active():
    choice = int(input("Введите 1, если хотите добавить информацию или 2, если хотите посмотреть справочник: "))
    if choice == 1:  
        
        si1()
        # si2()

    elif choice == 2:  vi()
    else: 
        print("Некорректный ввод ")
      
