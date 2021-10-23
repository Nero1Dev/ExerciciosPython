from datetime import date
dados = dict()
hj = date.today().year
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = hj - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - hj
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
