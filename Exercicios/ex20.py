import random
from random import shuffle
A1 = input('Digite o nome do primeiro aluno: ')
A2 = input('Digite o nome do segundo aluno: ')
A3 = input('Digite o nome do terceiro aluno: ')
A4 = input('Digite o nome do quarto aluno: ')

lista = [A1,A2,A3,A4]
random.shuffle(lista)
print('A ordem sorteada para apresentação dos trabalhos foi: {} '.format(lista))