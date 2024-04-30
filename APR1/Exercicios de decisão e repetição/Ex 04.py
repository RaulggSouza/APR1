#4. Faça um programa que gere aleatoriamente um número entre 0 e 100. Em seguida,
#o programa deve pedir que o usuário tente acertar qual o número gerado. Por
#exemplo, suponha que o programa gere o número 21 e o usuário tente adivinhálo digitando o número 50. 
#O programa deve, então, imprimir a mensagem:
#“Número incorreto, tente um valor menor”. O usuário digita, então, o número 10.
#Após a análise deste número, o programa deverá imprimir a mensagem “Número
#incorreto, tente um valor maior”. O processo deve continuar até que o usuário
#acerte o número gerado pelo programa. O programa deve finalizar informando o
#número de tentativas até o acerto.
#Obs: use a função randint() para gerar o número aleatoriamente. 
from random import randint
resultado = randint(0,101)
acertou = False
tentativas = 0
valido = False
while acertou == False:
    while valido == False:
        palpite = int(input("Digite um valor entre 0 e 100: "))
        if palpite >= 0 and palpite <= 100:
            valido = True
    if palpite < resultado:
        print("Número incorreto, tente um valor maior")
        tentativas += 1
        valido = False
    elif palpite > resultado:
        print("Número incorreto, tente um valor menor")
        tentativas += 1
        valido = False
    else:
        print(f"Parabéns! Você acertou o número! Você precisou de {tentativas} tentativas")
        acertou = True