from math import pow
from math import sqrt
from math import hypot
A = float(input('Digite o cateto oposto: '))
B = float(input('Digite o cateto adjascente: '))
catetoA = (pow(A, 2))
catetoO = pow(B,2)
hipotenusa = sqrt(catetoA + catetoO)

print('A ipotenusa é {:.2f}'.format(hipotenusa))

A1 = float(input('digite o cateto Oposto: '))
B1 = float(input('Digite o cateto adjascente: '))
catetoA1 = A**2
catetoB1 = B**2
hipotenusa1 = (catetoA1+catetoB1)*(1/2)
print(hipotenusa1)

A2 = float(input('Dgite o cateto Oposto: '))
B2 = float(input('Digite o cateto Adjascente: '))
hipotenusa2 = hypot(A2 , B2)
print('O valor da hipótenusa é {:.2f}'.format(hipotenusa2))
