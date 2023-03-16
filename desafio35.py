from time import sleep

print('Analisando possíveis formações de triangulo: ')

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

print('PROCESSANDO...')
sleep(2)

cond1 = r1 + r2 > r3
cond2 = r2 + r3 > r1
cond3 = r1 + r3 > r2

if cond1 and cond2 and cond3:
    print('As retas informadas podem formar triângulo!')

else: 
    print('As retas informada não podem formar triângulo.')