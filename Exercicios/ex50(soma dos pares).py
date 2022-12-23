soma = 0
cont = 0
for c in range(6):
    c = int(input('Digite o {} numero: '.format(c)))
    if c % 2 == 0:
        soma = soma + c
        cont += 1

        if cont == 1:
            print('Você digitou apenas um numero par e foi o {}'.format(soma))
        else:
            print('A soma dos {} valores pares que você digitou é {}'.format(cont, soma))
if cont == 0:
    print('Você não digitou numeros pares')
