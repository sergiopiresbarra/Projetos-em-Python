'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 5!')
#num.pop()

print(num) '''
#==========================================================
valores = []
'''valores.append(5)
valores.append(9)
valores.append(4)'''
#print(valores, end='')
'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}!')
print('FIM!')'''
#==========================================================
a = [2, 3, 4, 7]
b = a[:] #CÓPIA DE A PARA B
b[2] = 8
print(f'lista a: {a}')
print(f'lista b: {b}')