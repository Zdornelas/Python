numconta = int(input('digite um numero da conta:'))
numsaldo = float(input('digite um numero o saldo:'))
numdebito = float(input('digite um numero o debito:'))
numcredito = float(input('digite um numero credito:'))

saldoatual = numsaldo - numdebito + numcredito
if saldoatual >= 0:
    print(f'{saldoatual} saldo Possitivo')
else:
    print(f'{saldoatual}Saldo negativo') 