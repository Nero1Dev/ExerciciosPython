cont = 0

núm = (int(input('Digite o primeiro número: ')),
int(input('Digite o primeiro número: ')),
int(input('Digite o primeiro número: ')),
int(input('Digite o primeiro número: ')))

for c in núm:
    n = núm[c] % 2
    if n == 0:
        cont += 1

print(núm)         
print(f'O número 9 apareceu {núm.count(9)} vezes')
print(f'O valor 3 foi digitado na {núm.index(3) + 1} posição')
print(f'Você digitou {cont} número(s) pares')
