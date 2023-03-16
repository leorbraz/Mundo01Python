salario = float(input('Qual o valor do seu salário: R$'))
porcentagem = 15 / 100
aumento = salario * porcentagem
salarioNovo = salario + aumento

print('Seu salário aumentou em 15% e foi para R${:.2f}.' .format(salarioNovo))