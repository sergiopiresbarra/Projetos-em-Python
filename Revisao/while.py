num = 1

while num <= 10:
    print(num)
    num += 1

name = None
while True:
    name = input('digite seu nome ou x para sair:')
    if name == 'x' or name == 'X':
        break
    print(name)

print(name)