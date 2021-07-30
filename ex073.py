tabela = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino',
'Atlético-PR', 'Flamengo', 'Ceará', 'Atlético-GO', 
'Bahia', 'Corinthians', 'Fluminense', 'Santos', 
'Juventude', 'Internacional', 'Cuiabá', 'Sport', 
'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')

print('=-' * 35)
print(f'Lista completa: {tabela}')
print('=-' * 35)

print(f'Os 5 primeiros time da tabela são: {tabela[0:5]}')
print('=-' * 35)

print(f'Os 4 últimos times da tabela: {tabela[-4:]}')
print('=-' * 35)

print(f'Os  times em ordem alfabética: {sorted(tabela)}')
print('=-' * 35)

print(f'O Chapecoense esta na {tabela.index("Chapecoense") + 1}ª posição')
print('=-' * 35)        
