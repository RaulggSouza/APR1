#1. Em geometria analítica, dois vetores podem ser definidos como a=<a1,a2,a3> e
#b=<b1,b2,b3>. Escreva um programa que leia dois vetores a e b (duas listas) de
#três posições cada e efetue o produto escalar entre eles. O produto escalar é obtido
#por a*b = a1b1+a2b2+a3b3. De acordo com o exemplo dado abaixo, o calculo a ser
#efetuado será: 1x5+4x2+7x3 
a = []
b = []
prod = 0
for i in range(3):
    numA = int(input(f"Digite o {i+1}° número de A "))
    numB = int(input(f"Digite o {i+1}° número de B "))
    prod += numA*numB
    a.append(numA)
    b.append(numB)
print("O produto escalar entre A = ", end="")
for i in range(len(a)):
    print(a[i], end=" ")
print()
print("e B = ", end="")
for i in range(len(b)):
    print(b[i], end=" ")
print()
print(f"é {prod}")