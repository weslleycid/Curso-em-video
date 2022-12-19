from random import choice

aluno1 = input('Digite o nome do primeiro Aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
listaAlunos = [aluno1,aluno2,aluno3,aluno4]

print('O numero aluno sorteado foi: {} '.format(choice(listaAlunos)))
