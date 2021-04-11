import random

#definindo funções
def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    enforcado = False
    acertou = False
    num_erros = 0
    palavra_exibicao = inicializa_letras_acertadas(palavra_secreta)

    print("Não temos dicas")
    print("A palavra secreta tem {} letras".format(len(palavra_secreta)))
    print(palavra_exibicao)

    while(not enforcado and not acertou):

        chute = input("Digite a letra que acha que a palavra secreta contém: ")
        chute = chute.strip()
        posicao = 0
        
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(letra.lower() == chute.lower()):
                    palavra_exibicao[posicao] = chute.upper()

                posicao = posicao + 1

            print("A palavra secreta ")
            print(palavra_exibicao)

            if(not "_" in palavra_exibicao):
                print("Você acertou!")
                print("A palavra secreta é {}".format(palavra_secreta))

                acertou = True
        else:
            num_erros = num_erros + 1

            print("A palavra secreta não possui a letra {}".format(chute))

            if(num_erros >= 5):
                print("Você foi enforcado")
                print("A palavra secreta era {}".format(palavra_secreta))
                enforcado = True
            else:
                print("Você ainda tem {} chances".format(5 - num_erros))

def imprime_mensagem_abertura():
    print("#############################")
    print("Bem vindo ao Jogo da Forca.")
    print("#############################")

def carrega_palavra_secreta():
    lista_paralavras = []
    with open("palavra.txt", "r") as arquivo:
        for linha in arquivo:
            lista_paralavras.append(linha.strip())

    index = random.randrange(0, len(lista_paralavras))

    palavra_secreta = lista_paralavras[index]

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    palavra_exibicao = ["_"] * len(palavra_secreta)
    return palavra_exibicao

#Executando códigos
if(__name__ == "__main__"): #Executa a função jogar caso esse arquivo seja rodado como arquivo principal.
    jogar()