# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print("Введите число: ")
k = int(input())
def get_fibonachi(k):
    f_nums = []
    a, b = 1, 1
    for i in range(k):
        f_nums.append(a)
        a, b = b, a + b

    a, b = 0, 1
    for i in range (k + 1):
        f_nums.insert(0, a)
        a, b = b, a - b
    return f_nums

print(get_fibonachi(k))