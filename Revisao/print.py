# print(objetos, argumentos)

""" msg = 'print function()'
print(msg)
print('Python Class')

name = 'sergio pires'
print('curso de python -', name)
 """

name = input('digite o nome: ')
msg = 'ola ' + name + '! Bem vindo!'
print(msg)

print('...')

print('muda de linha.')
print('permanece na linha.', end='')
print('continua na mesma linha.')

print('...')

name = 'maria'
age = 30
msg = 'her name is {0} and has {1} years old.'.format(name,age)
print(msg)

print('...')

name = 'fabio'
weight = 73.50
msg = f'ola, o nome é {name}, e pesa {weight} quilos.'
print(msg)

value = 125.435364
print(f'o valor é: \'{value:.2f}\'')