# list = [2,6,9,4,0,12,3,7]
# word = 'boson'

# for item in list:
#     print(item, end=" ")

# print()

# for letter in word:
#     print(letter, end=" ")

# for number in range(1,11):
#     print(number)

# name = input('digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {name}')

#range(valor inicial, valor_final -1, incremento)
# for x in range(2,20,2):
#     print(x)

stones = ('ruby', 'emerald', 'quartzo', 'safira', 'diamond', 'turmalina')

for stone in stones:
    if stone == 'quartzo':
        continue
    print(stone)