import os 
os.system('cls')

######################## STRING ########################
########################################################

# in - contido
# print('n' in 'nome')
# print('no' in 'nome')
# print('nome1' in 'nome')

# name = 'marcus vinicius nascimento ferreira'
# email = 'marcos@gmail.com'
# espacos = '     111  '

# for teste in enumerate(name):
#         print('teste {}'.format(teste))
# print(email[6:7])
# print(email[6:]) # apartir do 5 para frente ou
# print(email[:6])
# print(name[0:15])

# -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
#  l    i   r   a   @  g  m  a  i  l  .  c  o  m
#  0    1   2   3   4  5  6  7  8  9  10 11 12 13

#str - transforma em string
#in  - verifica se está contido
# + - concatena
#format {} - substitui valores
#%s - substitui textos
#%d - substitui numeros decimais

# name = 'marcus ViNicius naScimentO feRreira'

# print(name.capitalize())
# print(name.casefold())
# print(email.endswith('@gmail.com'))
# print(name.endswith('@gmail.com'))
# print(name.startswith('marcos'))
# print(email.find('@'))
# print(email.replace('@', '%'))
# print(espacos.strip())
# print(name.title())


######################### LIST #########################
########################################################

# produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']

# estoque = [100, 150, 100, 120, 70, 180, 80]
# i = produtos.index('geladeira')
# qtde_estoque = estoque[i]
# print('Quantidade em estoque da geladeira é de {}'.format(qtde_estoque))

# append adiciona item ao final

#pop(e fala o indice)

#max() min()

# vendas = [1000, 1500, 15000, 270, 900, 100, 1200]
# produtos1 = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']

# mais_vendido = max(vendas)
# i = vendas.index(mais_vendido)
# produto_mais_vendido = produtos1[i]
# print('produto mais vendido foi {}'.format(produto_mais_vendido))

# menos_vendido = min(vendas)
# i = vendas.index(menos_vendido)
# produto_menos_vendido = produtos[i]
# print('o produto menos vendido foi {}'.format(produto_menos_vendido))

# produtos_apple = ['apple tv', 'mac', 'iphone x', 'iphone 11' ]
# novos_produtos = ['iphone 12', 'ioculos']

# print(produtos_apple+novos_produtos)
#metodo sort prioriza a letra maiuscula a minuscula o ideal é converter tudo antes de dar o sort
# produtos_apple.sort()
# vendas.sort()
# vendas.sort(reverse=True)
# print(vendas)
# print(produtos_apple)


#######################  FOR  ####################

# aqui eu consigo repetir
# for i in range(5):
#     print('foda')

# # aqui eu consigo a posição
# for i in range(5):
#     print(i)
# faço o range da posição e passo o i no que eu quero comparar

# produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
# qnt = [1, 4, 2, 2, 5]

# for i in range(5):
#     print('Essas foram as minhas bebidas {} na quantidade de {}'.format(produtos[i], qnt[i]))

#se eu nao quiser deixar chumbado posso usar o len()

# produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
# qnt = [1, 4, 2, 2, 7]

# tamanho = len(produtos)

# for i in range(tamanho):
#     print('Essas foram as minhas bebidas {} na quantidade de {}'.format(produtos[i], qnt[i]))

# produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
# texto = 'olha essa porra veio'
# for produto in produtos:
#     print(produto)

# for text in texto:
#         print(text)

# vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
# meta = 1000


# for menores_que_100 in vendas:
#     if menores_que_100 <= 100:
#         print(menores_que_100)

# qtd_bateu_meta = 0

# for venda in vendas:
#     if venda >= meta:
#         qtd_bateu_meta += 1

# print(qtd_bateu_meta)#fora do for se n vai mostrar os 6

# percentual_vendas = (qtd_bateu_meta / len(vendas))*100

# print('O percentual de pessoas que bateram a meta {:.2f}%'.format(percentual_vendas))

# nomes = ['joão', 'paulo', 'carlos']

# for i, nome in enumerate(nomes):
#     print(' essa é a posição {} e esse é o nome {}'.format(i, nome))


# estoque = [1200, 49, 800]
# produtos = ['coca', 'fanta', 'sprite']
# nivel_minimo = 50

# for i, qtde in enumerate(estoque):
#     if qtde < nivel_minimo:
#         print('abaixo do nivel minimo {}'.format(produtos[i]))
    
# qtde_pessoas = int(input('Quantas pessoas terão no quarto?'))
# quarto = []
# for qtde in range(qtde_pessoas):
#     nome  = input(' Informe o nome: ')
#     cpf   = input(' Informe o cpf: ')
#     dados = [nome, 'cpf: {}'.format(cpf)] 
#     quarto.append(dados)
# print(quarto)

# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]

# for venda in vendas:
#     if venda[1] >= meta:
#         print('Vendedor {} bateu a meta. Fez {}'.format(venda[0], venda[1]))

# produtos = ['iphone', 'samsung', 'lg', 'zephone']
# vendas2019 = [1, 2, 4, 5]
# vendas2020 = [3, 1, 3, 6]

# for i, produto in enumerate(produtos):
#     if vendas2020[i] > vendas2019[i]:
#         crescimento = (vendas2020[i]/vendas2019[i] -1)
#         print('{} vendeu R${:,} em 2019, R${:,} em 2020 e teve {:.1%} crescimento'.format(produto, vendas2019[i], vendas2020[i], crescimento))
#     print()


# estoques = [
#     [20, 125, 10, 400, 500, 600, 800],
#     [194, 225, 569, 1, 500, 6, 8],
#     [394, 325, 169, 400, 500, 600, 800],
# ]
# fabricas = ['lira manufaturado', 'lira posto', 'lira farmácia']
# nivel_minimo = 50

# for i, lista in enumerate(estoques):
    
#     for qtde in lista:
#         if qtde < nivel_minimo:
#             print(fabricas[i])

estoques = [
    [20, 125, 10, 400, 500, 600, 800],
    [194, 225, 569, 1, 500, 6, 8],
    [394, 325, 169, 400, 500, 600, 800],
]
fabricas = ['lira manufaturado', 'lira posto', 'lira farmácia']
nivel_minimo = 50
fabricas_abaixo_nivel = []

for i, lista in enumerate(estoques):
    
    for qtde in lista:
        if qtde < nivel_minimo:
            if fabricas[i] in fabricas_abaixo_nivel:
                pass
            else:
                fabricas_abaixo_nivel.append(fabricas[i])

print(fabricas_abaixo_nivel)

