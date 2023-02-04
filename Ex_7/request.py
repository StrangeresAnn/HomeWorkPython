import os

def add_info():
    name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    info =  input("Введите дополнительную информацию: ")

    with open('Ex_7/book1.txt', 'a') as data:
        data.write(f'{name}\n{second_name}\n{number}\n{info}\n')
        data.write(f'-------\n')
    with open('Ex_7/book2.txt', 'a') as data:
        data.write(f'{name}, {second_name}, {number}, {info}\n')

def show_info():
    data = open('Ex_7/book2.txt', 'r')
    isempty = os.stat('Ex_7/book2.txt').st_size == 0
    if isempty:
        print('Пусто!')
    else:
        for line in data:
            print(line, end = '')
    data.close()
