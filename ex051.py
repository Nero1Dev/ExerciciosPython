# cabesalho
print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)

# variaveis
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão

# estrutura de repetição
for pa in range(termo, décimo, razão):
    print(f'{pa}', end=' → ')
print('ACABOU')
