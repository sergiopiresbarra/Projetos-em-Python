#formula geral para o fatorial
#fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base'
#fatorial(num) = num * fatorial(num -1), para num >1 'Caso-Recursivo'
# 4! => 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1)
# 4! = 4 * 3 * 2 * 1 = 24

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num-1)
    
print(fatorial(900))