senha = str(input("Crie uma senha de no mínimo 8 caractéres: "))

QtdCarac = len(senha)

if QtdCarac > 8 and QtdCarac < 16:


    

    print("Senha atende a todos os requisitos!")    
        input("Confirme a senha: ")
            print("Senha cadastrada com sucesso!")

else:
    print("Senha não atende aos requisitos, tente outra vez.")
  

