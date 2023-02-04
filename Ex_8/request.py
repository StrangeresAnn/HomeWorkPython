from datetime import date
def add_info():
    subject = str(input('Какой предмет?\n >>> '))
    student = str(input('Какая фамилия ученика?\n >>> '))
    grade = str(input('Какая оценка?\n >>> ')) 
    current_date = date.today()
    with open(f'Ex_8/{subject}.txt', 'a') as data:
        data.write(f'{student} {grade} {current_date}\n')


def view_info():
    subject = str(input('Какой предмет?\n >>> '))
    student = str(input('Какая фамилия ученика?\n >>> '))
    data = open(f'Ex_8/{subject}.txt', 'r')
    for line in data:
        list = line
        list = list.split()
        if list[0] == student:
            print(line)
            break  
        elif data.readlines()[-1]:         
            print("Ученика с такой фамилией не найдено")

def view_student_info():
    student = str(input('Какая фамилия ученика?\n >>> '))
    subject = str(input('Какой предмет?\n >>> '))
    data = open(f'Ex_8/{subject}.txt','r')
    for line in data:
        list = line
        list = list.split()
        if list[0] == student: 
            print(line, end = '')
 