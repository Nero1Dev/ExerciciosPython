dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['média'] = float(input(f'Qual a média de {dados["nome"]}: '))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-=' * 20)
for k, v in dados.items():
    print(f' - {k} é igual a {v}')
    