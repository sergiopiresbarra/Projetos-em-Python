#style: 0-none , 1-bold , 4-underline , 7-negative/inverter
#text: 30-branco,31-red,32-verde,33-yellow,34-blue,35-roxo,36-ciano,37-gray
#background:30-branco,31-red,32-verde,33-yellow,34-blue,35-roxo,36-ciano,37-gray
#
#----codigo de cores-----
#   \033[0;33;44m
#
#\033[0;30;41m
print('\033[7;30mOlá mundo :D\033[m')
a = 3
b = 5
print('os valores sao \033[32m{} \033[me \033[31m{} \033[m!!!'.format(a, b))

#organizado em uma variável
cores = {'limpa':'\033[m'}
