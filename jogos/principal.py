#Importações necessárias
import adivinhacao
import forca

#Executando código
jogo_selecionado = int(input("Escolha um jogo: \n(1)Adivinhação (2)Forca \n"))

if(jogo_selecionado == 1):
    adivinhacao.jogar()
elif(jogo_selecionado == 2):
    forca.jogar()
else:
    print("Opção Inválida")