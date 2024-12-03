def gorgeta_porcentagem(valor, porcentagem):
    total = (valor * porcentagem)/100
    v_gorjeta = valor + total
    return v_gorjeta

valor = float(input('Digite o valor total da conta: '))
porcentagem = float(input('Digite a porcentagem da gorjeta: '))
result = gorgeta_porcentagem(valor, porcentagem)

quant = int(input('Quantas pessoas vão dividir a conta? '))
divisao_pessoas = gorgeta_porcentagem(valor, porcentagem) / quant

print(f'Total com gorjeta: R$ {result}')

print(f'Cada pessoa deve pagar: R$ {divisao_pessoas}')