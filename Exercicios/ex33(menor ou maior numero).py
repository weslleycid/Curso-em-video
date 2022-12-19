n1 = int(input('Digite o primero numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1>=n2 and n1>=n3:
    print('O maior numero é o primeiro: {}'.format(n1))
elif n2>=n1 and n2>=n3:
    print('O maior numero é o segundo: {}'.format(n2))
else:
    print('O maior numero é o terceiro: {}'.format(n3))


if n1<=n2 and n1<=n3:
    print('O menor numero é primeiro: {}'.format(n1))
elif n2<=n1 and n2<=n3:
    print('O menor numero é segundo: {}'.format(n2))
else:
    print('O menor numero é terceiro: {}'.format(n3))