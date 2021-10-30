def controle(lar, com):
    print(f'A área de um terreno {lar}x{com} é de {lar * com}m².')


print(' Controle de terrenos')
print('-' * 22)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

controle(lar=largura, com=comprimento)
