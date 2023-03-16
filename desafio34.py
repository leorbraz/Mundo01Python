salario = float(input('Qual o valor de seu salário: '))

if salario <= 1250.0:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 10 / 100)
    
print('Quem ganhava R${}, passa a ganhar R${} agora.' .format(salario, novo))

'''salario = float(input('Qual o valor de seu salário: '))
aumento10 = salario * 0.1
aumento15 = salario * 0.15

if salario > 1250.0:
    salario10 = aumento10 + salario
    print('Seu salário aumento 10%, agora você receberá R${}.' .format(salario10))

else:
    salario15 = aumento15 + salario
    print('Seu salário aumentou 15%, agora você receberá R${}.' .format(salario15))'''