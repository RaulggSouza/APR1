#1. Elabore um programa que efetue a soma de todos os números ímpares que são
#múltiplos de 3 e que se encontram no intervalo de 1 a 500.
soma = 0
for i in range(501):
    if i % 3 == 0 and i != 0 and i % 2 != 0:
        soma += i
        print(i)
print(f"A soma final desses números é: {soma}")
