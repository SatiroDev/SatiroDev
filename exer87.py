matriz = [[],
          [],
          []]

valores = []

soma = 0

for c in range(0,9):
    v = 0
    pos = 0
    valor = int(input(f'Digite um valor: '))
    valores.append(valor)
    
    if valor % 2 == 0:
        soma += valor
    v += 1
    if len(matriz[0]) <= 2:
        matriz[0].append(valor)
    elif len(matriz[1]) <= 2:
        matriz[1].append(valor)
    elif len(matriz[2]) <= 2:
        matriz[2].append(valor)

print('-='*30)
print(f'[  {matriz[0][0]}  ]',end='')
print(f'[  {matriz[0][1]}  ]',end='')
print(f'[  {matriz[0][2]}  ]',end='')
print()

print(f'[  {matriz[1][0]}  ]',end='')
print(f'[  {matriz[1][1]}  ]',end='')
print(f'[  {matriz[1][2]}  ]',end='')
print()

print(f'[  {matriz[2][0]}  ]',end='')
print(f'[  {matriz[2][1]}  ]',end='')
print(f'[  {matriz[2][2]}  ]',end='')
print()
somas = valores[2]+valores[5]+valores[8]
print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somas}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')