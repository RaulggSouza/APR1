#1. Gere uma lista de contendo os múltiplos de 3 entre 1 e 150.
i = 1
multiplos = []
while i <= 150:
    if i%3 == 0:
        multiplos.append(i)
    i += 1
print(multiplos)