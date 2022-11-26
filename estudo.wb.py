import os

os.system("cls")


alp1 = "interpolação"
# print(f'essa porra não faz sentido: {alp1.capitalize()}')


# print(alp1.count('o'))

x = [x for x in alp1]

# print(x)
# print(len(x))
# print("".join(x))
# print(type(x))
# print(type("".join(x)))


def corresponding_parenthesis(text: str):
    left = text.count("(")
    rigth = text.count(")")
    difference = left - rigth

    if difference > 0:
        return "(" * difference

    elif difference < 0:
        return ")" * (difference * -1)

    return '""'


# result = corresponding_parenthesis("((()")
# result = corresponding_parenthesis("((())")
# result = corresponding_parenthesis("((()))")
# result = corresponding_parenthesis("()))")
# result = corresponding_parenthesis("()")

# print(result)


def remove_more_than_two_repetitions(text: str):
    response = []
    response.append(text[0])
    response.append(text[1])

    for index, char in enumerate(text[2:], 2):
        if text[index - 1] != char or text[index - 2] != char:
            response.append(char)

    return "".join(response)

result = remove_more_than_two_repetitions('Ollloco meuuuu, taaa peegaando fogoo biiiiichooo')

# print(result)

x = 'Arroz com feijão e batata frita porra'

# if "a" in x:
#     print('está aqui porra')
# else:
#     print('nã está porra')

my_string = 'ola m5'
# for char in my_string:
#     if char != " ":
#         print(char)

# for i, char in enumerate(my_string):
#     print(char, i)

my_string1 = 'ola m5'
arr = []
for char in my_string1:
    if char != " ":
        arr.append(char)
# print("".join(arr))

my_string2 = 'olam5'
fat1 = my_string2[0:3]
fat2 = my_string2[3:]

jun = fat1 + ' ' + fat2

print(jun)
print(jun.split())
