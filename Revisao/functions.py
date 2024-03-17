# def <nome> ([argumentos]):
#     <instruçoes>

# def mensagem():
#     print('olá!')
#     print('fim!')

# mensagem()

def soma(a, b):
    print(a+b)

soma(12,7)

def mult(x, y):
    return x * y

print(f'produto: {mult(2,4)}')

print(f'{'='*10}')

def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere)

contar(10, '&')

