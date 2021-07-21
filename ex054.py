from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for c in range(1, 8):    
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? : '.format(c)))
    maior = atual - nascimento
    if maior >= 21: 
        total_maior += 1
    else:
        total_menor += 1
print('Tiveram {} pessoas maiores de idade'.format(total_maior))
print('Tiveram {} pessoas menores de idade'.format(total_menor))
