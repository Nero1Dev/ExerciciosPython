frase = str(input('\033[1;41mDigite uma frase: ')).strip().upper()
palavra = frase.split()
junto = '' .join(palavra)
inverso = ''
inverso = junto[:: -1]
# for letra in range(len(junto) - 1, -1, -1):
    # inverso += junto[letra]
print('\033[1;41mA frase {} ao contrario é {}\033[0;0m'.format(junto, inverso))
if junto == inverso:
    print('\033[1;41mA frase é um PALÍNDROMO\033[0;0m')
else:
    print('\033[1;41mEssa frase não é um PALÍNDROMO\033[0;0m')
