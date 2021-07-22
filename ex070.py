total = maior_preço = 0
menor_preço = 0
nome_maior = nome_menor = ' '
while True:
    print('\033[36m=' * 17)
    print('Cadastrar produto')
    print('=' * 17, '\033[m')
    nome = str(input('\033[33mNome: \033[m')).strip()
    preço = float(input('\033[33mPreço: R$\033[m'))
    total += preço
    if preço > maior_preço:
        maior_preço = preço
        nome_maior = nome
    if menor_preço == 0:
        menor_preço = preço
    if preço < menor_preço:
        menor_preço = preço
        nome_menor = nome
    continuação = ' '
    while continuação not in 'SN':
        continuação = str(input('\033[31mCadastrar mais produtos? [S/N] \033[m')).strip().upper()[0]
    if continuação == 'N':
        break
print(f'\033[32mTotal das compras foi de R${total:.2f}\033[m')
print(f'\033[32mO produto mais caro foi {nome_maior} e custou R${maior_preço:.2f}\033[m')
print(f'\033[32mO produto mais barato foi {nome_menor} e custou R${menor_preço:.2f}\033[m')
