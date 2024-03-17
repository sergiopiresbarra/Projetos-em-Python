import random

# value = random.randint(1,20)
# print(value)

# for i in range(5):
#     n = random.randint(1,50)
#     print(f'numero: {n}')

# value = random.random()
# print(f'numero: {round(value*10, 2)}')

# value = random.uniform(1,100)
# print(value)

l = [2,4,6,9,10,13,14,15,16,18,20,21]

# n = random.choice(l)
# print(f'numero escolhido: {n}')

# n = random.sample(l, 3)
# print(n)

print(f'lista original: {l}')
n = random.shuffle(l)
print(f'lista embaralhada: {l}')