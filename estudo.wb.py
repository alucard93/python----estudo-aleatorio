import os
os.system('cls')


alp1 = 'interpolação'
# print(f'essa porra não faz sentido: {alp1.capitalize()}')


# print(alp1.count('o'))

x = [x for x in alp1]

# print(x)
# print(len(x))
# print("".join(x))
# print(type(x))
# print(type("".join(x)))

def corresponding_parenthesis(text: str):
    left  = text.count("(")
    rigth = text.count(")")
    difference = left - rigth
    
    if difference > 0:
        return "(" * difference
    
    elif difference < 0:
        return ")" * (difference * -1)
    
    return ""

# result = corresponding_parenthesis("((()")
# result = corresponding_parenthesis("((())")
# result = corresponding_parenthesis("((()))")
# result = corresponding_parenthesis("()))")
# print(result)