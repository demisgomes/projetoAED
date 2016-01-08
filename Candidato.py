class Candidato:
    def __init__(self,nome, numero):
        self.__numero = numero
        self.__nome = nome
        self.__votos = 0

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome

    def getNumero(self):
        return self.__numero

    def setNumero(self,numero):
        self.__numero = numero

    def getVotos(self):
        return self.__votos

    def setVotos(self):
        self.__votos +=1

    def LimparVotos(self):
        self.__votos = 0
