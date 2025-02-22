#imprimir divisores de um número

num = int(input('Número: '))
for c in range(1, num+1):
    if num % c == 0:
        print(f'-> {c}', end=' ')