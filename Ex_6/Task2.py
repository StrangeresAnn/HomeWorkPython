# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

li = [12,'sadf',5643]
# print(list(filter(lambda x: isinstance(x, str) == True, li)),list(filter(lambda x: isinstance(x, str) == False, li)))

nums = list(filter(lambda x: isinstance(x, str) == True, li))
chars = list(filter(lambda x: isinstance(x, str) == False, li))
print(nums,chars)


