n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é: {} \n o produto é: {} \n  a divisão é {:.2f}  \n Divisao inteira é: {}, A potência é: {}'.format(s,m,d,di,e), end=' >>> ') #end não quebra linha

print(2 * 3) #multiplicação
print(2 ** 3) #exponencial
print(2%3) #módulo
print(2 / 3) #divisao
print(2 // 3) #divisao inteira
print(2+3) #soma
print(2-3) #subtracao

#ordem de precedencia
# parenteses ()
# potencias **
# multi, divisao, div inteira, modulo -- geralmente o que vem primeiro *,/,//,%
# soma e subtração +,-
# -------
# Pratica
print('Resultado exercicio pratico')
print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2) #9²
