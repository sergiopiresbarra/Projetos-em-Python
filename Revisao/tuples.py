#tuples sao imutaveis
tuple1 = (2,4,6,7,9)
print(tuple1)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases = ('He', 'Ne', 'Ar', 'Xe', 'Rn')
elements = halogenios + gases

print(elements)
print(elements.count('Ne'))

print(halogenios[0:2])
print('Cl' in halogenios)

grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)

grupo1 = ['a','b','c','d']

grupo2 = tuple(grupo1)
print(grupo2)