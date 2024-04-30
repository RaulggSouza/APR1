#Crie um algoritmo para resolver equações do 2º grau.
#Considere: ax² + bx + c = 0 (a deve ser diferente de 0)
#delta = b2 - 4 * a * c
#Caso: delta < 0, não existe raiz real
#delta = 0, existe uma raiz real: x = (-b) / (2 * a)
#delta > 0, existem duas raízes reais:
#x1 = (- b + raiz quadrada de delta) / (2 * a)
#x2 = (- b - raiz quadrada de delta) / (2 * a)
print("Calculo de equação do segundo grau")
a = float(input("Digite o valor de a da equação "))
b = float(input("Digite o valor de b da equação "))
c = float(input("Digite o valor de c da equação "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Não existe raiz real")
elif delta == 0:
    x = (-b) / (2 * a)
    print(f'A raiz da equação é {x}')
else:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f'As raízes da equação são {x1} e {x2}')
