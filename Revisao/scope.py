#escopo global e local

var_global = 'curso de python'

def escreve_texto():
    global var_global
    var_global = 'Banco de dados'
    var_local = 'Sergio'
    print(f'variavel global: {var_global}')
    print(f'variavel local: {var_local}')


if __name__ == '__main__':
    escreve_texto()
    print(var_global)
    # print(f'variavel global: {var_global}')
    # print(f'variavel local: {var_local}')