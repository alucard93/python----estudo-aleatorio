import os
os.system('cls')
# from teste.soma import doma
# from teste import soma
# from soma import soma

# print(soma(5,5))
# print(doma(5,5))
# print(soma.doma(5,5))

comidas = ['arroz', 'feijão', 'macarrão']

# comida_m = []
# def texto(txt):
#     for comida in txt:
#         comida_m.append(comida.capitalize())
# return comida_m 


# def texto(txt: str):
#     refeicoes = [comida.capitalize() for comida in txt]
#     st = " ".join(refeicoes)
#     return f'esse foi o resultado: {st} '
# print(texto(comidas))


my_list = [1, 2, 'String', True, 3.8, ['outra', 'lista'] ]

# print(my_list)
# print(type(my_list))

my_lst_2 = list('uma lista')
# print(my_lst_2)
# print(len(my_lst_2))

# print(my_lst_2[0:5])
# my_list.clear()
# print(my_list.index(2))
# my_list.extend(my_lst_2)
print(my_list)
# for value, i in enumerate(my_list, 20):
#     print(value, i)


my_dict = {
    'primeiro': 'Marcus',
    'segundo': 'Vinicius',
    'terceiro': 'Nascimento',
    'quarto': 'Ferreira',
    'quinto': 'Nicolle',

}

my_petistas = dict(primeiro='nicolle', segundo= 'soares', terceiro = 'correa', quarto = 'de Oliveira')
# print(my_dict)
# print(my_petistas)

my_dict.update({'1ª nome': 'Marcus'})
print(my_dict)
