quantatul = int(input('Digite a quantidade atual:'))
quantmax = int(input('Digite a quantidade maxima:'))
quantmin = int(input('Digite a quantidade minima:'))

quantmedia = (quantmax + quantmin)/2

if quantatul >= quantmedia:
    print(f'{quantmedia}Não efetuar comprar')
else:
    print(f'{quantmedia}Efetuar comprar')