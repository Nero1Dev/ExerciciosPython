from time import sleep
print(
    '-=' * 20,
    ['Contagem regrssivaa para o estouro de fogos!'],
    '-=' * 20
)
start = int(input('''Deseja começar a contagem!
[ 1 ] = Sim
[ 2 ] = Não
= '''))
sleep(1)
if start == 1:
    for c in range( 10, -1, -1, ):
        sleep(1)
        print(c)
    sleep(0.7)
    print('Booooooooom!')  
