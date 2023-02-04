from request import add_info, view_info, view_student_info
def start():
    while (True):
        user = int(input(f'Кто запрашивает? \n 1: Учитель.\n 2: Ученик.\n 3: Выход.\n >>> '))
        list = []
        list_grade = []
        if user == 1:
            value = int(input(' 1: Добавить\n 2: Найти\n >>> '))
            if value == 1:
                add_info()
            if value == 2:
                view_info()
        if user == 2:
            view_student_info()
        if user == 3:
            break




