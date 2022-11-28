import os 
os.system('cls')

def div_by_zero():
    try:
        a = 1
        b = 0
        print(a / b)

    except ZeroDivisionError:
        print('não é possivel dividir por zero')

div_by_zero()

def unexisting_key():
    try:
        my_dict = {"name": "Alex", "module": "M5"}

        print(my_dict["address"])
    
    except KeyError:
        print('chave não encontrada')

unexisting_key()

def unexisting_index():
    try:
        my_list = [0, 1]
        print(my_list[5])

    except IndexError:
        print('indice não encontrado')

unexisting_index()


def misterious_error():
    try:
        a = 5
        print(a.capitalize())
    except AttributeError:
        print('AttributeError tratado')