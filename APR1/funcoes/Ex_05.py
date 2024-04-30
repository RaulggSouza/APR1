#5) Faça uma função que receba quatro valores reais (faça a consistência), referentes as notas que um aluno 
#obteve nos bimestres. A função deve retornar a média final desse aluno. Pesquise como arredondar a nota.

from math import ceil

def isReal(n):
    contador = 0
    numeros = ['0','1','2','3','4','5','6','7','8','9','-','.']
    for i in range(len(n)):
        for j in range(len(numeros)):
            if n[i] == numeros[j]:
                contador += 1
    if contador == len(n):
        return True
    else:
        return False

def media(notas):
    media = 0
    for nota in notas:
        media += float(nota)
    media /= len(notas)
    return ceil(media)

def main():
    notas = []
    i = 0
    while i < 4:
        nota = input(f"Digite a {i+1}ª nota: ")
        if isReal(nota):
            notas.append(nota)
            i += 1
        else:
            print("Número não real, insira outro valor")
    media_final = media(notas)
    print(f'Sua média final foi: {media_final}')
main()