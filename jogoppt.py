import random
def jogo():
    while True:
        esc = ['pedra', 'papel', 'tesoura']
        j_maquina = random.choice(esc)
        usuario_escolha = input('Digite (pedra/papel/tesoura): ')
        if usuario_escolha in esc:
            print(f'Você escolheu {usuario_escolha} e a máquina {j_maquina}')
            if usuario_escolha == j_maquina:
                print(f'Empate! Máquina escolheu {j_maquina} e você {usuario_escolha}.')
            elif usuario_escolha == 'papel' and j_maquina == 'tesoura' or usuario_escolha == 'tesoura' and j_maquina == 'pedra' or usuario_escolha == 'pedra' and j_maquina == 'papel':
                print(f'A máquina ganhou! Ela escolheu {j_maquina} e você {usuario_escolha}.')
            else:
                print(f'Parabéns! Você ganhou! Você escolheu {usuario_escolha} e a máquina {j_maquina}')    
        else:
            print('Escolha entre "pedra", "papel" ou "tesoura"')
            continue
        jogar_novamente = input('Deseja jogar novamente? (sim/nao)')
        if jogar_novamente == 'sim':
            continue
        else:
            print('Obrigado por jogar! Até mais!')
            break
jogo()