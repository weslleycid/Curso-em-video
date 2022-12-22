from random import randint
from time import sleep

print('*='*50)
print('Vamos jogar pedra, papel e tesoura?')
print('*='*50)
op = str('0')
while op != '1' and op != '2' and op != '3':
    op = str(input('[1] - pedra\n'
               '[2] - papel\n'
               '[3] - tesoura\n'
               'Escolha uma opção: '))

pc = randint(1,3)

print('pedra')
sleep(1)
print('Papel')
sleep(1)
print('tesoura!')
sleep(1)

if op == '1' and pc == 1:
    print('você: pedra X PC: pedra')
    print('Empate!!')
elif op == '2' and pc == 2:
    print('você: Papel X PC papel')
    print('Empate')
elif op == '3' and pc == 3:
    print('você: tesoura X PC tesoura')
    print('Empate!')
elif op == '1' and pc == 2:
    print('Você pedra X PC papel')
    print('Você perdeu!!')
elif op == '1' and pc == 3:
    print('Você pedra X PC tesoura')
    print('Você venceu!!')
elif op == '2' and pc == 1:
    print('Você papel X PC pedra')
    print('Você Venceu!!')
elif op == '2' and pc == 3:
    print('Você papel X PC tesoura')
    print('Você perdeu!!')
elif op == '3' and pc == 1:
    print('Você tesoura X PC pedra')
    print('Você perdeu!!')
elif op == '3' and pc == 2:
    print('Você tesoura X PC papel')
    print('Você venceu!!')