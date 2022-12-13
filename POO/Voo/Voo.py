import datetime

class Voo:
    def __init__(self, num, data):
        self.num = num
        self.data = data
        self.lugares = []
        for i in range(200):
            self.lugares.append(0)

    def ocupa (self, lugar):
        if self.lugares[lugar-1] == 0:
            self.lugares[lugar-1] = 1
            return True
        return False

    def verifica (self, lugar):
        if self.lugares[lugar-1] == 0:
            return True
        return False

    def proximoLivre (self):
        for i in range(200):
            if self.lugares[i] == 0:
                return i+1

    def vagas (self):
        contador=0
        for i in range (200):
            if self.lugares[i] == 0:
                contador += 1
        return contador

    def getVoo (self):
        return self.num

    def getData (self):
        return self.data

    def __eq__ (self, outro):
        if isinstance(outro, Voo):
            if self.num == outro.num and self.data == outro.data:
                return True
        return False

    def __str__ (self):
        return f'Número do voo: {self.num}\nData: {self.data}'


def main():
    aviao=Voo("123-4", datetime.datetime(2022, 9, 11))
    aviao2=Voo("234-5", datetime.datetime(2022, 7, 20))
    print(aviao.ocupa(1))
    print(aviao.verifica(69))
    print(aviao2.verifica(69))
    print(aviao)
    print(aviao==aviao2)
    print(aviao.getData())
    print(aviao.getVoo())
    print(aviao.proximoLivre())
    print(aviao.vagas())

main()

    
    

    


    