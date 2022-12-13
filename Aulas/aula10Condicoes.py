n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua media foi: {} '.format(m))

if m< 6:
    print('Voce foi reprovado')
elif m>6< 7:
    print('Você está de recuperação')
else:
    print('Você está reprovado')