#Faça um algoritmo que receba três valores A, B e C e verifica se eles podem ser os comprimentos dos 
#lados de um triângulo. Se forem, mostrar se é um triângulo equilátero, isósceles ou escaleno. 
#Considere que:
# Para ser triângulo: cada lado é menor que a soma dos outros dois lados.
# Triângulo equilátero: tem três lados iguais
# Triângulo isósceles: tem dois lados iguais e um diferente Triângulo escaleno: tem três lados diferentes
l1 = int(input("Digite o primeiro lado "))
l2 = int(input("Digite o segundo lado "))
l3 = int(input("Digite o terceiro lado "))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    if l1 == l2 and l2 == l3:
        print("Trinângulo Equilátero")
    elif l1 != l2 and l2 != l3:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isóceles")
else:
    print("Não é um triângulo")