anoNasc = int(input("Digite seu ano de nascimento: "))

idade = 2023 - anoNasc
if idade > 18:
    tempo = idade - 18

else:
    tempo = 18 - idade

if idade < 18:
    print("Você ainda deverá se alistar ao serviço militar. Faltam {} anos para se alistar." .format(tempo))

elif idade == 18:
    print("Está na hora de você se alistar.")

else: 
    print("Já passou do tempo de alistamento. Já se passaram {} anos desde a data de se alistar." .format(tempo))




