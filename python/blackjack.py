import random


#jogo = [{baralho}, {cartasDealer}, {cartasJog}, virouCarta]
#carta = (("J"), ("paus"))



def virou_jogo(jogo):
    return [jogo[0], jogo[1], jogo[2], True]

def printa_jogador(jogador, mao, mostrar_primeira):
    if mostrar_primeira == True:
        saida = (jogador + ": " + str(get_pontuacao(mao)) + " pontos\nCartas: " + printa_cartas(mao))
    else:
        mao_em_jogo = mao[1:]
        saida = jogador + ": " + str(get_pontuacao(mao_em_jogo)) + " pontos\nCartas: " +  "carta virada, " + printa_cartas(mao_em_jogo)

    return saida

def to_str(jogo):
    saida = ""
    saida += printa_jogador("dealer", jogo[1], jogo[3])
    
    saida += printa_jogador("\njogador 1", jogo[2], True)

    return saida

def printa_cartas(cartas):
    saida = ""
    for carta in cartas:
        saida += carta[0] + " de " + carta[1] + ", "
    return saida

def prepara_jogo():
    jogo = [novo_baralho(), [], [], False]
    jogo = jogada(jogo, 1)
    jogo = jogada(jogo, 1)
    jogo = jogada(jogo, 2)
    jogo = jogada(jogo, 2)

    return jogo

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

def jogada(jogo, jogador):
    novo_baralho, cartas_jog = puxar_carta(jogo[0], jogo[jogador])

    if jogador == 1:
        return [novo_baralho, cartas_jog, jogo[2], jogo[3]]
    else:
        return [novo_baralho, jogo[1], cartas_jog, jogo[3]]
def puxar_carta(baralho, cartasJog):
    carta = random.choice(baralho)   
    novo_baralho = [item for item in baralho if item != carta]
    novas_cartasJog = [item for item in cartasJog] + [carta]

    return (novo_baralho, novas_cartasJog)
    



def novo_baralho():
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    naipes = ["paus", "copas", "espada", "ouro"]

    cartas = []
    for i in naipes:
        for j in valores:
            cartas.append((j, i)) 
    return cartas



