#3. Faça um programa que leia três notas de provas de uma turma de 50 alunos (3 notas para cada aluno). 
#Para cada aluno, o programa deve calcular a média ponderada como segue: Média = (nota1*2 + nota2*4 + nota3*3 ) / 10. 
#Além de mostrar a média de cada aluno, o programa deve mostrar uma mensagem
#"Aprovado", caso a média seja maior ou igual a 6,0, e uma mensagem
#"Reprovado", caso contrário. Ao final, o programa deve calcular e apresentar a média geral da turma.
alunos = 50
media_alunos = 0
for i in range(alunos):
    print(f'Digite as notas do {i+1}° aluno')
    n1 = float(input("Digite a 1° nota do aluno: "))
    n2 = float(input("Digite a 2° nota do aluno: "))
    n3 = float(input("Digite a 3° nota do aluno: "))
    media = (n1*2 + n2*4 + n3*3) / 10
    media_alunos += media
    if media >= 6.0:
        print("Parabéns você foi aprovado!")
    else:
        print("Que pena você foi reprovado.")
print(f'A média geral da turma foi: {media_alunos/alunos:.2f}')
