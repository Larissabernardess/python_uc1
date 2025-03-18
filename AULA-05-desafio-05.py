idade =int(input ('Informe a sua idade: '))
renda = float(input('informe a sua renda: '))
nome_sujo =input('informe se seu nome está sujo: ')

if (idade  > 21) and (renda > 2000 ) and (nome_sujo =="n") :
    print('EMPRÉSTIMO APROVADO')

else :
    print ("Reprovado")
    
