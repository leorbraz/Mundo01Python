n = float(input('Quanto você tem de dinheiro em reais: '))
conversao = n / 3.27

print('Com R${}, pode-se comprar US${:.2f}.' .format(n, conversao))