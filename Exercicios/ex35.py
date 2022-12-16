print('-='*20)
print('Analisador de triagulos')
print('-='*20)
r1 = float(input('Digite o valor da primerira reta: '))
r2 = float(input('Digite o valor da segunda reta:'))
r3 = float(input('Digite o valor da terceira reta: '))

if (r1+r2)<r3 and (r1+r3)<r2 and (r2+r3)<r3:
    print('É possível formar um triangulo com os valores fornecidos! ')
else:
    print('Não é possível formar um triangulo com os valores fornecidos.')