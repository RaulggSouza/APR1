#Folhas de Avião
while True:
    c = int(input("Digite o número de competidores: "))
    p = int(input("Digite a quantidade de folhas papel especial comprada: "))
    f = int(input("Digite a quantidade de folhas papel especial para cada competidor: "))
    if c > 0 and c <= 1000 and p > 0 and p <= 1000 and f > 0 and f <= 1000:
          break
    else:
         print("Valores digitados inválidos, digite outros")
         continue
if c*f <= p:
    print("S")
else:
    print("N")
    