"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a:'.format(medida))
print(f'{km} km\n{hm} hm\n{dam} dam\n{dm:.0f} dm\n{cm:.0f} cm\n{mm:.0f} mm')
