notas = []
def adicionar_nota():
    nota = input('Digite a sua nota: ')
    notas.append(nota)
    print('Nota adicionada com sucesso!')

def exibir_notas():
    if notas:
        print('Suas notas: ')
        for i, nota in enumerate(notas, 1):
            print(f'{i}. {nota}')
    else:
        print('Nenhuma nota adicionada!')
def salvar_notas():
    with open('notas.txt', 'w') as arquivo:
        for nota in notas:
            arquivo.write(nota + "\n")
    print('Notas salvas no arquivo "notas.txt"\n')
def remover_notas():
    if notas:
        exibir_notas()
        remover = input('Qual nota deseja remover? ')
        if remover in notas:
            notas.remove(remover)
            print('Nota removida com sucesso!')
        else:
            print('Nota não encontrada!')
    else:
        print('Nenhuma nota para remover!')
def mostrar_menu():
    print('1. Adicionar notas.')
    print('2. Exibir notas.')
    print('3. Salvar notas')
    print('4. Remover nota.')
    print('5. Sair.')

while True:
    mostrar_menu()
    escolha = input('Escolha uma opção (1/2/3/4): ')
    if escolha == '1':
        adicionar_nota()
    elif escolha == '2':
        exibir_notas()
    elif escolha == '3':
        salvar_notas()
    elif escolha == '4':
        remover_notas()
    elif escolha  == '5':
        print('Saindo dos blocos de notas. Até logo!')
        break
    else:
        print('Opção inválida! Por favor selecione uma opção válida!')