n1 = float(input("Primeira nota: "))    
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2
print(media)

if media < 5:
    print("REPROVADO!")

elif media <= 6.9:
    print("RECUPERAÇÃO!")

else:
    print("APROVADO!")
