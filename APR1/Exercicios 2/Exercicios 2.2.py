#Faça um programa que receba a idade de um eleitor e informa se o 
#voto dele é facultativo (entre 16 e 17 anos), obrigatório (entre 18 a 65), 
#se ele está dispensado de votar (acima de 65) ou ainda se ele não tem idade para votar
idade = int(input("Digite a idade do eleitor "))
if idade < 16:
    print("Eleitor não tem idade para votar")
elif 16 <= idade < 18:
    print("Voto Facultativo")
elif 18 <= idade < 66:
    print("Voto Obrigatório")
else:
    print("Dispensado de votar")
