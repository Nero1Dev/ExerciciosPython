number = int(input('\033[1;31mDigite o primeiro valor: \033[0;0m'))
conclusão = 0
for primo in range(1, number + 1):
    if number % primo == 0:
        print('\033[1;33m{}\033[0;0m'.format(primo), end= ' ')
        conclusão += 1
    else:
        print('\033[1;34m{}\033[0;0m'.format(primo), end= ' ')
print('\n\033[1;31mO número {} é divisível {} vezes'.format(number, conclusão))
if conclusão == 2:
    print('Então ele é PRIMO')
else:
    print('Então ele não é PRIMO\033[0;0m')
