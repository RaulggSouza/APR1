#6) Faça uma função que receba quatro valores, referentes as notas que um aluno obteve nos bimestres. 
#A função deve retornar Verdadeiro se o aluno foi aprovado e Falso caso contrário. 

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

def passou(notas):
    media = 0
    for nota in notas:
        media += float(nota)
    media /= len(notas)
    if media >= 6:
        return True
    else:
        return False

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
    aprovado = passou(notas)
    if aprovado:
        print("Parabéns você foi aprovado!")
    else:
        print("Você foi reprovado")
main()