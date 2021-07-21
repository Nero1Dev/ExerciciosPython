'''from math import factorial
n = int(
    input(
    'Digite um número para calcular seu fatorial: '
    )
)
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''
number = int(input('Qual o valor a ser calculado: '))
cont = number
fato = 1
print('Calculando... {}! = '.format(number), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = {}'.format(fato), end='')
    fato *= cont
    cont -= 1
