from time import sleep

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


print("COMPARANDO OS NÚMEROS...\n")
sleep(2)

maior = n1
menor = n2

if n1 > n2:
    n1 = maior
    print("O primeiro valor é o maior.")

elif n2 > n1:
    n2 = maior
    print("O segundo valor é o maior.")
else: 
    n1 == n2
    print("Não existe valor maior, os dois são iguais.")




