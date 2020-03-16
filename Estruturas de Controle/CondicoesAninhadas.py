nome = str(input('Qual é o seu nome? '))
if nome == 'gustavo':
    print('Seu nome é bonito')
elif nome == 'pedro' or nome == 'joao' or nome == 'maria':
    print('seu nome é bem popular no brasil')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print('Tenha um bom dia, {} !'.format(nome))