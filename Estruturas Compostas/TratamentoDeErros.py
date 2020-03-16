try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi: {erro.__class__}')

else:
    print(f'o resultado foi {r:.1f}')
finally:
    print('Volte sempre! Obrigado!')