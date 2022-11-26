import os
os.system('cls')

# posso criar dicionarios atraves das {} ou dict

# zip junta tudo

# lista_1 = ['primeiro', 'segundo', 'terceiro', 'quarto']
# >>> lista_2 = [1, 2, 1]
# >>> meu_dicionario = dict(zip(lista_1, lista_2))

#loop


pessoa = {"nome": "José da Silva", "idade": 36, "sexo": "masculino"}
print(pessoa.keys())
# for item, valor in pessoa.items():
#     x = item
#     y = valor
#     print('Esse é o x: {} esse é o y: {}'.format(x, y))

# for item in pessoa.keys():
#     print(item)

# for item in pessoa.values():
#     print(item)


# for item in pessoa.items():
#     print(item)

# for chave, valor in pessoa.items():
#     print(chave, valor)
# lista_1 = ["telefone", "casado", "idade"]
# lista_2 = ["999-999-999", False, 28]
# d1 = dict(nome = 'Kenzinho', cidade = 'Curitiba', modulo = 'M5')
# print(d1)
# print(type(d1))
# print(d1.get('nome'))
# print(d1.get('cidade'))
# print(d1.get('modulo'))

# print(d1.keys())
# print(d1.values())

# d2 = dict(zip(lista_1, lista_2))
# print(d2)

# print(d1.update(d2))

# del d1['casado']
# print(d1)
# print(d1.pop('idade'))
# print(d1.clear())
# print(d1)