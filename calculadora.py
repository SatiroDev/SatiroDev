def soma(n1, n2):
    return n1 + n2
def subtacao(n1, n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return('Erro na divisão')
    else:
        return n1 / n2

print('Escolha uma operação: ')
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

escolha_oper = input('Digite o número da operação (1/2/3/4): ')

while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        if escolha_oper == '1':
            resultado = soma(n1, n2)
            print(f'{n1} + {n2} = {resultado}')
        elif escolha_oper == '2':
            resultado = subtacao(n1, n2)
            print(f'{n1} - {n2} = {resultado}')
        elif escolha_oper == '3':
            resultado = multiplicacao(n1, n2)
            print(f'{n1} x {n2} = {resultado}')
        elif escolha_oper == '4':
            resultado = divisao(n1, n2)
            print(f'{n1} / {n2} = {resultado}')
        else:
            print('Operação inválida!')
        continuar = input('Deseja realizar outra operação? (sim/nao): ') 
        if continuar != 'sim':
            print('Obrigado por usar a calculadora! ') 
            break   
        else:
            escolha_oper = input('Digite o número da operação (1/2/3/4): ')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número válido!')
