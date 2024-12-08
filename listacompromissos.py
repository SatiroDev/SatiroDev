compromissos = []

def adicionar_compromissos():
    global compromissos
    data = input('Data do compromisso: ')
    hora = input('Horário do compromisso: ')
    descricao = input('Descrição do compromisso: ')
    add_compromisso = {'data': data, 'hora': hora, 'descricao': descricao}
    compromissos.append(add_compromisso)
    print(f'Compromisso adicionado com sucesso!')




def exibir_tarefas():
    global compromissos
    if compromissos:
        print('Seus compromissos:')
        for i, compromisso in enumerate(compromissos, 1):
            print(f"{i}. Data: {compromisso['data']}, Hora: {compromisso['hora']}, Descrição: {compromisso['descricao']}")
    else:
        print('Nenhum compromisso adicionado!')
    


def remover_compromisso():
    global compromissos
    if compromissos:
        exibir_tarefas()
        remover = int(input('Digite o número do compromisso que deseja remover? '))
        if 0 < remover <= len(compromissos):
            compromissos_removido = compromissos.pop(remover - 1)
            print(f'Compromisso {compromissos_removido["descricao"]} removido com sucesso!')
        else:
            print(f'Compromisso {remover} não encontrado!')
    else: 
        print('Nenhum compromisso para remover!')

def mostrar_menu():
    print('1. Adicionar tarefas')
    print('2. Exibir tarefas')
    print('3. Remover tarefas')
    print('4. Sair')


while True:
    mostrar_menu()
    escolha = input('Escolha uma opção (1/2/3/4): ')

    if escolha == '1':
        adicionar_compromissos()
    elif escolha == '2':
        exibir_tarefas()
    elif escolha == '3':
        remover_compromisso()
    elif escolha == '4':
        print('Saindo da Agenda de compromissos. Até mais!')
        break
    else:
        print('Entrada inválida! Por favor digite algo válido!')

