#PAR OU ÍMPAR
p = None
while True:
    p = int(input("Se Alice for par digite 0, se Bob for par digite 1: "))
    if p == 0 or p == 1:
        d_1 = int(input("Digite quantos dedos foram jogados por Alice: "))
        d_2 = int(input("Digite quantos dedos foram jogados por Bob: "))
        if d_1 >= 0 and d_1 <=5 and d_2 >= 0 and d_2 <= 5:
            break
    else: 
        continue
if (d_1+d_2) % 2 == 0:
    if p == 0:
        print("Alice Ganhou!")
    else:
        print("Bob Ganhou!")
else:
    if p == 0:
        print("Bob Ganhou!")
    else:
        print("Alice Ganhou!")