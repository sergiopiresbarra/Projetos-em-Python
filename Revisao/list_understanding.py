numeros = [1,4,7,9,10,12,21]

#quadrados = list(map(lambda num: num**2, numeros))
quadrados = [num**2 for num in numeros]
print(quadrados)

#criar uma lista de numeros pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]
print(pares)

frase = 'A logica e apenas o principio da sabedoria e nao o seu fim'
vogais = ['a','e','i','o','u']

lista_vogais = [v for v in frase if v in vogais]
print(f'a frase possui {len(lista_vogais)} vogais')

#distributiva entre valores de duas listas
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)

