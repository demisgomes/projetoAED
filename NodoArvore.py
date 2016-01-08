from NodoNulo import NodoNulo

class NodoArvore:

    def __init__(self, dado):

        self.cor= "vermelho"
        self.pai=None
        self.esquerdo= NodoNulo(self)
        self.direito= NodoNulo(self)
        self.dado=dado

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
        self.dado=dado

    def setEsquerdo(self,dado):
        self.esquerdo=dado
        
    def setDireito(self,dado):
        self.direito=dado

    def setPai(self,dado):
        self.pai=dado
    
