expr = str(input('Digite uma expressão: '))
pilha = list()
for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta!')
else: 
    print('A sua expressão não esta correta!')
