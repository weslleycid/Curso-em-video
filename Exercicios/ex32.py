from datetime import date
ano = int(input('Digite o ano desejado ou digite 0 para saber o anual atual:'))

r = ano%4
if ano==0:
    ano= date.today().year
    print('O ano atual é {} '.format(ano))
if ano % 4 == 0 and ano%100 !=0 or ano%400==0:
    print('\033[34:47mO ano {} é BISSEXTO\033[m'.format(ano))
else:
    print('\033[31:47mO ano {} NÃO é BISSEXTO\033[m'.format(ano))