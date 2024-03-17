elemento = {
    'Z': 3,
    'nome': 'Litio',
    'grupo': 'metais alcalinos',
    'densidade': 0.534
}

print(f'elemento: {elemento['nome']}')
print(f'densidade: {elemento['densidade']}')
print(f'tamanho: {len(elemento)}')

elemento['grupo'] = 'alcalinos'
print(elemento)

elemento['periodo'] = 1
print(elemento)

del elemento['periodo']
print(elemento)

# elemento.clear()
# print(elemento)

print(elemento.items())

print(elemento.keys())

print(elemento.values())

for i,j in elemento.items():
    print(f'{i} : {j}')

