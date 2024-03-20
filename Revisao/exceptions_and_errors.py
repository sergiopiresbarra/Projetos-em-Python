#blocos try ... except

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

try:
    r = round(n1/n2, 2)
except ZeroDivisionError:
    print(f'nao é possivel divisao por zero!')
else:
    print(f'resultado: {r}')
finally:
    print('='*10)


from math import sqrt
class NumeroNegativoError(Exception):
    def __init__(self):
        pass

try:
    num = int(input('digite um numero positivo: '))
    if num < 0:
        raise NumeroNegativoError
except NumeroNegativoError:
    print('numero negativo!')
else:
    print(f'raiz quadrada: {sqrt(num)}')


