print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro_termo
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{}'.format(termo), end= ' → ')
        c += 1
        termo += razão
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão foi finalizada com {} termos mostrados.'.format(total))
