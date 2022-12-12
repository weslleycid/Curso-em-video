#Tipos primitivos
#Int = numeros Inteiros(sem casa depois da virgula)
#float = numeros com casas depois da virgula
#bool = recebe dois valores: true ou false (sempre usar a primeira letra Maiuscula(True))
#str  = string ou seja 'Palavras'

n1 = int(input('Digite um valor ')) #isso é uma conversão de string(que é gerado pelo input) para int
n2 = int(input('Digite o segundo valor '))
soma = n1+n2
print(type(n1))  # mostra o tipo da variavel
print(type(n2))  #mostra o tipo da variável
print('O resultado da soma entre ',n1,' e ',n2,' e',soma)
print('A soma entre {} e {} é {}'.format(n1, n2, soma)) #forma mais eficiente de colocar um print o ponto format da a possibilidade de inserção das variaveis dentro do {} no print


casa = input('Digite seu nome')

print('Este valor é {}, {}, {}, {}, {}, {}, {}, {}, {}, {},  {}, {}, {}, {}, {} '.format(
    type(casa),
    casa.isalnum(),
    casa.isalpha(),
    casa.isascii(),
    casa.isdigit(),
    casa.islower(),
    casa.isdecimal(),
    casa.isidentifier(),
    casa.isnumeric(),
    casa.isprintable(),
    casa.isspace(),
    casa.isascii(),
    casa.istitle(),
    casa.isupper(),
    casa.__init_subclass__()
)
      )