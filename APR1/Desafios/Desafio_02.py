continuar = False
cores = []
for i in range(4):
    num = 0
    while continuar != True:
        if num >= 1 and num <= 9:
            continuar = True
        else:
           num = int(input(f"Digite o {i+1}° número inteiro entre 1 e 9: "))
    continuar = False
    cores.append(num)
if cores[0] == cores[2] or cores[1] == cores[3]:
    print("V")
else:
    print("F")