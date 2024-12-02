def calculo_imc(peso, altura):
    imc = peso/altura**2
    return imc
def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso!'
    elif 18.5 <= imc < 24.9:
        return 'Peso normal!'
    elif 24.9 <= imc < 29.9:
        return 'Sobrepeso!'
    elif 29.9 <= imc < 34.9:
        return 'Obesidade Grau I'
    elif 34.9 <= imc < 39.9:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau III ou Mórbida!'
print('='*5, 'Calculadora de IMC', '='*5)
try:
    peso = float(input('Digite seu peso (em kg): '))
    altura = float(input('Digite a sua altura (em metros): '))
    if peso <=0 or altura <= 0:
        print('Peso e altura devem ser maiores que 0!')
    else:
        imc = calculo_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f'Seu IMC é: {imc:.2f}')
        print(f'Classificação: {classificacao}')
except:
    print('Entrada inválida! Por favor, insara valores válidos!')