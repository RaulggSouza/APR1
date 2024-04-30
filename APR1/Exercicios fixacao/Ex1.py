#Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:
# Se D ≤ 800, a cesta vale 1 ponto;
# Se 800 < D ≤ 1400, a cesta vale 2 pontos;
# Se 1400 < D ≤ 2000, a cesta vale 3 pontos.
#Restrição: 0 ≤ D ≤ 2000
#A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da distância D, você deve escrever um programa para
#calcular o número de pontos do lançamento. 
    
d = -1
while d < 0 or d > 2000:
    d = int(input("Digite a distância do robô: "))
if d <= 800:
    ponto = 1
elif d > 800 and d < 1400:
    ponto = 2
else:
    ponto = 3
print(f'Essa cesta vale {ponto}')