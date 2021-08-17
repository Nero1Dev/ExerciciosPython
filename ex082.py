valores = list()
par = list()
impar = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Continuar? [S/N] '))

    if continuar in 'Nn':
        break

for c in range(0, len(valores)):
    n = valores[c] % 2
    if n == 0: par.append(valores[c])

    else: impar.append(valores[c])

print(f'Todos os valores são: {valores}')
print(f'Pares: {par}')
print(f'Impar: {impar}')
