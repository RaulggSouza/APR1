#Faça um programa que receba um número inteiro maior que 1,
#verifique se o número é primo ou não e mostre a mensagem de número primo ou de número não primo. 
#Obs: Um número éprimo quando é divisível apenas por 1 e por ele mesmo.
num = int(input("Digite um número inteiro "))
primo = 0
for i in range(num):
    if num%(i+1) == 0:
        primo += 1
if primo == 2:
    print("Número primo")
else:
    print("Número não primo")