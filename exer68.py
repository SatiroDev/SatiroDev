from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    
    esc_computador = randint(1,10)
    valor = int(input('Diga um valor: '))
    esc = input('Par ou Ímpar? [P/I] ').upper().strip()
    soma = esc_computador + valor
    result = soma % 2
    if result == 0:
        resp = 'PAR'
    if result == 1:
        resp = 'ÍMPAR'
    print('-' * 30 )
    print(f'Você jogou {valor} e o cumputador {esc_computador}. Total de {soma} DEU {resp}')
    print('-' * 30)
    
    if esc == 'P' and result == 0:
        print('Você GANHOU!')
        print('Vamos tentar novamente...')
        cont += 1
    elif esc == 'I' and result == 1:
        print('Você GANHOU!')
        print('Vamos tentar novamente...')
        cont += 1
    elif esc == 'P' and result == 1:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        print('=-' * 15)
        break
        
    elif esc == 'I' and result == 0:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        print('=-' * 15)
        break
    else:
        print('Erro')
    print('=-' * 15)