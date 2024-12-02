cont = 0
def soma(n1):
    return n1 + cont+1

def subtracao(n1):
    return n1 - cont-1

def multiplicacao(n1):
    return n1 * cont+2

def divisao(n1):
    if n1 == 0:
        return 'O número tem que ser diferente de 0!'
    else:
        return n1 / cont+1


print('Escolha uma operação: ')
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

escolha = input('Digite a operação que deseja (1/2/3/4): ')

try:
    n1 = int(input('Digite um número: '))

    if escolha == '1':
        while cont <= 9:
            resultado = soma(n1)
            cont += 1
            print(f'{n1} + {cont} = {resultado}')
    elif escolha == '2':
        while cont <= 9:
            resultado = subtracao(n1)
            cont += 1
            print(f'{n1} - {cont} = {resultado}')
    elif escolha == '3':
        while cont <= 9:
            resultado = multiplicacao(n1)
            cont += 1
            print(f'{n1} x {cont} = {resultado}')
        
            

    #cont += 1
except:
    print('ERRO')

