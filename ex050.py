soma_dos_numeros = 0
contador = 0
for par in range(1, 6+1):
    numeros_inteiros = int(input(f'Digite o {par} valor: '))
    if numeros_inteiros % 2 == 0:
        soma_dos_numeros += numeros_inteiros
        contador += 1
print(f'Você informou {contador} números PARES a soma é igual a {soma_dos_numeros} ') 
