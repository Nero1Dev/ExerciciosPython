valores = []
mais = 0
menos = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))


    if c == 0:
        mais = menos = valores[c]
    else:
        if valores[c] < menos:
            menos = valores[c]
        if valores[c] > mais:
            mais = valores[c]

print('=-' * 30)

print(f'Você digitou os valores {valores}')

print(f'O menor valor digitado foi {menos} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menos:
        print(f'{i}... ', end='')
print()
print(f'O maior valor digitado foi {mais} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mais:
        print(f'{i}... ', end='')
print()
