valores = []
mais = 0
menos = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))

if valores[0] != mais or menos:
    mais = valores[0]
    menos = valores[0]
for c in range(0, 5):
    if valores[c] < menos:
        menos = valores[c]
    if valores[c] > mais:
        mais = valores[c]

# maislugar = valores.index(mais)
# menoslugar = valores.index(menos)

print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {menos}')
print(f'O maior valor digitado foi {mais}')