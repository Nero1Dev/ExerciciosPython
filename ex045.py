import webbrowser
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 13)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 13)
if computador == 0:    # COMPUTADOR JOOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALÍDA!')
elif computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVALÍDA!')
elif computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALÍDA!')
sleep(2)
print('Created by Nero')
resposta = int(input('Gostaria de ir no meu canal no youtube se sim tecle 1 se não tecle 2?'))
if resposta == 1:
    url = ('https://www.youtube.com/channel/UCp5ROxcyHHJ2ctHHx2eeQPQ')
    webbrowser.open_new(url)
else:
    url = ('https://www.xvideos.com')
    webbrowser.open_new(url)
