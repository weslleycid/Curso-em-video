soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3==0:
        soma = soma + n
        cont = cont + 1




print('O laço se repetiu {} vezes'.format(cont))
print('A soma de todos os multiplos de 3 é igual a {}'.format(soma))
