# funcoes lambda (anonimas)
# sintaxe: 
# lambda argumentos: expressao

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x % 2 == 0
# print(par(9))

f_c = lambda f: (f -32) * 5/9
print(f_c(212))

#fucao map()
#sintaxe:
#map(funcao, iterável)

num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x*2, num))
print(dobro)

palavras = ['python', 'é', 'uma', 'linguagem','de', 'programacao']
maiusculas = list((map(str.upper, palavras)))
print(maiusculas)

# funcao filter()
# sintaxe:
# filter(funcao, sequencia)

# def numeros_pares(n):
#     return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

num_impar = list(filter(lambda x: x%2 != 0, numeros))
print(num_impar)

# funcao reduce()
# sintaxe:
# reduce(funcao, sequencia, valor_inicial)
from functools import reduce

def mult(x,y):
    return x*y

numeros = [1,2,3,4,5,6]
total = reduce(mult, numeros)
print(total)

#soma cumulativa dos quadrados de valores,usando lambda
numeros = [1,2,3,4]
# ((1^2 + 2^2)^2 + 3^2)^2+ 4^2
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)