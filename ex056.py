from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
idade_velho = 0
cara_velho = ''
idades = 0
idade = 0
mulheres_novas = 0
pessoas = int(input('Quantas pessoas são para o teste: '))
for c in range(1, pessoas + 1):
    print('\033[1;31m========== {}ª Pessoa ==========\033[m'.format(c))
    nome = str(input('\033[1;33mNome: \033[m')).strip().title()
    idade = int(input('\033[1;33mIdade: \033[m'))
    sexo = str(input('''\033[1;33m[ M ] MASCULINO
[ F ] FEMININO
Digite sua sexualidade: \033[m''')).upper().strip()
    idades += idade
    if sexo == 'F':
        if idade <= 20:
            mulheres_novas += 1
    elif sexo == 'M':
        if c == 'M':
            idade_velho = idade
            cara_velho = nome
        if idade > idade_velho:
            idade_velho = idade
            cara_velho = nome
média = idades / pessoas
print('\033[1;41mA média de idade das {} pessoas é {}\033[m'.format(pessoas, média))
print('\033[1;41mDas {} pessoas listadas existem {} mulheres menores de 20 anos\033[m'.format(pessoas, mulheres_novas))
print('\033[1;41mO homem mais velho se chama {} e ele tem {} anos\033[m'.format(cara_velho, idade_velho))
input('Aperte qualquer tecla para limpar...')
clear()
