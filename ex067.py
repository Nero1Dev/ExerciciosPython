while True:
    n1 = int(input('\033[32mQuer ver a tabuada de qual valor? \033[m'))
    if n1 < 0:
        break
    print('-' * 35)
    for c in range(1, 11):
        print(f'\033[34m{n1} x {c} = {n1 * c}\033[m')
    print('-' * 35)
print('\033[31mPROGRAMA DE TABUADA ENCERRADO. Volte sempre!\033[m')
