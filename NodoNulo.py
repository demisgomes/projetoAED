class NodoNulo:

    def __init__(self, pai):

        self.cor = "preto"
        self.pai = pai
        self.esquerdo = None
        self.direito = None
        self.dado = None


    def Cor(self):
        return self.cor

    def Info(self):
        return self.dado

    def Esquerdo(self):
        return self.esquerdo

    def Direito(self):
        return self.direito

    def Pai(self):
        return self.pai

    def setCor(self,cor):
        self.cor = cor

    def setDado(self,dado):
        self.dado = dado

    def setEsquerdo(self,dado):
        self.esquerdo = dado

    def setDireito(self,dado):
        self.direito = dado

    def setPai(self,dado):
        self.pai = dado
        
