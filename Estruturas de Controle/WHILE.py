'''for c in range(1, 10):
    print(c)
print('FIM!!')'''
c = 1
'''while c < 10:
    print(c)
    c = c + 1
print('FIM!!') '''

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
