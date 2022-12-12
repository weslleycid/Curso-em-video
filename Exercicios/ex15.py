D = int(input('Alugou o carro por quantos dias? '))
kmRodado = float(input('Quantos KM rodados? '))
A = 60
KM = 0.15
R = (D*A)+ (kmRodado*KM)

print('O valor a pagar é R${:.2f}'.format(R))

