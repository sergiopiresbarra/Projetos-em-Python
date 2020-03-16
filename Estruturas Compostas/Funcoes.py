'''def lin():
    print('=' * 30)


#Programa Principal
lin()
print(f'{"curso em video":^30}')
lin()
print(f'{"Python":^30}')
lin()
print(f'{"FIM!!!":^30}')
lin() '''


'''def mensagem(msg):
    print('='*30)
    print(f'{msg:^30}')
    print('='*30)


mensagem('curso em video')
mensagem('Python')
mensagem('FIM!!!') '''


def contador(* num): # "*" Para Variável sem tamanho definido.
    print(num)


contador(2, 1, 7)
contador(4, 4, 7, 6, 2)