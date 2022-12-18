print('+*'*20)
print('RESULTADO FINAL')
nota1 = float(input ('digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = float(nota1+nota2)/2
sexo = str('0')
while sexo != '1' and sexo !='2':
    sexo = str(input('Escolha seu sexo -> \n''[1] masculino \n [2] Feminino\n'
                 'Opção Sexual: '))

if media <=5 and sexo == 1:
    print('Foi reprovado!')

elif media > 5 and media < 7 and sexo ==1:
    print('Você ficou de recuperação!')
    nota3 = float(input('Digite a nota da prova de recuperação: '))
    mediaRec = (nota1+nota2+nota3)/3
    if mediaRec < 7:
        print('REPROVADO!!')
    else:
        print('APROVADO!! \n'
              'Parabéns!!')
elif media > 7 and sexo ==1:
    print('Você está aprovado!!')

elif media <=5 and sexo ==2:
    print('Você está reprovada!')
elif media > 5 and media <7 and sexo==2:
    print('Você está de recuperação!')
    nota3 = float(input('Digite a nota da prova de recuperação: '))
    mediaRec = (nota1+nota2+nota3)/3
    if mediaRec >= 7:
        print('Você está APROVADA!!\n'
              'Parabéns!!!')
    else:
        print('Você está REPROVADA!!')
else:
    print('Você está APROVADA!!')

