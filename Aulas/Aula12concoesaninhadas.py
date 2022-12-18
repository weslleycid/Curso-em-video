# Existe a possibilidade de criar uma lista com


print('#'*25)
print('Boletim do ultimo bimestre')
print('#'*25)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua media final é {}'.format(m))
if m>= 6:
    print('\033[32m Você foi aprovado!\033[m')

elif m>=5 and m<=5.9:
    print('\033[33mVocê está de recuperação!!\033[m')
    n3 = float(input('Digite a nota da prova de recuperação: '))
    mf = (n1+n2+n3)/3
    print('Após a prova de recuperação sua nova media é {} '.format(mf))
    if mf >= 6:
        print('\033[32mVocê foi aprovado!\033[m')
    else:
        print('\033[31mVocê está reprovado!!\033[m')


else:
    print('\033[31mVocê está reprovado!!\033[m')