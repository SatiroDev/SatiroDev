print('como o seu professor faz a sua media?')
um = print('3 provas, descarta a menor nota e faz a média = 1')
dois = print('3 provas, média é feita com essas três notas = 2')
tres = print('2 provas, média é feita comn essas duas provas = 3')
print('digite 1, 2, ou 3!!')
logica_professor = int(input('digite a logística: '))
if logica_professor == 1:
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
    if nota1 > 10 or nota2 > 10 or nota3 > 10:
        if nota1 > 10:
            print('nota maior que 10!! [error (nota1)]')
        elif nota2 > 10:
            print('nota maior que 10!! [error (nota2)]')
        else:
            print('nota maior que 10!! [error (nota3)]')
    else:
        notas = [nota1, nota2, nota3]
        notas.remove(min(notas))
        media = sum(notas) / 2
        media = media * 2
        median1 = 30 - media
        print(f'nota necessaria {median1}')
        necessaria1 = median1 / 3
        print(f'você precisará tirar duas notas de no mínimo {necessaria1:.2f} em duas das três provas da N2')
elif logica_professor == 2:
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
    if nota1 > 10 or nota2 > 10 or nota3 > 10:
        print('nota maior que 10!!')
    else:
        notas = [nota1, nota2, nota3]
        media = sum(notas) / 3
        media = media * 2
        median2 = 30 - media
        print(f'nota necessaria {median2}')
        necessaria2 = median2 / 3
        print(f'você precisará tirar três notas de no mínimo {necessaria2:.2f} em cada uma das provas da N2')
elif logica_professor == 3:
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    if nota1 > 10 or nota2 > 10:
        print('nota maior que 10!!')
    else:
        notas = [nota1 , nota2]
        media = sum(notas) / 2
        media = media * 2
        median1 = 30 - media
        print(f'nota necessaria {median1}')
        necessaria1 = median1 / 3
        print(f'você precisará tirar duas notas de no mínimo {necessaria1:.2f} em cada uma nas provas da N2')
else:
    print('ERRO!!!')