import random

NAIPES = ["Paus", "Copas", "Espadas", "Ouros"]

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.naipe}"


class Baralho:
    def __init__(self):
        self.cartas = []
        self.lixeira = []
        for naipe in NAIPES:
            for valor in range(1, 14):
                self.cartas.append(Carta(naipe, valor))
        random.shuffle(self.cartas)

    def distribuir(self, jogadores):
        for jogador in jogadores:
            for i in range(9):
                jogador.mao.append(self.cartas[0])
                self.cartas.pop(0)


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.trios = 0

    def ver_mao(self):
        print(f"{self.nome} tem:")
        for carta in self.mao:
            print(carta)

    def verificaMao(self):
        #incompleto
        listaOrdenadaPorNumero = []
        for i in range(1,13):
            for carta in self.mao:
                if i == carta.valor:
                    listaOrdenadaPorNumero.append(carta)

        listaVerificada = []
        for i in range(1,len(listaOrdenadaPorNumero)):
            if i <= len(listaOrdenadaPorNumero)-3:
                if listaOrdenadaPorNumero[i].valor == listaOrdenadaPorNumero[i+1].valor == listaOrdenadaPorNumero[i+2].valor:
                    listaVerificada.append(listaOrdenadaPorNumero[i])
                    listaVerificada.append(listaOrdenadaPorNumero[i+1])
                    listaVerificada.append(listaOrdenadaPorNumero[i+2])
                    self.trios += 1
                    for carta in listaVerificada:
                        self.mao.remove(carta)
        listaOrdenadaPorNaipe = []
        for i in NAIPES:
            for carta in listaOrdenadaPorNumero:
                if i == carta.naipe:
                    listaOrdenadaPorNaipe.append(carta)
        for i in range(len(listaOrdenadaPorNaipe)):
            if i <= len(listaOrdenadaPorNaipe)-3:
                if (listaOrdenadaPorNaipe[i].naipe == listaOrdenadaPorNaipe[i+1].naipe == listaOrdenadaPorNaipe[i+2].naipe) and (listaOrdenadaPorNaipe[i].valor == listaOrdenadaPorNaipe[i+1].valor - 1 == listaOrdenadaPorNaipe[i+2].valor - 2):
                    listaVerificada.append(listaOrdenadaPorNaipe[i])
                    listaVerificada.append(listaOrdenadaPorNaipe[i+1])
                    listaVerificada.append(listaOrdenadaPorNaipe[i+2])
                    self.trios += 1
                    for carta in listaVerificada:
                        self.mao.remove(carta)
        self.mao = listaVerificada + self.mao
        if self.trios == 3:
            return True
        else:
            return False
        
class Pife:
    def __init__(self):
        self.jogadores = []
        self.turno = 0

    def criaJogadores(self, numJogadores):
        for i in range(1, numJogadores + 1):
            nome = input(f"Digite o nome do jogador {i}: ")
            self.jogadores.append(Jogador(nome))

    def tiraCarta(self, baralho):
        jogadorAtual = self.jogadores[self.turno]
        if jogadorAtual.verificaMao():
            print("VENCEDOR: ", jogadorAtual.nome)
            return True
        print("(º_º)  Jogador: ", jogadorAtual.nome, "\n\n \/ Cartas \/")
        for carta in jogadorAtual.mao:
            print(jogadorAtual.mao.index(carta), " --> ",
                  carta.valor, " <-> ", carta.naipe)
        if len(baralho.lixeira)>0:
            print("Carta da lixeira: ", baralho.lixeira[-1].valor, " <-> ",baralho.lixeira[-1].naipe)
            print("\n  (*~*) Escolha sua ação: \n  -> 1 - Pegar\n  -> 2 - Comprar do baralho\n")
        else:
            print("(ToT)  Lixeira vazia! \n  (*~*) Escolha sua ação:\n  -> 2 - Comprar do baralho\n")
        acao = int(input("  ---> "))
        while (acao != 1 and acao != 2):
            print(
                "(*_*) AÇÃO INVÁLIDA, digite novamente: \n  -> 1 - Descartar\n  -> 2 - Adicionar a mão\n")
            acao = int(input("  ---> "))
        if acao == 1:
            cartaTirada = baralho.lixeira[-1]
            baralho.lixeira.pop(-1)
        else:
            cartaTirada = baralho.cartas[0]
            baralho.cartas.pop(0)
        print("\n (+_+) Carta tirada: ", cartaTirada)
        print("\n  (*~*) Escolha sua ação: \n  -> 1 - Descartar\n  -> 2 - Adicionar a mão\n")
        acao = int(input("  ---> "))
        while (acao != 1 and acao != 2):
            print(
                "(*_*) AÇÃO INVÁLIDA, digite novamente: \n  -> 1 - Descartar\n  -> 2 - Adicionar a mão\n")
            acao = int(input("  ---> "))
        if acao == 1:
            baralho.lixeira.append(cartaTirada)
        elif acao == 2:
            troca = int(input(" Selecione uma carta da mão para trocar (0 a 8): "))
            jogadorAtual.mao[troca] = cartaTirada
        self.turno += 1
        if self.turno == len(self.jogadores):
            self.turno = 0
        return False


def main():
    pife = Pife()
    pife.criaJogadores(4)
    baralho = Baralho()
    baralho.distribuir(pife.jogadores)
    acabou = False
    while not acabou:
        acabou = pife.tiraCarta(baralho)
    print("FIM DE JOGO")
main()
