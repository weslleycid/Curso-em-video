numero = int(input('Digite um numero inteiro: '))
opçao = int(input('Esoclha uma opção: \n'
                  '[1] converter para binário\n'
                  '[2] converter para octal\n'
                  '[3] converter para hexadecimal\n'
                  'Sua opção: '))

if opçao == 1:
   binario = bin(numero)[2:]
   print('O {} em binario é igual a {}'.format(numero, binario))

elif opçao == 2:
    octal = oct(numero)[2:]
    print('O {} em octal é igual a {}'.format(numero, octal))
elif opçao == 3:
    hexa = hex(numero)[2:]
    print('O {} em hexadecimal é igual a {}'.format(numero, hexa))
else:
    print('Opção invalida')
