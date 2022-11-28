import os 
os.system('cls')

def unexisting_key():
    try:
        my_dict = {"name": "Alex", "module": "M5"}

        print(my_dict["address"])
    
    except KeyError:
        print('chave não encontrada')