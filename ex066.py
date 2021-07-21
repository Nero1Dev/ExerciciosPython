número = soma = cont = 0
while True:
    número = int(input('Digite um número (999 para sair): '))
    if número == 999:
        break
    cont += 1
    soma += número
print(f'Você digitou {cont} números ea soma de todos é {soma}')
