import blackjack as bj

def jogadas():
    while True:
        yield input("hit or stand? ")

def main():
    jogo = bj.prepara_jogo()
    print(bj.to_str(jogo))
    for jogada in jogadas():
        if jogada == "hit" or jogada == "stand":

            if jogada == "hit":
                jogo = bj.jogada(jogo, 2)
                print(bj.to_str(jogo))
                if bj.get_pontuacao(jogo[2]) > 21:
                    print("voce perdeu")
                    break
            elif jogada == "stand":
                jogo = bj.virou_jogo(jogo)
                while bj.get_pontuacao(jogo[1]) <= 16:
                    jogo = bj.jogada(jogo, 1)
                    if bj.get_pontuacao(jogo[1]) > 21:
                        print(bj.to_str(jogo))
                        print("voce ganhou")
                        return

                if bj.get_pontuacao(jogo[1]) > bj.get_pontuacao(jogo[2]):
                    print(bj.to_str(jogo))
                    print("voce perdeu")
                    break

                else:
                    print(bj.to_str(jogo))
                    print("voce  ganhou")
                    break


main()
