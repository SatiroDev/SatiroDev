# somar digitos de números até 99
soma = 0
num1 = int(input('número: '))
dezena = num1//10
soma += dezena
unidade = num1 % 10
soma += unidade
print(soma)