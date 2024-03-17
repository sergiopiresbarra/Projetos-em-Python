nome = 'sergio'
sobrenome = 'pires'
#letra = nome[2]
print(nome + ' ' + sobrenome)

frase = 'vamos aprender python hoje'
palavras = frase.split()
print(palavras)

for palavra in palavras:
    print(palavra)

print(frase[:5:-1])

email = 'sergio@gmail.com'
arroba = email.find('@')
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

produtos = 'carbonato de sodio e oxido de zinco'
print('sodio' in produtos)
print('magnesio' not in produtos)

item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)

objeto_celeste = 'galaxia esPiral M31'
print(objeto_celeste.upper())
print(objeto_celeste.capitalize())
print(objeto_celeste.title())

suplemento = 'cloreto de magnesio'
n_suplemento = suplemento.replace('magnesio', 'zinco')
print(suplemento)
print(n_suplemento)

frase = '    omega 3 é bom   '
print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())

fruta = 'abacate'
print(fruta.rjust(20))
print(fruta.center(20, '='))
print(fruta.ljust(20, '-'))

p = 'boson treinamentos'
print(p.startswith('bo'))
print(p.endswith('s'))

#docstrings
texto = """

Docstring -> documentação

"""
print(texto)

