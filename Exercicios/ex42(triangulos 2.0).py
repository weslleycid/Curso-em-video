print('*&'*20)
print('  Analisador de triangulos')
print('*&'*20)

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if (r1 < r2) + r3 and (r2 < r1) + r3 and (r3 < r1) < r2:
    print('É possivel formar um triangulo')
    if r1 == r2 == r3:
        print('Este triangulo é um EQUILATERO')
    elif r1 == r2 != r3 or r1==r3 != r2 or r2==r3 != r1:
        print('Este triangulo é um ISÓCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Este triangulo é um ESCALENO')
else:
    print('Não é possível formar um triangulo')
