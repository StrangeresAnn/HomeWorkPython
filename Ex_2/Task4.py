# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
print ('Введите N: ')
n = int(input())
i = 1
res = 0
while (i <= n):
    if i % 2 == 0:
        res += i
    i += 1
print(res)
