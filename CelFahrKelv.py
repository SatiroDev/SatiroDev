def cels_para_fehr(celsius):
    fehr = celsius * 9/5 + 32
    return fehr
def cels_para_kelvin(celsius):
    kelv = celsius + 273.15
    return kelv
while True:
    try:
        celsius = float(input('Digite a temperatura em celcius: '))
        fehrenheit = cels_para_fehr(celsius)
        kelvin = cels_para_kelvin(celsius)
        print(f'{celsius}°C é igual a {fehrenheit}°F e {kelvin}K.')
        break
    except ValueError:
        print('Entrada inválida! Por favor, insira um número válido!')    