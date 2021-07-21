loop = 'S'
número = cont = soma = maior = menor = 0
while loop in 'Ss':
    número = int(input('Digite um número: '))
    loop = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    cont += 1
    soma += número
    if cont == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
media = soma / cont
print('Você digitou {} números ea média {}'.format(cont, media))
print('O valor maior é {} eo menor é {}.'.format(maior, menor))
