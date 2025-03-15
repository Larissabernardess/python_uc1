frutas = ['maçã','banana','cereja']

for item in frutas:
    print(f'\t{item.upper()}')
    input('\n PRESSIONE ENTER !!!\n')

    contagem = (9,8,7,6,5,4,3,2,1,0)
    for item in contagem:
        print(f'{item}...')


for i in range(3):
    print(f'{i} - {frutas[i]}')
