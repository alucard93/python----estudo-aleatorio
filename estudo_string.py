import os 
os.system('cls')
# # curso = "      CuRsO De pYthon   "
# # arr = ["arroz", "feijão", "sushi"]
# # arr1 = "SuShi"


# # # os 2 pontos significa até
# # print(curso.strip()[6:8])

# # # len() é utilizado para dizer o tamanho
# # print(len(curso))

# # # .strip() é utilizado para remover espaços vazios
# # print(curso.strip())

# # # .lower é utilizado para converter tudo para minusculo
# # print(curso.lower())

# # # .upper é utilizado para converter tudo para maiusculo
# # print(curso.upper())

# # # .replace é utilizado para trocar algum determinado char
# # print(curso.lower().replace("curso", "suruba"))

# # #split() utilizado para transformar uma string em um array
# # print(curso.strip().lower().split(" "))

# # # in utilizado para saber se está incluso e retorna True ou False posso usar o not
# # res = "sushi" in arr
# # res1 = "sush" not in arr
# # res2 = arr1.lower() in arr

# # print(res)
# # print(res1)
# # print(res2)

# # cidade = "Rio de Janeiro"
# # dia = 15
# # mes = "Abril"
# # ano = 2022
# # # \n quebra linha - \ escapa algo das aspas
# # # \t tabulação \r tipo apertar o enter
# # # \b apagar o caracter anterior
# # print(f"dia: {dia} do mês: {mes} do ano: {ano}")
# # print("dia: {} do mês: {} do ano: {}".format(dia, mes, ano))


# nome = 'marcus'
# sobrenome = 'vinicius'
# nome_completo = nome + " " + sobrenome

# # title() pega a primeira letra e coloca para maiusculo respeitando imutabilidade
# print(nome_completo.title())

# # startswith() utilizado para checar se a primeira letra ou a primeira palavra(posso definir outras posições)
# # endswith() inverso do start

# myStr = "python é doido"
# print(myStr.startswith('p'))
# print(myStr.startswith('o',4))
# print(myStr.startswith('thon',2,6))
# print(myStr.endswith('python é', 0 ,8))

# valores = input().split()
# a = float(valores[0])
# b = float(valores[1])
# c = float(valores[2])
# pi = 3.14159

# area_triangulo  = (a *c)/ 2
# area_circulo    = (pi *pow(c,2))
# area_trapezio   = ((a + b) * c)/2
# area_quadrado   = pow(b,2)
# area_retangulo  = a * b

# print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo))

# values = input().split()
# a = int(values[0])
# b = int(values[1])
# c = int(values[2])

# maior = max(a,b,c)
# print('{} eh o maior'.format(maior))

# x = int(input())
# y = float(input())

# media = x/y

# print('{:.3f} km/l'.format(media))

# p1 = input().split()
# p2 = input().split()

# x1 = float(p1[0])
# x2 = float(p2[0])

# y1 = float(p1[1])
# y2 = float(p2[1])

# f = ((x2-x1)**2 +(y2-y1)**2)**(1/2)
# print('{:.4f}'.format(f))

# autonomia = 12
# v_h = int(input())
# tempo = int(input())
# total = (v_h/autonomia)*tempo
# print('{:.3f}'.format(total))

# valor = int(input())

# cedulas = [100, 50, 20, 10, 5, 2 , 1]

# print(valor)

# for cedula in cedulas:
#   qt_cedulas = int(valor / cedula)
#   print("{} nota(s) de R$ {:.2f}".format(qt_cedulas, cedula))
#   valor -= qt_cedulas * cedula

# segundos = int(input())
# h = segundos / 3600
# r = segundos % 3600
# m = r / 60
# s = r % 60
# print('%i:%i:%i'%(h, m, s))

# dias = int(input())
# mes = 30
# ano = 365

# cal_a = dias/365
# r = dias % 365

# cal_mes = r / 30

# d = r%30

# print('{:.0f} ano (s)'.format(cal_a))
# print('{:.0f} mes (es)'.format(cal_mes))
# print('{:.0f} dia (s)'.format(d))

# valor = float(input())

# notas = [100, 50, 20, 10, 5, 2]
# moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

# print('NOTAS:')
# for nota in notas:
#     quantidade_notas = int(valor / nota)
#     print('{} nota(s) de R$ {:.2f}'.format(quantidade_notas, nota)) 
#     valor -= quantidade_notas * nota
# print('MOEDAS:')
# for moeda in moedas:
#     quantidade_moedas = int(round(valor,2)/moeda)
#     print('{} moeda(s) de R$ {:.2f}'.format(quantidade_moedas, moeda))
#     valor -= quantidade_moedas * moeda

# values = input().split()
# a = int(values[0])
# b = int(values[1])
# c = int(values[2])
# d = int(values[3])

# if (b > c) and (d > a ) and (c+d > a+b) and (c+d > c>0) and (d > 0) and (a % 2 == 0):
#     print('Valores aceitos')
# else:
#     print('Valores nao aceitos')

# # import math
# a, b, c = [float(x) for x in input().split(" ")]
# print('{} {} {}'.format(a,b,c))
# try:
#     delta = b * b - 4 * a * c
#     r1 = (-b + math.sqrt(delta)) / (2 * a)
#     r2 = (-b - math.sqrt(delta)) / (2 * a)

#     print('R1 = {:.5f}'.format(r1))
#     print('R2 = {:.5f}'.format(r2))

# except:
#     print('Impossivel calcular')


# x = float(input())

# if 0 <= x <= 25:
#     print('Intervalo [0,25]')

# elif 25 < x <= 50:
#     print('Intervalo (25,50]')

# elif 50 < x <= 75:
#     print('Intervalo (50,75]')

# elif 75 < x <= 100:
#     print('Intervalo (75,100]')

# else:
#     print('Fora de intervalo')

id, quantidade = map(int, input().split())
valor = 0

if id == 1:
    valor = 4.0

elif id == 2:
    valor = 4.5

elif id == 3:
    valor = 5.0

elif id == 4:
    valor = 2.0

elif id == 5:
    valor = 1.5
else:
    print('id inválido')

print(f'Total: R$ {valor*quantidade:.2f}')
