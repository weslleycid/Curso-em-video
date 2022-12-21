from random import randint
print('*='*50)
print('Vamos jogar pedra, papel e tesoura?')
print('*='*50)

op = int(input('[1] - pedra\n'
               '[2] - papel\n'
               '[3] - tesoura\n'
               'Escolha uma opção: '))

pc = randint(1,3)

if op == 1 and pc == 1:
    print('você: pedra x PC: pedra')
    print('Empate!!')
if op == 2:
    print('você: Papel')
if op == 3:
    print('você: tesoura')

