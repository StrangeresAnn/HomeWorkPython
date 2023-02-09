id_user = None 
input_data = None
result = None

def get_id_user(num_id):
    global id_user
    id_user = num_id

def get_input_data(data):
    global input_data
    input_data = data

def get_result(res):
    global result
    result = res 

def save_log():
    with open('Ex_10/Log.txt', 'a', encoding = 'utf-8') as f:
        f.writelines(f'ID user: {id_user}\nInput: {input_data}\nResult: {result}\n----------------\n')