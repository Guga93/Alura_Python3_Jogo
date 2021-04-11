#Importações necessárias
import random

#Definindo Funções
def jogar():
    resposta = random.randrange(1, 21)
    total_de_rodadas = 20

    print("##################################")
    print("Bem vindo ao Jogo da Adivinhação.")
    print("##################################")

    dificuldade = int(input("Escolha a dificuldade: \n(1)Fácil (2)Moderado (3)Dificil \n"))

    if(dificuldade == 1):
        total_de_rodadas = 20
    elif(dificuldade == 2):
        total_de_rodadas = 10
    elif(dificuldade == 3):
        total_de_rodadas = 5
    else:
        print("Opção inválida.")
        return

    for tentativa in range(1, total_de_rodadas + 1):
        chute = int(input("Chute um número entre 1 a 20: "))

        if(chute == resposta):
            print("Você acertou.\nParabéns!!")
            break
        elif(chute > resposta):
            print("Errou. O número correto é menor que",chute,"\nEssa foi a tentativa ",tentativa,"de",total_de_rodadas)
        elif(chute < resposta):
            print("Errou. O número correto é maior que",chute,"\nEssa foi a tentativa ",tentativa,"de", total_de_rodadas)

#Executando códigos
if(__name__ == "__main__"): #Executa a função jogar caso esse arquivo seja rodado como arquivo principal.
    jogar()