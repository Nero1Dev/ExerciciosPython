print('\033[33mGerador de PA')
print('-=' * 10)
primeiro_termo = int(input('\033[mPrimeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro_termo
c = 1
while c <= 10:
    print('{}'.format(termo), end= ' → ')
    c += 1 
    termo += razão
print('FIM')
