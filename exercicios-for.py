import os
os.system('cls')
# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]

# vendedores_bateram_meta = []
# vendedores = len(vendas)

# for lista in vendas:
#     if lista[1] >= meta:
#         vendedores_bateram_meta.append(lista[0])

# print(' {:.1%} dos vendedores bateram a meta'.format(len(vendedores_bateram_meta)/vendedores))

# melhor_vendedor = ''
# maior_venda = 0

# for venda in vendas:
#     if venda[1] > maior_venda:
#         maior_venda = venda[1]
#         melhor_vendedor = venda[0]

# print('o melhor vendedor foi {} e no valor de venda de {}'.format(melhor_vendedor, maior_venda))

vendas = [100, 150, 1500, 2000, 120]

meta = 110

# for venda in vendas:
#     if venda < meta:
#         print('A loja não ganha bônus')
#         break
# print(venda)

# for venda in vendas:
#     if venda < meta:
#         continue
#     print(venda)

# venda = input('coloca aqui o produto')
# vendas = []

# while venda != '':
#     vendas.append(venda)
#     venda = input('Registre um produto ')


# print('finalizado, sua lista é {}'.format(vendas))
# vendedores = ['maruc', 'mard', 'assse']
# i = 0
# while vendas[i] > meta:
#     print('{} bateu {}'.format(vendedores[i], vendas[i]))
#     i += 1

list_1 = list(range(6,21))
list_1[1] = "Kenzie" 
list_1[-1] = "Academy"
# print(list_1)
# print(list_1[-1])
# print(list_1[2:5])
# print(list_1.pop())
print(list_1.pop(-1))
print(list_1.pop(1))
print(list_1)

list_2 = list_1.copy()
list_2.sort(reverse=True)
print(list_2)

print(len(list_1), len(list_2))