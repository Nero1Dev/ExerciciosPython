valores = list()
cont = 0
while True:
    cont += 1

    var = int(input('Adicione valor: '))

    if var not in valores:
        valores.append(var)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não adicionar...')

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

valores.sort()
print(f'Você digitou os valores: {valores}')
