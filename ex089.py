temp = list()
dados = list()

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    resp = str(input('Quer continuar? [S/N] '))
    média = (nota1 + nota2) / 2
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(média)
    dados.append(temp[:])
    temp.clear()
    if resp in 'Nn':
        break
        
print(temp)
print(dados)
