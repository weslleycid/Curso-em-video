import random
from time import sleep
print('-'*20)
print('O jogo começa agora!!')
print('-'*20)

sorteado = random.randint(0,5)
print('*'*50)
palpite = int(input('Digite o seu palpite de um numero entre 0 e 5 : '))
print('*'*50)
print('PROCESSANDO...')
sleep(3)
if palpite==sorteado:
    print('Voce acertou!!')
else:
    print('Não foi dessa vez!!!')


