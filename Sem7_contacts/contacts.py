#  4 - Добавить контакт\n 5 - Удалить контакт\n 6 - Поиск контактов\n
import excep

def create_contact(*num_book):
    surname_c = input ('Введите фамилию:\n')

    name_c = input ('Введите имя:\n')
    prot_c = input ('Введите отчество:\n')
    num_ph = input ('Введите номер телефонв:\n')
    while excep.check_phone(num_ph) is False:
        num_ph = input ('Введите номер телефонв:\n')
    with open(num_book, 'a', encoding='utf-8') as list_b:
        list_b.write(f'{surname_c}, {name_c}, {prot_c} - {num_ph}\n')
    list_b.close()
