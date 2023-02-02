import logger
import user_interface

def save_info1():
    
    logger.log_in1(*user_interface.input_info())

# def save_info2():
#     logger.log_in2(*user_interface.input_info())    
    

def view_info():
    format = int(input(" В каком формате вы хотите вывести справочник? Введите 1 (в столбик) или 2 ( в строку ): "))
    if format == 1: print(*logger.log_out1())
    elif format == 2: print(*logger.log_out2())
    else: 
        print(" Некорректный ввод")
        view_info()