from request import add_info, show_info

def  process_func():  
    while (True):
        value = int(input("\n 1: Добавить информацию\n 2: Вывод\n 3: Выйти \n >>> "))
        if value == 1:
            add_info()
        if value == 2:
            show_info()
        if value == 3:
            break

