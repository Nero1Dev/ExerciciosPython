lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer adicionar mais números? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('=' * 50)
print(f'Os valores digitador foram: {lista}')
print(f'{len(lista)} Numero(s) foram digitados')
print(f'Os números em ordem decrecente fica: {sorted(lista, reverse=True)}')
print('=' * 50)
