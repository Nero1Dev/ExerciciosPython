núm = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2  == 0: núm[0].append(valor)
    else: núm[1].append(valor)

print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os números pares são {núm[0]}')
print(f'Os números impares são: {núm[1]} ')
