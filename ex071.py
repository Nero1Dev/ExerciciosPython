print('=' * 30)
print('{:^30}'.format('BANCO NERO'))
print('=' * 30)
saque = int(input('Quanto dinheiro você quer sacar? R$'))
total = saque
cédulas = 50
totalcédulas = 0
while True:
    if total >= 50:
        total -= cédulas
        totalcédulas += 1
    else:
        if totalcédulas > 0:
            print(f'Total de {totalcédulas} cédulas de R${cédulas}')
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 1
        totalcédulas = 0
        if total == 0:
            break
print(f'Acabou')