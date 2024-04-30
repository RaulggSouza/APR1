#2. Faça um programa que simule um jogo da loto. O computador deve gerar 5
#números aleatoriamente entre 50 possíveis (0 a 49), armazenando as dezenas
#sorteadas em um vetor (dez_sort) de 5 posições. Em seguida, o usuário deverá ler
#uma lista com 10 posições, representando a aposta (conforme o exemplo abaixo).
#O programa deve, então, verificar e imprimir uma mensagem mostrando quantos
#números o usuário acertou. De acordo com o exemplo abaixo o usuário acertou 4
#dezenas. 
import random
dez_sort = []
aposta = []
acertos = 0
for i in range(5):
    num = random.randrange(0, 50)
    if num not in dez_sort:
        dez_sort.append(num)
    else:
        num = random.randrange(0,50)
        dez_sort.append(num)
for i in range(10):
    aposta.append(int(input(f'Digite sua {i+1}ª aposta entre 1 e 49: ')))
for i in range(len(aposta)):
    if aposta[i] in dez_sort:
        acertos += 1
print(f'Você acertou {acertos} dezenas')