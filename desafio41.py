
nascimento = int(input("Digite o seu ano de nascimento: "))

idade = 2023 - nascimento  

if idade <= 9:
    print("\nVocê faz parte da categoria: MIRIM")

elif idade <= 14:
    print("\nVocê faz parte da categoria: INFANTIL")

elif idade <= 19:
    print("\nVocêfaz parte da categoria: JUNIOR")

elif idade <= 20:
    print("\nVocê faz parte da categoria: SÊNIOR") 

else: 
    print("\nVocê faz parte da categoria: MASTER")

