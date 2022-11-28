import os 
os.system('cls')

list_1 = list(range(6,21))
# print(list_1)

# print(list_1[-1])

list_1[1] = 'Kenzie'
# print(list_1)

# print(list_1[2:5])

list_1.append('Academy')
# print(list_1)

list_1.remove('Kenzie')
list_1.remove('Academy')
list_2 = sorted(list_1.copy(), reverse=True)

# print(len(list_1))
# print(len(list_2))
# print(list_1)
# print(list_2)

print(list_1.pop())
print(list_2.pop())

print(list_1.clear())
print(list_2.clear())