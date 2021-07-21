maior_18 = mulheres_novas = homens = 0
while True:
    print('\033[36m=' * 17)
    print('CADASTRAR PESSOA')
    print('=' * 17, '\033[m')
    idade = int(input('\033[33mIdade: \033[m'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('\033[33mSexo: [F/M] \033[m')).strip().upper()[0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres_novas += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[31mCadastrar mais alguem? [S/N] \033[m')).strip().upper()[0]
    if continuar == 'N':
                break
print(f'\033[32m{maior_18} pessoas são maiores de 18 anos.\033[m')
print(f'\033[32m{homens} homens foram cadastrados no total.\033[m')
print(f'\033[32m{mulheres_novas} mulheres com ou menos de 20 anos foram cadastrados.\033[m')
