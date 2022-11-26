import os

os.system("cls")
# pessoa = {"nome": "José da Silva", "idade": 36, "sexo": "masculino"}

# pessoa["nome"] = "Marcus" # Mudando o valor do campo


# print(pessoa)
# print(pessoa.keys())

# pesquisando um campo no dicionário

# print("Esse é o nome do craque: {}".format(pessoa["nome"]))


paises = {
    "BRA": "Brasil",
    "EUA": "Estados Unidos",
    "FRA": "França",
    "ESP": "Espanha",
    "ALE": "Alemanha",
}

# para adicionar um campo
paises["POR"] = "Portugal"
# print(paises)

# print(paises.get('SUI', 'Chave não encontrada'))


# para remover um item do dicionário
# paises.pop('ALE')
# print(paises)

# para percorrer pares em um dicionario
# for chave, valor in paises.items():
#     print(chave + '=' + valor)

dicio_2 = {"primeiro": 1, "segundo": 2, "terceiro": 3}

# para acessar as chaves
# print(dicio_2.keys())

# para acessar os valores
# print(dicio_2.values())

# para acessar os 2 valores
# print(dicio_2.items())


# crio um dicionario passo chave e valor
dicio = dict(primeiro=1, segundo=2, terceiro=3)
nomes_idades = dict(nome="marcus", idade=29)
quarto = dict(rig=2, cadeiras=2, ventilador=1, arcondicionado=1)
casa = dict(quarto1="vinicius", quarto2="pais", sala="todos")

# print(nomes_idades)
# print(quarto)
# print(casa)
# print(dicio)

# a = ['primeiro', 'segundo', 'terceiro']
# b = [1, 2, 3]

# para juntar dicionarios
# dicio_3 = dict(zip(a, b))
# dicio_3 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))

# print(dicio_3)


# percorrer as chaves

# for key in paises.keys():
#     print(key)


# percorrer os valores

# for values in paises.values():
#     print(values)


# com o .items() você acessa o dado mas não consegue interar sobre o dado

frutas = {'pera': 10, 'uva': 2, 'maça': 55}

# print(frutas.items())

# for chaves, valores in frutas.items():
#     print(f"Chave =  {chaves} - Valor {valores} ")

#Verificar se uma chave existe
# if 'uva' in frutas:
#     print(f"A fruta desejada existe: {frutas['uva']}")

# # Verificar se um valor existe

# if 10 in frutas.values():
#     print('O valor desejado existe')

# deleta e retornar
# frutas.pop("pera")
# print(frutas)

# hora_inicial, minuto_inicial, hora_final, minuto_final = map(int,(input().split()))

# minuto_inicial += hora_inicial * 60
# minuto_final += hora_final * 60

# duracao = minuto_final - minuto_inicial

# if duracao <= 0:
#     duracao += 24 * 60

# h = duracao // 60
# m = duracao % 60


# print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))


# salario = float(input())

# if salario >=0 and salario <= 400:
#     reajuste = salario*0.15
#     print('Novo salario: {:.2f}'.format(salario+reajuste))
#     print('Reajuste ganho: {:.2f}'.format(reajuste))
#     print('Em percentual: 15 %')

# elif (salario >=400.01) and (salario <= 800):
#     reajuste = salario*0.12
#     print('Novo salario: {:.2f}'.format(salario+reajuste))
#     print('Reajuste ganho: {:.2f}'.format(reajuste))
#     print('Em percentual: 12 %')

# elif (salario >=800.01) and (salario <= 1200):
#     reajuste = salario*0.10
#     print('Novo salario: {:.2f}'.format(salario+reajuste))
#     print('Reajuste ganho: {:.2f}'.format(reajuste))
#     print('Em percentual: 10 %')

# elif (salario >=1200.01) and (salario <= 2000):
#     reajuste = salario*0.07
#     print('Novo salario: {:.2f}'.format(salario+reajuste))
#     print('Reajuste ganho: {:.2f}'.format(reajuste))
#     print('Em percentual: 7 %')

# elif (salario > 2000):
#     reajuste = salario*0.04
#     print('Novo salario: {:.2f}'.format(salario+reajuste))
#     print('Reajuste ganho: {:.2f}'.format(reajuste))
#     print('Em percentual: 4 %')
    

# v_inv, car, tipo = map(str, input().split())

# if v_inv.upper() == 'VERTEBRADO' and car.upper() == 'AVE' and tipo.upper() == 'CARNIVORO':
#     print('aguia')

# elif v_inv.upper() == 'VERTEBRADO' and car.upper() == 'AVE' and tipo.upper() == 'ONIVORO':
#     print('pomba')

# elif v_inv.upper() == 'VERTEBRADO' and car.upper() == 'MAMIFERO' and tipo.upper() == 'ONIVORO':
#     print('homem')

# elif v_inv.upper() == 'VERTEBRADO' and car.upper() == 'MAMIFERO' and tipo.upper() == 'HERBIVORO':
#     print('vaca')

# elif v_inv.upper() == 'INVERTEBRADO' and car.upper() == 'INSETO' and tipo.upper() == 'HEMATOFAGO':
#     print('pulga')

# elif v_inv.upper() == 'INVERTEBRADO' and car.upper() == 'INSETO' and tipo.upper() == 'HERBIVORO':
#     print('lagarta')

# elif v_inv.upper() == 'INVERTEBRADO' and car.upper() == 'ANELIDEO' and tipo.upper() == 'HEMATOFAGO':
#     print('sanguessuga')

