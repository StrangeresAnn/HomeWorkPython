# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 

# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

#     a, b, c, d, e, h - рандом

k = int(input(('Введите натуральную степень k: ')))
list1 = list(range(0, k))
i = 0
st = ''
import random
def rnd():
    return random.randint(0, 101)
for i in range(len(list1)):
    list1[i] = rnd()
for i in range(len(list1)+1):
    if i < (len(list1)):
        st += f'{list1[i]}x^{k} + '
        k -= 1
    elif i == (len(list1)-1):
        st += f'{list1[k]}x'
        k -= 1
    elif i == (len(list1)):
        st += f'{list1[k]}'
        
print(st)

# Я пыталась

