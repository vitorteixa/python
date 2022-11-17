# Exercise 4 : Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada_teclado = input('Digite algo aqui:')
print('o tipo digitado é: ',type( entrada_teclado))

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
    print('possui minúsculas')
if entrada_teclado.isspace():
    print('Não tem só espaços')
