from random import sample
from time import sleep

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
qtd_de_jogos = int(input('Quantos jogos serão sorteados? '))
print('-=' * 3, f'SORTEANDO {qtd_de_jogos} JOGOS', '-=' * 3)
for c in range(qtd_de_jogos):
    palpite = sorted(sample(range(1, 61), 6))
    sleep(0.7)
    print(f'Jogo {c+1}: {palpite}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
