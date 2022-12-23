import datetime
anoNasceu = int(input('Digite o ano em que você nasceu: '))
aliste = 18
anoAtual = datetime.date.today().year
idade = anoAtual - anoNasceu
sexo = int(input('Digite seu sexo:\n'
                 '[1] Masculino\n'
                 '[2] Feminino: '))
if sexo == 1:
    if idade>aliste:
        prazo = idade - aliste

        print('Você tem {} anos, deveria ter se alistado {} anos atrás.'.format(idade, prazo))
        print('Seu alistamento foi em {}'.format(anoAtual - prazo))

    elif idade < aliste:
        faltante = aliste - idade

        print('Você tem {} anos deverá se alistar em: {}\n'
              'exatamente daqui a {} anos'.format(idade, anoAtual + faltante, faltante ))
    else:
        print('Você tem {} anos em {}. Aliste-se IMEDIATAMENTE!'.format(idade, anoAtual))
elif sexo == 2:
        print('Você não precisa se alistar!!\n'
          'O alistamento Obrigatório é somente para Brasileiros do sexo masculino')
else:
    print('Opção sexual invalida \n'
          'Escolha corretamente')
