# Fatiamento
frase = 'Curso em Video Python'
print(frase[9:14])  # fatia de 9 até 13
print(frase[9:21])  # fatia de 9 até 20
print(frase[9:21:2])  # pulando de 2 em 2
print(frase[:5]) # do inicio até o 4
print(frase[15:]) # do 15 até o final
print(len(frase)) # comprimento da string
print(frase.count('o')) # verifica quantos 'o' existem
print(frase.count('o',0,13)) # quantos 'o' existem de 0 à 12
print(frase.find('deo')) # encontra a posição que esta 'deo'
print('Curso' in frase) #se existe 'Curso' em frase, retorna True ou False

#Transformação
print(frase.replace('Python','Android')) #substitui o Python por Android
print(frase.upper())#mauisculas
print(frase.lower())#minusculas
frase = '   Aprenda Python  '
print(frase.strip())#Remove os espaços inuteis do comeco e do final
frase = frase.split()#divide a frase em listas
print(frase)
frase = '-'.join(frase)#junta as listas através de '-'
print(frase)
