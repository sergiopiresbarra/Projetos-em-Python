import os

#print(os.listdir())
#os.chdir('.\\Revisao')
#manipulador = open('arquivo.txt', 'r', encoding='utf-8')

#print(f'metodo read(): {manipulador.read()}')
print('\n')
#print(manipulador.readline())

#print(manipulador.readlines())
# texto = input('qual termo deseja procurar no arquivo?')

# try:
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'a string foi encontrada!')
#             print(linha)
# except IOError:
#     print('nao foi possivel abrir arquivo')
# else:
#     manipulador.close()

try:
    #manipulador = open('arquivo.txt', 'w', encoding='utf-8')
    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
    manipulador.write('\nPython é muito usado em IA')
    manipulador.write('\n'+'='*20)
except IOError:
    print('nao foi possivel abrir o arquivo!')
else:
    manipulador.close()
