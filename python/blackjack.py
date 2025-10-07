import random


#jogo = [{baralho}, {cartasDealer}, {cartasJog}]
#carta = (("J"), ("paus"))




def get_pontuacao(cartas):
    contA = 0
    pontuacao = 0
    for carta in cartas:
        if carta[0] == "A":
            contA +=1
        else:
            pontuacao += valor_carta(carta)

    for i in range(contA):
        if pontuacao + 11 < 21:
            pontuacao += 11
        else: pontuacao += 1
    return pontuacao


def valor_carta(carta):
    if carta[0] in "2345678910":
        return int(carta[0])
    elif carta[0] in "JQK":
        return 10


def puxar_carta(baralho, cartasJog):
    carta = random.choice(baralho)   
    novo_baralho = {item for item in baralho if item != carta}
    novas_cartasJog = {item for item in cartasJog} + {carta}

    return (novo_baralho, novas_cartasJog)
    



def novo_baralho():
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    naipes = ["paus", "copas", "espada", "ouro"]

    cartas = set()
    for i in range(naipes):
        for j in range(valores):
            set.add((valores[i], naipes[i])) 
    return cartas



