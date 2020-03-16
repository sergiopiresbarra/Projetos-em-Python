#Interactive Help
#comando:  help()
#exemplo:  help(print)

#Docstrings
'''
def contador(i, f, p):
    """
        ->Faz uma contagem e mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c=i
    while c<= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')


help(contador)
'''

#Paranmetros Opcionais
'''
def somar(a=0, b=0, c=0):
    """
    ->Faz a soma de tres valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar()
'''

#Retorno de Função
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(3 , 3)
r3 = somar(5)
print(f'a somas valem {r1}, {r2}, {r3}')