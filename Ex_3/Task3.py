# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 10.01]
min = 1
max = 0
for i in list1:
    if (i - int(i)) > max:
        max = i - int(i)
    elif (i - int(i)) < min:
        min = i - int(i)

print(round(max - min, 2))