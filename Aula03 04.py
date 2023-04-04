#Aula 03/04 - Int/float if/else


#Atividade 01

idade = int(input('digite sua idade:'))
nova_idade = idade + 1
print (nova_idade)


#Atividade 02

num = float(input('Digite Um Numero:'))
if num > 10:
    print(f'{num} Valor maior que 10')
else:
    print(f'{num} Valor menor que 10')


#Atividade 03

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota_final = ((nota1 + nota2)/2)
if nota_final >= 6:
    print(f'{nota_final}Aprovado')
else:
    print(f'{nota_final}Reprovado')


#Atividade 04

num01 = int(input('digite um numero:'))
num02 = int(input('digite um numero'))
if num01 > num02:
    print(f'{num01}')
else:
    print(f'{num02}')


#Atividade 05

num01 = int(input('Digite um numero:'))
num02 = int(input('Digite um numero:'))
if num01 < num02:
    print (f'{num01},{num02}')
else:
    print (f'{num02},{num01}')

#Atividade 06

numconta = int(input('digite um numero da conta:'))
numsaldo = float(input('digite um numero o saldo:'))
numdebito = float(input('digite um numero o debito:'))
numcredito = float(input('digite um numero credito:'))

saldoatual = numsaldo - numdebito + numcredito
if saldoatual >= 0:
    print(f'{saldoatual} saldo Possitivo')
else:
    print(f'{saldoatual}Saldo negativo') 


#Atividade 07

quantatul = int(input('Digite a quantidade atual:'))
quantmax = int(input('Digite a quantidade maxima:'))
quantmin = int(input('Digite a quantidade minima:'))

quantmedia = (quantmax + quantmin)/2

if quantatul >= quantmedia:
    print(f'{quantmedia}Não efetuar comprar')
else:
    print(f'{quantmedia}Efetuar comprar')


#Atividade 08

numero = float(input('Digite um numero'))
resto = numero %2

if resto == 0:
    print('numero par')
else:
    print('numero impar')


#Ted4 Questão 01

Num01 = float(input('Digite um numero:'))

if Num01 >= 0:
    print('Positivo')

else:
    print('Negativo')

#Ted4 Questão 02

num02 = int(input('Digite o numeros de maças:'))

if num02 >= 12:
    print (num02 * 1.0)

else:
    print(num02 * 1.30)