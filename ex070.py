total = caros = menor_preço = cont = 0
nome_menor = ' '
while True:
    print('\033[36m=' * 17)
    print('Cadastrar produto')
    print('=' * 17, '\033[m')
    nome = str(input('\033[33mNome do produto: \033[m')).strip()
    preço = float(input('\033[33mPreço: R$\033[m'))
    cont += 1
    total += preço
    if cont == 1  or preço < menor_preço:
        menor_preço = preço
        nome_menor = nome
    if preço >= 1000:
        caros += 1
    continuação = ' '
    while continuação not in 'SN':
        continuação = str(input('\033[31mCadastrar mais produtos? [S/N] \033[m')).strip().upper()[0]
    if continuação == 'N':
        break
print(f'\033[32mTotal das compras foi de R${total:.2f}\033[m')
print(f'\033[32mO produto mais barato foi {nome_menor} e custou R${menor_preço:.2f}\033[m')
print(f'\033[32m{caros} produtos tem o valor acima de R$1000.00\033[m')
print('{:-^40}'.format(' FIM DO PROGRAMA '))
