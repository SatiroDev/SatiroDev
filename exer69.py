cont_18 = 0
masc = 0
mulher = 0
while True:
    idade = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').upper().strip()
    if idade > 18:
        cont_18 += 1
    if sex == 'M' or sex == 'F':
        
        if sex == 'M':
            masc += 1
        if sex == 'F' and idade < 20:
            mulher += 1
    else:
        while True:
            sex = input('Sexo [M/F]: ').upper().strip()
            if sex == 'M' or sex == 'F':
                break

    cont = input('Deseja continuar? [S/N] ').upper().strip()
    if cont == 'S' or cont == 'N':
        if cont == 'S':
            continue
        elif cont == 'N':
            print(f'Pessoas com mais de 18 anos: {cont_18}')
            print(f'Quantos HOMENS cadastrados: {masc}')
            print(f'MULHERES com menos de 20 anos: {mulher}')
            break
    else:
        cont = input('Deseja continuar? [S/N] ').upper().strip()
    
    
        