# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O



# Вывод игрового поля:
def print_field(field):
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3],'|', field [1 + i * 3], '|', field[2 + i * 3])
        print('-------------')
# Проверка возможности сделать шаг:
def check_cell(num, field):
    if (0 < num < 10 and field[num - 1] != 'X' and field[num - 1] != 'O'):
        return True   

    print('Клетка занята или находится вне поля игры (1-9)')
    return False
# Проверка на win:
def check_win(field):
    if    (field[0] == field[1] == field[2]
        or field[3] == field[4] == field[5] 
        or field[6] == field[7] == field[8] 
        or field[0] == field[3] == field[6] 
        or field[1] == field[4] == field[7]
        or field[2] == field[5] == field[8]
        or field[0] == field[4] == field[8]
        or field[2] == field[4] == field[6]):
        return True
    else:
        return False

count = 0
game_field = [1,2,3,4,5,6,7,8,9]
print_field(game_field)

while check_win(game_field) == False:
    cell = int(input('Ходят Крестики. Введите номер клетки: '))

    while check_cell(cell, game_field) == False:
        cell = int(input('Введите номер клетки: (1-9) '))
        
    game_field[cell - 1] = 'X'
    print_field(game_field)
    
    if check_win(game_field) == True:
        print("Выиграли крестики!")
        break
       
    count += 1

    if count == 5:
        print('Ничья! Конец игры !')
        break

    cell = int(input('Ходят Нолики. Введите номер клетки: '))

    while check_cell(cell, game_field) == False:
        cell = int(input('Введите номер клетки: (1-9) '))
 
    game_field[cell - 1] = 'O'
    print_field(game_field)
  
    if check_win(game_field) == True:
        print("Выиграли нолики!")
        break
