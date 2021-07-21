from random import randint
print('\033[31mJogo da adivinhação')
print('Sou seu computador... E pensei em um número entre 0 e 50')
print('Sera que você consegue acertar?\033[31m')
adiversario = randint(0, 50)
acertou  = False
cont = 0
while not acertou:
    cont += 1
    escolha = int(input('Tente acertar o número: '))
    if escolha == adiversario:
        print('\033[1;33mParabens você acertou!\033[m')
        acertou =  True
    else:
        if escolha < adiversario:
            print('Mais... Tente denovo')
        if escolha > adiversario:
            print('Menos... Tente denovo')
print('\033[36mVocê ganhou com {} tentaiva o número era {} mesmo,  Parabéns\033[m'.format(cont, adiversario))
