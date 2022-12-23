m = int(input('Digite um numero para ver sua tabuada: '))
print('*='*7)
print('Tabuada')
print('*='*7)
for n in range(11):
    t = m*n
    print('{} x {} = {}'.format(m, n, t))

