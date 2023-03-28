print("Programa Empréstimo Bancário ")

valorcasa = float(input("Valor da casa? "))
salario = float(input("Salário do comprador: "))
qntdAnos = float(input("Em quantos anos será pago? "))

qntdMeses = qntdAnos * 12
mensalidade = valorcasa / qntdMeses
salario30 = salario * 30 / 100
 
if mensalidade > salario30:
    print("\nOs requisítos para o empréstimo não foram atendidos.")

else:
    print("\nTudo certo com seu empréstimo!")



