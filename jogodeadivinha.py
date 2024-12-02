import random
def jogo_adivinhacao():
    print('Bem vindo ao Jogo da Adivinhação!')
    num_secret = random.randint(1, 50)
    tentativas = 5
    print('Eu escolhi um número entre 1 e 50. Você tem 5 tentativas para adivinhas.')
    while tentativas > 0:
        try:
            chute = int(input(f'Você tem {tentativas} tentativas restantes. Qual é o seu palpite? '))
        except ValueError:
            print('Por favor, digite um número válido!')
            continue
        if chute == num_secret:
            print('Você adivinhou o número! Parabens!')
            break
        elif chute < num_secret:
            print('O número é maior!')
        else:
            print('O número é menor!')
        tentativas -= 1
    if tentativas == 0:
        print(f'Suas tentativas acabaram. O número secreto era {num_secret}.')
    print('Fim do jogo.')
jogo_adivinhacao()