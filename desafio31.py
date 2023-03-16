distancia = float(input('Digite a distância em km de sua viagem: '))
print('Você está prestes a começar uma viagem de {}km.' .format(distancia))
preço1 = distancia * 0.50
preço2 = distancia * 0.45

if distancia <= 200:
    print('O preço por cada km será de R$0.50, e o valor total da viagem será de R${}' .format(preço1))

else:
    print('O preço por cada km será de R$0.45 e o valor total da viagem será de R${:.2f}' .format(preço2))