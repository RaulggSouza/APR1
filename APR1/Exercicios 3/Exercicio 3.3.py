#Faça um programa para mostrar as tabuadas de todos os números de 1 a 10.
#For
for i in range(10):
    for j in range(10):
        print((i+1)*(j+1))
    print("---------------------------")
#While
print("Usando o While\n")
x = 1
while x <= 10:
    y = 1
    while y <= 10:
        print(y*x)
        y += 1
    x += 1
    print("---------------------------")