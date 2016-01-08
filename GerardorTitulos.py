from random import *
class GerarTitulos:

    def __init__(self):

        self.Titulos = open("TitulosValidos.txt",'w')
        
        for i in range(0,100):
            num_titulo=randint(188088880000,188088889999)#O numero do titulo varia entre 1880 8888 0000 e 1880 8888 9999
            self.Titulos.write(str(num_titulo)+"\n")

        self.Titulos.close()

    def getTitulos(self):
        num_titulos= open("TitulosValidos.txt",'r')
        num_titulos2=num_titulos.readlines()
        num_titulos.close()
        return num_titulos2
    
#Funcao adicionada em Alterar titulo:
    #adicionar valores aleatorios a arvore de Titulos           #
#--gerarTitulos=GerarTitulos()                                 #
#--arroz=gerarTitulos.getTitulos()                             #
#--for valor in range(0,len(arroz)):                           #
#--    print arroz[valor]
#--    a = NodoArvore(arroz[valor])
#--    ArvoreEleitores.InsereNodo(a)#
#-----------------------------------------------------------# 

