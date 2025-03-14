nome = input('informe o seu login :')
senha = input('informe a sua senha :')

if (len(nome)<3):
    print ('!! ERRO - Nome invalido !!')

elif (len(senha)<6):
    print('!! ERRO - Senha invalido !!')

elif(senha=='123456') or (senha=='senha'):
    print('!! ERRO - SenhaFraca!!')
else :
    print('[OK] Cadastro realizado com sucesso')