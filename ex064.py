soma = 0
number = 0
cont = -1
while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    soma += number
    parar = number
    cont += 1
valor_final = soma - 999
print('Você digitou {} números ea soma entre eles é {}.'.format(cont, valor_final))
