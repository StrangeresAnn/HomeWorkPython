
def process_step(list1):
    if ('/' in list1) or ('*' in list1):
        for i in range(len(list1)):
            if list1[i] == '/':
                temp = list1[i - 1] / list1[i + 1]
                del list1[i-1 : i+2]
                list1.insert(i - 1, temp)
                break

            elif list1[i] == '*':
                temp = list1[i - 1] * list1[i + 1]
                del list1[i-1 : i+2]
                list1.insert(i - 1, temp)
                break
    else:
        for i in range(len(list1)):
            if list1[i] == '+':
                temp = list1[i - 1] + list1[i + 1]
                del list1[i-1 : i+2]
                list1.insert(i - 1, temp)
                break

            elif list1[i] == '-':
                temp = list1[i - 1] - list1[i + 1]
                del list1[i-1 : i+2]
                list1.insert(i - 1, temp)
                break

    return list1

def process_func(values):
    res_str = ''

    for i in values:
        if i.isdigit():
            res_str += i
        else:
            res_str += f' {i} '
    
    res_str = res_str.split()

    for i in range(len(res_str)):
        if res_str[i].isdigit():
            res_str[i] = int(res_str[i])

    count = 0
    for i in res_str:
        if type(i) == str:
            count += 1
    
    for _ in range(count):
        res_str = process_step(res_str)

    return res_str[0]
