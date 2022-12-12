import math # importando a biblioteca
from math import ceil # Importando um modulo específico da biblioteca
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
soma = num1 + num2
raiz = math.sqrt(soma) # usando um dos modulos da biblioteca

print('A soma entre {} e {} é igual a {} \n A raiz quadrada dessa soma é {} '.format(num1, num2, soma, ceil(raiz))) # importando
# o modulo especifico ceil da bilbioteca não preciso declarar a biblioreca quando vou usar a função
