#Faça um programa em Python que leia um número X do usuário e escreva ele na
#tela no seguinte formato: “O número escolhido foi X”
b = input("Digite um número: ")
print("O número escolhido foi {}".format(b))
#Faça um programa em Python que leia do usuário dois números. Faça a
#multiplicação dos dois números e mostre o resultado.
num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))
print("A multiplicação desses dois número é {}".format(num1*num2))
#Faça um programa que leia do usuário um número e escreva o seu
#sucessor e o seu antecessor.
a = int(input("Escreva um número: "))
print("O sucessor do número {} é {} e o antecessor é {}".format(a,a+1,a-1))
#Faça um programa que leia 2 notas de um aluno, onde a primeira nota possui
#peso 6 e a segunda possui peso 4. Calcule a média ponderada do aluno baseada
#nos pesos e exiba.
nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))
print(f'A média ponderada das notas é: {(nota1*6+nota2*4)/10}')
#Faça um programa que receba dois inteiros x e y e calcule o valor de z,
#dado pela expressão a seguir:
y = int(input("Digite o primeiro número: "))
x = int(input("Digite o segundo número: "))
print((x**2+y**2)/(x-y)**2)
#Faça um programa que receba o salário de um funcionário, reajusta o
#salário em 25% e apresenta o valor do reajuste e o novo salário após o aumento.
sal = int(input("Digite o salário: "))
print(f'O reajuste foi de {sal*1,25}')
