números = ('zero', 'úm', 'dois', 'três', 'quatro', 
'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'quatorse',
'quinze', 'dezesseis', 'desesete', 'dezoito',
'desenove', 'vinte')

while True:
    while True:
        number = int(input('Digite um número entre 0 e 20: '))
        if 0 <= number <= 20:
            break
        print('Tente Novamente. ', end=' ')
    print(f'Você digitou {números[number]}')
    pause = str(input('Você que continuar? [S/N] ')).strip().upper()[0]
    if pause == 'N':
        break
    