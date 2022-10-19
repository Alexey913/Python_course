import os
# import interface
import excep
import linecache

def create_book():
    name = input('Введите имя нового справочника:\n')
    res_check_name = excep.check_name_file(name)
    while res_check_name is False:
        name = input('Повторите ввод:\n')
        res_check_name = excep.check_name_file(name)
    else:
        if excep.os.path.isfile(name) is True:
            print("Справочник уже существует! Повторить ввод?")
        else:
            with open(name, 'a', encoding='utf-8') as new_book:
                new_book.write(f'Телефонный справочник "{name}"\n\n')
                print (f'Телефонный справочник "{name}" успешно создан!')
            new_book.close()
            with open('list_book.csv', 'a', encoding='utf-8') as list_b:
                list_b.write(f'{name}\n')
            list_b.close()

def del_book():
    name = input('Какой справочник желаете удалить? Введите название:\n')
    res_check_name = excep.check_name_file(name)
    while res_check_name is False:
        name = input('Повторите ввод:\n')
        res_check_name = excep.check_name_file(name)
    else:
        if excep.os.path.isfile(name) is True:
            os.remove(name)
            print(f"Файл {name} успешно удален!")
            with open ('list_book.csv', 'r', encoding='utf-8') as list_b:
                lines = list_b.readlines()
            list_b.close()
            with open ('list_book.csv', 'w', encoding='utf-8') as list_b:
                for line in lines:
                    if line!=name+"\n":
                        list_b.write(line)
            list_b.close
        else:
            print("Такого справочника не существует!")

def print_book_list():
    with open('list_book.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(f'Cправочник {line}', end='')
    file.close()

def open_book():
    print ('Какой справочник желаете открыть?')
    with open('list_book.csv', 'r', encoding='utf-8') as file:
        temp_dict = {}
        temp_dict.clear()
        count = 1
        for line in file:
            print(f'{count} - Cправочник {line}', end='')
            temp_dict[count] = line.split()
            count += 1
    file.close()
    num_book = excep.check_menu(count)
    with open(*temp_dict[num_book],'r', encoding='utf-8') as open_file:
        for line in open_file:
            print(line, end ='')
    open_file.close()
    return temp_dict[num_book]