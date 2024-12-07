def inicio():
    print('Você está em uma floresta escura: ')
    print('1. Seguir pelo caminho à esquerda.')
    print('2. Seguir pelo caminho à direita.')
    escolha = input('O que você faz? (1/2): ')
    print('=' * 50)

    if escolha == '1':
        caminho_esquerda()
    elif escolha == '2':
        caminho_direita()
    else:
        print('Escolha inválida! Escolha uma opção válida!')
        inicio()
    print('=' * 50)


def caminho_esquerda():
    print('Você encontra um cabana abandonada.')
    print('1. Entrar na cabana.')
    print('2. Continuar andando.')
    escolha = input('O que você faz? (1/2): ')
    print('=' * 50)

    if escolha == '1':
        entrar_cabana()
    elif escolha =='2':
        continuar_andando()
    else:
        print('Escolha inválida! Escolha uma opção válida!')
        caminho_esquerda()
    print('=' * 50)


def caminho_direita():
    print('Você encontra um rio.')
    print('1. Tentar atrevessar o rio.')
    print('2. Seguir o rio.')
    escolha = input('O que você faz? (1/2): ')
    print('=' * 50)

    if escolha == '1': 
        seguir_rio()
    elif escolha == '2':
        seguir_rio()
    else:
        print('Escolha inválida! Escolha uma opção válida!')
        caminho_direita()
    print('=' * 50)


def entrar_cabana():
    print('Dentro da cabana, você encontra um baú.')
    print('1. Abrir baú.')
    print('2. Sair da cabana.')
    escolha = input('O que você faz? (1/2): ')
    print('=' * 50)

    if escolha == '1':
        abrir_baú()
    elif escolha == '2':
        sair_da_cabana()
    else:
        print('Escolha inválida! Escolha uma opção válida!')
        entrar_cabana()
    print('=' * 50)


def continuar_andando():
    print('Você continua andando e encontra um urso.')
    print('1. Tentar fugir.')
    print('2. Enfrentar o urso.')
    escolha = input('O que você faz? (1/2): ')
    print('=' * 50)

    if escolha == '1':
        fugir_do_urso()
    elif escolha == '2':
        enfrentar_urso()
    else:
        print('Escolha inválida! Escolha uma opção válida!')
        continuar_andando()
    print('=' * 50)


def tentar_atravessar_rio():
    print('Você tenta atravessar o rio, mas a correnteza está muito forte.')
    print('Fim de jogo.')
    print('=' * 50)


def seguir_rio():
    print('Você segue o rio e encontra um vila.')
    print('1. Entrar na vila.')
    print('2. Continuar seguindo o rio.')
    escolha = input('O que você faz? (1/2): ')
    print('=' * 50)

    if escolha == '1':
        entrar_na_vila()
    elif escolha == '2':
        segui_rio_ate_cachoeira()
    else:
        print('Escolha inválida! Escolha uma opção válida!')
        seguir_rio()
    print('=' * 50)


def abrir_baú():
    print('Você encontrou um tesouro!')
    print('Parabéns, você venceu!')
    


def sair_da_cabana():
    print('Você sai da cabana e continua explorando a floresta.')
    


def fugir_do_urso():
    print('Você conseguiu fugir!')
    print('Mas a aventura continua.')
    


def enfrentar_urso():
    print('O urso era muito forte.')
    print('Fim de jogo.')    
    


def entrar_na_vila():
    print('Você encontra abrigo e segurança na vila.')
    print('Parabéns, você venceu!')
    


def segui_rio_ate_cachoeira():
    print('Você segue o rio e encontra uma cachoira.')
    print('fim do jogo')



inicio()





