# Desafio 1
nome = input('Qual é o seu nome? ')
print('Seja bem vindo,', nome, ' é um prazer ter você aqui!')

# Desafio 2

dia = input('Dia do nascimento? ')
mes = input('Mês do nascimento? ')
ano = input('Ano do nascimento? ')

print('Olá', nome, 'a sua data de nascimento é', dia, '/', mes, '/', ano)

# Desafio 3
print('Digite 2 números que serão somados.')
num1 = int(input())
num2 = int((input()))
soma = num1 + num2
print('A soma é:{}'.format(soma))

# validações alfa numerico/ maiuscula

print(nome.isalpha())
print(nome.isalnum())
print(nome.isupper())

