nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota_final = ((nota1 + nota2)/2)
if nota_final >= 6:
    print(f'{nota_final}Aprovado')
else:
    print(f'{nota_final}Reprovado')
