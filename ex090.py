dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['média'] = float(input(f'Qual a média de {dados["nome"]}: '))
if dados['média'] < 6:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Aprovado'
print('-=' * 20)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
    