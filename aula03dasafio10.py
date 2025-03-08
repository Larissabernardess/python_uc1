reais = input('Qual o valor em real que você possui?')
reais = float(reais)
dolar = input('Qual a cotação do dolar hoje?')
dolar = float(dolar)

valor = reais / dolar 

print(' Você possui R$ {valor:.2f} em dolar')