import random

bocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
all = bocales + consonantes

for i in range(10):
    for j in range(10):
        name = ""
        name += random.choice(consonantes)
        name += random.choice(bocales)
        name += random.choice(bocales)
        name += random.choice(consonantes)
        name += random.choice(consonantes)
        name += random.choice(bocales)
        print(name, end=" ")
    print()

# for i in range(10):
#     for j in range(10):
#         name = "H"
#         name += random.choice(bocales)
#         name += random.choice(consonantes)        
#         name += random.choice(consonantes)
#         name += random.choice(bocales)
#         print(name, end="tech ")
#     print()

# for i in range(10):
#     for j in range(10):
#         name = "IF"
#         name += random.choice(all)
#         name += random.choice(all)        
#         name += random.choice(all)
#         name += random.choice(all)
#         print(name, end=" ")
#     print()

input()