from random import randint
cont = 0
print('-=' * 10)
print('Jogo da adivinhação')
print('-=' * 10)
while True:
    computador = randint(1, 100)
    player = int(input('Digite um número: '))
    impar_par = ' '
    while impar_par not in 'PpIi':
        impar_par = str(input('Impar ou par? [I/P] ')).strip().upper()[0]
    if ((player + computador) % 2) == 0:
        print('-=' * 30)
        print(f'\033[32mVocê digitou {player} e o computador {computador} a soma é {player + computador} e é PAR\033[m')
        if impar_par == 'P':
            print('-=' * 30)
            print('''Você ganhou! \nVamos jogar de novo...''')
            print('-=' * 30)
            cont += 1
        else:
            print('\033[31mVocê Perdeu!\033[m')
            break
    else:
        print('-=' * 30)
        print(f'\033[32mVocê digitou {player} e o computador {computador} a soma é {player + computador} e é IMPAR\033[m')
        if impar_par == 'I':
            print('-=' * 30)
            print('\033[33mVocê ganhou! \n\033[33mVamos jogar de novo...\033[m')
            print('-=' * 30)
            cont += 1
        else:
            print('\033[31mVocê Perdeu!\033[m')
            break
print('-' * 33)
print(f'Você ganhou {cont} vezes consecutiva(s)')
print('-' * 33)
