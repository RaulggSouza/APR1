a, c = 0, 0
viagens = 0
continuar = False
while continuar != True:
    contador = 0
    if c >= 2 and c <= 100:
        contador += 1
    else:
       print("Digite um número entre 2 e 100")
       c = int(input("Digite um número máximo de pessoas na cabine: "))
    if a >= 1 and a <= 1000:
        contador += 1
    else:
        print("Digite um número entre 1 e 1000")
        a = int(input("Digite o número de alunos da turma: "))
    if contador == 2:
        continuar = True
while a > 0:
    a -= c-1
    viagens += 1
print(viagens)