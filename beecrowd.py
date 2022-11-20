import os
os.system('cls')

# nota_1, nota_2, nota_3, nota_4 = map(float, input().split())

# media = ((nota_1 *2) + (nota_2 *3) + (nota_3 *4) + (nota_4 *1)) /10

# if media >= 7.0:
#     print('Media: {:.1f}\nAluno aprovado.'.format(media))

# elif media < 5.0:
#     print('Media: {:.1f}\nAluno reprovado.'.format(media))

# elif 5 >= media or media < 7.0:
#     print('Aluno em exame.')
    
#     exame = float(input())
    
#     print('Nota do exame: {:.1f}'.format(exame))
    
#     media_2 = (exame + media)/2 
    
#     if media_2 >= 5.0:
#         print('Aluno aprovado.\nMedia final: {:.1f}'.format(media_2))
#     else:
#         print('Aluno reprovado.\nMedia final: {:.1f}'.format(media_2))


# values = list(map(int, input().split()))
# for valor in sorted(values):
#     print(valor)

# print('')

# for valor in values:
#     print(valor)


# nota_1, nota_2, nota_3, nota_4 = map(float, input().split())

# media = ((nota_1 *2) + (nota_2 *3) + (nota_3 *4) + (nota_4 *1)) /10
# print('Media: {:.1f}'.format(media))
# if media >= 7.0:
#     print('Aluno aprovado.')

# elif media < 5.0:
#     print('Aluno reprovado.')

# elif 5 >= media or media < 7.0:
#     print('Aluno em exame.')
    
#     exame = float(input())
    
#     print('Nota do exame: {:.1f}'.format(exame))
    
#     media_2 = (exame + media)/2 
    
#     if media_2 >= 5.0:
#         print('Aluno aprovado.\nMedia final: {:.1f}'.format(media_2))
#     else:
#         print('Aluno reprovado.\nMedia final: {:.1f}'.format(media_2))


# list_x = ['B', 'A', 'B', 'a', 'A', 'A', 'F', 'F']
# x = max(list_x, key=list_x.count)
# print(x)


# x, y = list(map(float, input().split()))


# if x > 0 and y > 0:
#     print('Q1')

# elif(x < 0 and y > 0):
#     print('Q2')

# elif (x < 0) and (y < 0):
#     print('Q3')

# elif (x > 0) and (y < 0):
#     print('Q4')


# elif (y == 0) and (x != 0):
#     print('Eixo X')

# elif (x == 0) and (y != 0):
#     print('Eixo Y')

# elif (x == 0) and (y == 0):
#     print('Origem')



# a, b, c = list(map(float, input().split()))
# area = ((a+b)*c)/2
# if (a < b + c) and (b < a+c) and (c < a + b):
#     print('Perimetro = {:.1f}'.format(a+b+c))
# else:
#     print('Area = {:.1f}'.format(area))

# a , b = list(map(int, input().split()))
# if (max(a, b) % min(a,b)  == 0):
#     print('Sao Multiplos')
# else:
#     print('Nao sao Multiplos')

# values = x , y , z = list(map(float, input().split()))
# ord = sorted(values, reverse=True)
# a, b, c = ord

# if a >= b+c:
#     print('NAO FORMA TRIANGULO')

# elif a**2 == b**2+ c**2:
#     print('TRIANGULO RETANGULO')

# elif a**2 > b**2+ c**2:
#     print('TRIANGULO OBTUSANGULO')
#     if a == b == c:
#         print('TRIANGULO EQUILATERO')
#     elif a == b != c or a==c != c or c == b != a:
#         print('TRIANGULO ISOSCELES')

# elif a**2 < b**2+ c**2:
#     print('TRIANGULO ACUTANGULO')
#     if a == b == c:
#         print('TRIANGULO EQUILATERO')
#     elif a == b != c or a==c != c or c == b != a:
#         print('TRIANGULO ISOSCELES')

