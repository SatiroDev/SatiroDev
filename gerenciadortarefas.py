def menu():
    print('=' * 45)
    print('ATENÇÃO! Se é sua primeira vez aqui no gerenciador, ele so funcionara quando você colocar suas tarefas!!')
    print('=' * 45)
    print('O que você deseja fazer? ')
    print('1. Adicionar tarefa')
    print('2. Ver tarefas')
    print('3. Remover tarefa')
    print('4. Sair')
    print('=' * 45)

def gerenciador_de_tarefas():
    tarefas = []
    while True:
        menu()
        escolha = input('Escolha: ')
        print('=' * 45)
        if escolha == '1':
            tarefa_add = input('Digite a tarefa: ')
            tarefas.append(tarefa_add)
            print('Tarefa adicionada!')
            print('=' * 45)
        elif escolha == '2':
            if tarefas:
                print('Suas tarefas: ')
                for indice, tarefa in enumerate(tarefas, 1):
                    print(indice, tarefa)
                    
            else:
                print('Nenhuma tarefa no momento.')
                print('=' * 45)
        elif escolha == '3':
            if tarefas:
                print('Suas tarefas: ')
                for indice, tarefa in enumerate(tarefas, 1):
                    print(indice, tarefa)
                    
                remover = input('Remover tarefa: ')
                if remover in tarefas:
                    tarefas.remove(remover)
                    print(f'Tarefa {remover} removida!')
                    print('=' * 45)
                else:
                    print(f'A tarefa "{remover}" não foi encontrada!')
                    
            else:
                print('Nenhuma tarefa para remover.')
                
        elif escolha == '4':
            print('Saindo do gerenciador. Até mais!')
            print('=' * 45)
            break
        else:
            print('Opção inválida! tente novamente!')
            
            
gerenciador_de_tarefas()
