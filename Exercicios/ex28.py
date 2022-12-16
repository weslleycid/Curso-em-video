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
sleep(1)
if palpite==sorteado:
    print('\033[1:32:40mVoce acertou!!\033[m')
else:
    print('\033[1:31:40mNão foi dessa vez!!!\033[m')


