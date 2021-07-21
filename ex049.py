from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
print('-=' * 25)
number = int(input('Digite o numero que deseja ver sua tabuada: '))
quantidade = int(input('Quantos divisores terá? '))
print('-=' * 25)
multiplicador = 0
for tabuada in range(1, quantidade+1):
    multiplicador += 1
    resultado = number * multiplicador
    print(f'{number} x {multiplicador} = {resultado}')  
print('-=' * 25)  
input('Deseja finalizar o script tecle enter...')
clear()
