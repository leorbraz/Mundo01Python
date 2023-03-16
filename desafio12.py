n = float(input('Digite o valor de um produto: R$'))
porcentagem = 5 / 100
desconto = n * porcentagem
precodesconto = n-desconto

print('Na liquidação, esse produto sairá por R${}.' .format(precodesconto))