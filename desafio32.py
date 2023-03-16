from calendar import isleap

ano = int(input('Digite o ano que deseja verificar se é bissexto: '))

if isleap(ano):
    print('É bissexto.')

else:
    print('Não é bissexto.')