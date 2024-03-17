planeta_nao = {'plutao','ceres','eris','haumea','makemake'}

print(planeta_nao)
print('ceres' in planeta_nao)

for astro in planeta_nao:
    print(astro.upper())

astros = ['lua', 'venus', 'sirius', 'marte', 'lua']
print(astros)

astro_set = set(astros)
print(astro_set)

print(f'{'='*10}')

astros1 = {'lua', 'venus', 'sirius', 'marte'}
astros2 = {'lua', 'venus', 'sirius', 'marte', 'cometa halley'}

#união de conjuntos
print(astros1 | astros2)
#interseção
print(astros1 & astros2)
#diferença simetrica
print(astros1 ^ astros2)

astros1.add('urano')
astros1.add('sol')
print(astros1)
astros1.remove('sol')
print(astros1)

#remove um elemento aleatoriamente
astros1.pop()
print(astros1)

astros1.clear()
print(astros1)