# elif v_inv.upper() == 'INVERTEBRADO' and car.upper() == 'ANELIDEO' and tipo.upper() == 'ONIVORO':
#     print('minhoca')

# c1 = input()
# c2 = input()
# c3 = input()

# print(type(c1))
# if c1.upper() == 'VERTEBRADO' and c2.upper() == 'AVE' and c3.upper() == 'CARNIVORO':
#     print('aguia')

# elif c1.upper() == 'VERTEBRADO' and c2.upper() == 'AVE' and c3.upper() == 'ONIVORO':
#     print('pomba')

# elif c1.upper() == 'VERTEBRADO' and c2.upper() == 'MAMIFERO' and c3.upper() == 'ONIVORO':
#     print('homem')

# elif c1.upper() == 'VERTEBRADO' and c2.upper() == 'MAMIFERO' and c3.upper() == 'HERBIVORO':
#     print('vaca')

# elif c1.upper() == 'INVERTEBRADO' and c2.upper() == 'INSETO' and c3.upper() == 'HEMATOFAGO':
#     print('pulga')

# elif c1.upper() == 'INVERTEBRADO' and c2.upper() == 'INSETO' and c3.upper() == 'HERBIVORO':
#     print('lagarta')

# elif c1.upper() == 'INVERTEBRADO' and c2.upper() == 'ANELIDEO' and c3.upper() == 'HEMATOFAGO':
#     print('sanguessuga')

# elif c1.upper() == 'INVERTEBRADO' and c2.upper() == 'ANELIDEO' and c3.upper() == 'ONIVORO':
#     print('minhoca')

# value = int(input())

# if value == 61:
#     print('Brasilia')

# if value == 71:
#     print('Salvador')

# if value == 11:
#     print('Sao Paulo')

# if value == 21:
#     print('Rio de Janeiro')

# if value == 32:
#     print('Juiz de Fora')

# if value == 19:
#     print('Campinas')

# if value == 27:
#     print('Vitoria')

# if value == 31:
#     print('Belo Horizonte')


# value = int(input())
# ddd = {
#     61: 'Brasilia', 
#     71: 'Salvador',
#     11: 'Sao Paulo',
#     21: 'Rio de Janeiro',
#     32: 'Juiz de Fora',
#     19: 'Campinas',
#     27: 'Vitoria',
#     31: 'Belo Horizonte',
#     }

# print(ddd.get(value, 'DDD não cadastrado'))

# renda = float(input())

# if renda == 0 and renda <= 2000:
#     print("Isento")

# elif renda >= 2000.01 and renda <= 3000:
#     conta = (renda - 2000)*0.08
#     print('R$ {:.2f}'.format(conta))

# elif renda >= 3000.01 and renda <= 4500:
#     conta = (renda - 3000)*0.18 + (1000 * 0.08)
#     print('R$ {:.2f}'.format(conta))

# elif renda > 4500:
#     conta = (renda - 4500)*0.28 + (1500 * 0.18) + (1000*0.08)
#     print('R$ {:.2f}'.format(conta))


# value = int(input())

# meses = {
#         1: 'January', 
#         2: 'February',
#         3: 'March',
#         4: 'April',
#         5: 'May',
#         6: 'June',
#         7: 'July',
#         8: 'August',
#         9: 'September',
#         10:'October',
#         11:'November',
#         12:'December',
#         }

# mes = meses.get(value)
# print(mes)

# for num in range(1, 101):
#     if num % 2 == 0:
#         print(num)

# arr = a, b, c, d, e, f = list(map(float, input().split()))
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# f = float(input())

# arr = [a, b, c, d, e, f]
# # positivos = [numeros for numeros in arr if numeros >= 0]
# # print(positivos)

# d1 = int(input().split()[1])
# h1, m1, s1 = map(int, input().split(":"))

# t1 = s1 + m1*60 + h1*60*60 + d1*24*60*60

# d2 = int(input().split()[1])
# h2, m2, s2 = map(int, input().split(":"))

# t2 = s2 + m2*60 + h2*60*60 + d2*24*60*60

# dif = t2-t1
# d = dif//(24*60*60)
# dif = dif(24*60*60)

# h = dif//(60*60)
# dif = dif%(60*60)

# m = dif//(60)
# dif = dif%(60)

# s = dif

# print(f"{d} dia(s)")
# print(f"{h} hora(s)")
# print(f"{m} minuto(s)")
# print(f"{s} segundo(s)")




# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# f = float(input())

# arr = [a, b, c, d, e, f]

# positivos = []
# soma = 0
# for num in arr:
#     if num >= 0:
#         positivos.append(num)
#         soma += num 

# print('{} valores positivos'.format(len(positivos)))
# print('{:.1f}'.format(soma/len(positivos)))


# a = abs(int(input()))
# b = abs(int(input()))
# c = abs(int(input()))
# d = abs(int(input()))
# e = abs(int(input()))

# arr = [a, b, c, d, e]
# pares = []
# for num in arr:
#     if num % 2 == 0:
#         pares.append(num)

# print('{} valores pares'.format(len(pares)))

# par      = 0
# impar    = 0
# positivo = 0
# negativo = 0

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# arr = [a, b, c, d, e]

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         par += 1
    
#     elif arr[i] % 2 == 1:
#         impar += 1
    
#     elif arr[i] > 0:
#         positivo += 1
    
#     elif arr[i] < 0:
#         negativo +=1

# print('{} valor(es) par(es)'.format(par))
# print('{} valor(es) impar(es)'.format(impar))
# print('{} valor(es) positivo(s)'.format(positivo))
# print('{} valor(es) negativo(s)'.format(negativo))
