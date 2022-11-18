#incompleto
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[0, 1, 0, 1, 0, 1, 0, 1],
                          [1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [2, 0, 2, 0, 2, 0, 2, 0],
                          [0, 2, 0, 2, 0, 2, 0, 2],
                          [2, 0, 2, 0, 2, 0, 2, 0]]
        self.vez = 1

    def printTabuleiro(self):
        print("\n\n\n\n")
        print("  0 1 2 3 4 5 6 7")
        for l in range(8):
            string = str(l)+" "
            for c in range(8):
                if self.tabuleiro[l][c] == 0:
                    string += "--"
                elif self.tabuleiro[l][c] == 1:
                    string += "XX"
                elif self.tabuleiro[l][c] == 2:
                    string += "OO"
            print(string)

    def jogada(self):
        possiveis = self.verificaPecaLivre()

        print("Possiveis Peças:")
        for jogada in range(len(possiveis)):
            print(jogada, "--->", possiveis[jogada])
        opcao = int(input("Escolha uma Peça: "))
        while opcao not in range(len(possiveis)):
            opcao = int(input("Escolha uma Peça válida: "))
        pecaEscolhida = possiveis[opcao]

        lugaresPossiveis = self.verificaMovimento(pecaEscolhida)

        print("Possiveis lugares:")
        for lugar in range(len(lugaresPossiveis)):
            print(lugar, "--->", lugaresPossiveis[lugar])
        opcao = int(input("Escolha um lugar: "))
        while opcao not in range(len(lugaresPossiveis)):
            opcao = int(input("Escolha um lugar válido: "))
        lugarEscolhido = lugaresPossiveis[opcao]

        self.verificaCaptura(pecaEscolhida, lugarEscolhido)

        self.tabuleiro[pecaEscolhida[0]][pecaEscolhida[1]] = 0
        self.tabuleiro[lugarEscolhido[0]][lugarEscolhido[1]] = self.vez

        if self.vez == 1:
            self.vez = 2
        else:
            self.vez = 1

    def verificaPecaLivre(self):
        possiveis = []
        for l in range(8):
            for c in range(8):
                if self.tabuleiro[l][c] == self.vez:
                    possiveis.append([l, c])
        verificadas = []
        for peca in possiveis:
            movimentos = self.verificaMovimento(peca)
            if len(movimentos) > 0:
                verificadas.append(peca)
        return verificadas

    def verificaMovimento(self, peca):
        movimentos = []
        if self.vez == 1:
            if peca[1]-1 >= 0:
                if self.tabuleiro[peca[0]+1][peca[1]-1] == 0:
                    movimentos.append([peca[0]+1, peca[1]-1])

                elif self.tabuleiro[peca[0]+1][peca[1]-1] == 2 and peca[0]+2 <= 7 and peca[1]-2 >= 0:
                    if self.tabuleiro[peca[0]+2][peca[1]-2] == 0:
                        movimentos.append([peca[0]+2, peca[1]-2])

            if peca[1]+1 <= 7:
                if self.tabuleiro[peca[0]+1][peca[1]+1] == 0:
                    movimentos.append([peca[0]+1, peca[1]+1])

                elif self.tabuleiro[peca[0]+1][peca[1]+1] == 2 and peca[0]+2 <= 7 and peca[1]+2 <= 7:
                    if self.tabuleiro[peca[0]+2][peca[1]+2] == 0:
                        movimentos.append([peca[0]+2, peca[1]+2])
        else:
            if peca[1]-1 >= 0:
                if self.tabuleiro[peca[0]-1][peca[1]-1] == 0:
                    movimentos.append([peca[0]-1, peca[1]-1])

                elif self.tabuleiro[peca[0]-1][peca[1]-1] == 1 and peca[0]-2 >= 0 and peca[1]-2 >= 0:
                    if self.tabuleiro[peca[0]-2][peca[1]-2] == 0:
                        movimentos.append([peca[0]-2, peca[1]-2])

            if peca[1]+1 <= 7:
                if self.tabuleiro[peca[0]-1][peca[1]+1] == 0:
                    movimentos.append([peca[0]-1, peca[1]+1])

                elif self.tabuleiro[peca[0]-1][peca[1]+1] == 1 and peca[0]-2 >= 0 and peca[1]+2 <= 7:
                    if self.tabuleiro[peca[0]-2][peca[1]+2] == 0:
                        movimentos.append([peca[0]-2, peca[1]+2])

        return movimentos

    def verificaCaptura(self,antigoLugar,novoLugar):
        if antigoLugar[0] - novoLugar[0] == 2:
            if antigoLugar[1] - novoLugar[1] == 2:
                self.tabuleiro[antigoLugar[0]-1][antigoLugar[1]-1] = 0
            else:
                self.tabuleiro[antigoLugar[0]-1][antigoLugar[1]+1] = 0
        elif antigoLugar[0] - novoLugar[0] == -2:
            if antigoLugar[1] - novoLugar[1] == 2:
                self.tabuleiro[antigoLugar[0]+1][antigoLugar[1]-1] = 0
            else:
                self.tabuleiro[antigoLugar[0]+1][antigoLugar[1]+1] = 0


def main():
    tabuleiro = Tabuleiro()
    while True:
        tabuleiro.printTabuleiro()
        tabuleiro.jogada()


main()
