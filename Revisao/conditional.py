# simple, compound, chained
n1 = n2 = 0.0
mean = 0.0

n1 = float(input('digite a primeira nota:'))
n2 = float(input('digite a segunda nota:'))

mean = (n1 + n2)/2

if mean >= 7:
    print("aprovado!")
elif (mean >= 5):
    print('recuperação!')
else:
    print("reprovado!")

print('sua média é {}'.format(mean))