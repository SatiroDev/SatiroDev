# r = float(input('Raio do circulo: '))
# area = 3.14159 * (r**2)
# print(area)

# dia = int(input('Quantidade de dias: '))
# mins = (dia * 24)*60
# print(mins)

preco = float(input('Preço do produto: '))
desc = int(input('Porcentagem do desconto: '))
prec_final = preco - (preco * (desc/100))
print(prec_final)