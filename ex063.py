print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
number = int(input('Quantos termos deseja que sejam mostrados? '))
cont = 0
t1  = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end= '')
while cont <= number:
    t3 = t1 + t2 
    print(' → {} '.format(t3), end= '')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
