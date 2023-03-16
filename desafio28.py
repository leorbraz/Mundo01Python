from random import randint
from time import sleep

computador = randint(0,5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar ...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('\nPARABÉNS! Você me venceu!')

else:
    print('\nVOCÊ PERDEU! Pensei no número {} e não no número {}.\n' .format(computador, jogador))



'''import random

n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5

lista = [n1, n2, n3, n4, n5, n6]
sorteio = random.choice(lista)

nescolhido = int(input('Digite um número de 0 a 5: '))

if nescolhido == sorteio:
    print('Parabéns, você acertou!')

else:
    print('O computador venceu!') '''






