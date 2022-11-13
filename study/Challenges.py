# Desafio 1
from _ast import If

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
num2 = float((input()))
soma = num1 + num2
print('A soma é:{}'.format(soma))

# Desafio 4 com condicionais
entrada_teclado = input('Digite algo aqui:')

if entrada_teclado.isnumeric() is True:
    print('é numérico')
else:
    print('nao é numérico')
if entrada_teclado.isalnum():
    print('é alfanumerico')
else:
    print('nao é alfanumerico')
if entrada_teclado.isupper():
    print('Somente maiúsculas')
else:
    print('possui minusculas')
