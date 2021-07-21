maior_peso = 0 
menor_peso = 0
for p in range(1, 6):
    peso = float(input('\033[33mPeso da {}º pessoa: \033[m'.format(p)))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('\033[1;31mO maior peso lido foi de {}Kg\033[0;0m'.format(maior_peso))
print('\033[1;31mO menor peso lido foi de {}Kg\033[0;0m'.format(menor_peso))
