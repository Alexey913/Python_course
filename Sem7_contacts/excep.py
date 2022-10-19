import os
# import interface

def check_menu(quan):
    while True:
        try:
            ent_menu = (input())
            while int(ent_menu) not in range (1, quan):
                print ('\nНеверный ввод! Повторите ввод:')
                # log.universal_logger("Неверный пункт меню", data_description = "Ошибка ввода") 
                ent_menu = (input())
            return int(ent_menu)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            # log.universal_logger("Неверный формат ввода меню", data_description = "Ошибка ввода")

def check_name_file(ent_name):
    list_name = list(ent_name)
    error_pop = ['/','|','*','?','>','<',':','"','\\']
    for i in list_name:
        if i in error_pop or len(ent_name)<3:
            print ("Недопустимое название")
            return False
    return True

def check_phone (phone_data):
    if phone_data.isdigit():
        return phone_data
    else:
        print ('Неверный ввод! Повторите')
        return False