'''from random import randint

velocidade = randint(40,120)
print('O carro estava a {}km/h.' .format(velocidade))'''
velocidade = int(input('Digite a velocidade de um carro em km/h: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('VOCÊ FOI MULTADO!! Sua multa será de R${}.' .format(multa))


print('\nBom dia! Dirija com segurança!')