from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10),
randint(0, 10), randint(0, 10))

print(f'Sorteei os valores: ', end=' ')

for c in n:
    print(f'{c}', end=' ')

print(f'\nO maior número foi {max(n)}')
print(f'O menor número foi {min(n)}')
