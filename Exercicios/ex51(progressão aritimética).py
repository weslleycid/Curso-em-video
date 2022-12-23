print('+*'*15)
print('PROGRESSÃO ARITIMÉTICA')
print('+*'*15)
p = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão: '))
print('{}'.format(p), end='-> ')
for c in range(0,9):
    p = p + r
    print('{}'.format(p),end='->')
print('Acabou!')