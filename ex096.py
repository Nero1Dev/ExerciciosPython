def área(lar, com):
    print(f'A área de um terreno {lar}x{com} é de {lar * com}m².')


print(' Controle de terrenos')
print('-' * 22)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(lar=largura, com=comprimento)
