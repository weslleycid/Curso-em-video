import math
from math import trunc
num1 = float(input('Digite um  numero: '))
print('O numero digitado foi {} sua parte inteira é {} '.format(num1, math.trunc(num1)))
# Forma de mostrar a parte inteira de um numero usando uma biblioteca

num2 = float(input('Digite um segundo valor: '))
print('O valor digitado foi: {} a sua parte inteira é {}'.format(num2, int(num2)))
''' Forma de mostrar apenas a parte inteira de um numero sem usar uma biblioteca'''
int1 = trunc(num1) # Usando o modulo especifico importado de uma biblioteca
int2 = trunc(num2)

print('A soma das duas partes inteiras {} e {} é igual a {}'.format(int1, int2, int1+int2))