nome = str(input('Digite seu nome completo: '))

print('Seu nome em letras maiúsculas é: ' .format(nome.upper()))
print('Seu nome em letras minúsculas é: ' .format(nome.lower()))
#print(len(nome.replace(' ', '')))
print('Seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras. ' .format(nome.split()[0], nome.find(' ')))