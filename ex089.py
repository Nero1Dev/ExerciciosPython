dados = list()

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    resp = str(input('Quer continuar? [S/N] '))
    média = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], média])

    if resp in 'Nn':
        break

print('-=' * 30)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(dados) -1:
        print(f'As notas de {dados[opc][0]} são {dados[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
