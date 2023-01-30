# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

import os.path

def coding(text):
    count = 0
    el = text[0]
    res = ''
    for element in text:

        if element == el:
            count += 1
        else:
            res += str(count) + el
            count = 1
            el = element
    else:
        res += str(count) + el
    return res

def decoding(text):
    num = ''
    res = ''
    for element in text:
        if element.isdigit():
            num += element
        else:
            for i in range(int(num)):
                res += element
            else:
                num = ''
    return res

with open(os.path.join( 'coding.txt'), 'r') as f:
    file1 = f.read()

res_coding = coding(file1)
print(res_coding)
print(decoding(res_coding))




    

