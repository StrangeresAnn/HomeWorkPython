# Задайте последовательность чисел. Напишите программу, 
# которая выведет список элементов, которые не имели повторов в исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1


list1 = input("Введите числа через пробел: ").split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2 += [i]
list2.reverse()
print(list2)

