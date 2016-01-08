from NodoArvore import NodoArvore
from NodoNulo import NodoNulo


class Arvore:

    def __init__(self):
        self.RaizDaArvore=None

    def EhDireito(self,nodo):
        pai=nodo.Pai()
        if pai==None:
            return False
        elif pai.Direito()==nodo:
            return True
        else:
            return False

    def EhEsquerdo(self,nodo):
        pai=nodo.Pai()
        if pai==None:
            return False
        elif pai.Esquerdo()==nodo:
            return True
        else:
            return False

    def InsereNodo(self,nodo):
        if self.RaizDaArvore==None:
            self.RaizDaArvore=nodo
            nodo.setCor("preto")
        else:
            NodoAuxiliar=self.RaizDaArvore
            while NodoAuxiliar!=None:
                if nodo.Info() < NodoAuxiliar.Info():
                    if NodoAuxiliar.Esquerdo()!=None:
                        if NodoAuxiliar.Esquerdo().Info() == None:
                            nodo.setPai(NodoAuxiliar)
                            NodoAuxiliar.Esquerdo().setPai(None)
                            NodoAuxiliar.setEsquerdo(nodo)
                            NodoAuxiliar=None
                            nodo.setCor("vermelho")
                            self.RepararInsercao(nodo)
                        else:
                            NodoAuxiliar=NodoAuxiliar.Esquerdo()
                    else:
                            nodo.setPai(NodoAuxiliar)
                            NodoAuxiliar.setEsquerdo(nodo)
                            NodoAuxiliar=None
                            nodo.setCor("vermelho")
                            self.RepararInsercao(nodo)
                        
                elif nodo.Info() > NodoAuxiliar.Info():
                    if NodoAuxiliar.Direito()!=None:
                        if NodoAuxiliar.Direito().Info() == None:
                            nodo.setPai(NodoAuxiliar)
                            NodoAuxiliar.Direito().setPai(None)
                            NodoAuxiliar.setDireito(nodo)
                            NodoAuxiliar=None
                            nodo.setCor("vermelho")
                            self.RepararInsercao(nodo)
                        else:
                            NodoAuxiliar=NodoAuxiliar.Direito()
                    else:
                            nodo.setPai(NodoAuxiliar)
                            NodoAuxiliar.setDireito(nodo)
                            NodoAuxiliar=None
                            nodo.setCor("vermelho")
                            self.RepararInsercao(nodo)
                else:
                    print "\nNodo ja inserido!(Igual)\n"
                    break
        self.RaizDaArvore.setCor("preto")


    def DeletaNodo(self, nodo):
        if nodo.Direito().Info() == None and nodo.Esquerdo().Info() == None: # se o nodo a ser deletado n?o tiver filhos
            NodoPai = nodo.Pai() # capturo o pai dele.
            if NodoPai != None: # se ele tiver pai.
                if self.EhDireito(nodo): # vejo se ele ? direito.
                    NodoPai.setDireito(nodo.Direito()) # corto a liga??o do pai com ele.
                    nodo.setPai(None) # corto a liga??o dele com o pai.
                else: # se ele for filho esquerdo.
                    NodoPai.setEsquerdo(nodo.Esquerdo()) # corto a liga??o do pai dele com ele.
                    nodo.setPai(None) # corto a liga??o dele com o pai.
                NodoSubstituto=NodoNulo(NodoPai)
            else: # se ele n?o tiver pai (ou seja for raiz).
                self.RaizDaArvore = None # a raiz da ?rvore recebe None
                NodoSubstituto=NodoNulo(None)
        else:
            if (nodo.Direito().Info() == None and nodo.Esquerdo().Info() != None) or (nodo.Esquerdo().Info() == None and nodo.Direito().Info() != None): # se ele tiver somente um filho esquerdo ou um filho direito.
                if nodo.Esquerdo().Info() == None: # se o filho que ele tiver for o direito.
                    NodoFilho = nodo.Direito() # o nodo filho recebe o filho direito dele.
                    NodoPai = nodo.Pai() # o nodo pai recebe o pai dele.
                    if NodoPai != None: # se ele tiver pai.
                        if self.EhDireito(nodo): # e ele for filho direito.
                           NodoPai.setDireito(NodoFilho) # O filho direito dele vira filho direito do pai dele.
                           NodoFilho.setPai(NodoPai) # fazendo a rela??o do filho direito dele com o pai dele.
                           nodo.setPai(None) # corto a liga??o dele com o pai dele.
                           nodo.setDireito(None) # corto a liga??o dele com o filho direito dele.
                        else: # se ele for filho esquerdo.
                            NodoPai.setEsquerdo(NodoFilho) # O filho direito dele vira filho esquerdo do pai dele.
                            NodoFilho.setPai(NodoPai) # fazendo a rela??o do filho direito dele com o pai dele.
                            nodo.setPai(None) # corto a liga??o dele com o pai dele.
                            nodo.setDireito(None) # corto a liga??o com o filho direito dele.
                        NodoSubstituto=NodoFilho
                    else: # se ele n?o tiver pai (ou seja for raiz)
                        NodoFilho = nodo.Direito() # O nodo filho recebe o filho direito dele.
                        nodo.setDireito(None) # corto a liga??o dele com o filho direito.
                        self.RaizDaArvore = NodoFilho # transformo o filho direito dele na raiz da ?rvore.
                        NodoFilho.setPai(None) # corto a liga??o do filho direito dele com ele
                        NodoSubstituto=NodoFilho
                else: # se n?o
                    if nodo.Direito().Info() == None: # se o filho que ele tive for o esquerdo.
                        NodoFilho = nodo.Esquerdo() # o nodo filho recebe o filho esquerdo dele.
                        NodoPai = nodo.Pai() # o nodo pai recebe o pai dele.
                        if NodoPai != None: # se ele tiver pai.
                            if self.EhDireito(nodo): # e for filho direito.
                                NodoPai.setDireito(NodoFilho) # O seu filho esquerdo vira filho direito do seu pai
                                NodoFilho.setPai(NodoPai) # fazendo a rela??o do filho esquerdo com o pai
                                nodo.setPai(None) # corto a rela??o do nodo com o pai
                                nodo.setEsquerdo(None) # corto a rela??o do nodo com o filho esquerdo
                            else:
                                NodoPai.setEsquerdo(NodoFilho) #
                                NodoFilho.setPai(NodoPai)
                                nodo.setPai(None)
                                nodo.setEsquerdo(None)
                        else:
                            NodoFilho = nodo.Esquerdo()
                            nodo.setEsquerdo(None)
                            self.RaizDaArvore = NodoFilho
                            NodoFilho.setPai(None)
                NodoSubstituto=NodoFilho
            else:
                if nodo.Esquerdo().Info() != None and nodo.Direito().Info() != None:
                    NodoSucessor = self.Sucessor(nodo)
                    NodoPai = nodo.Pai()
                    NodoEsquerdo = nodo.Esquerdo()
                    NodoDireito = nodo.Direito()
                    #DELETANDO N? COM DOIS FILHOS
                    if NodoPai != None:
                        if self.EhDireito(nodo):
                            NodoPaiSucessor = NodoSucessor.Pai()
                            if nodo == NodoPaiSucessor:
                                nodo.setDireito(None)
                                nodo.setPai(None)
                                nodo.setEsquerdo(None)
                                NodoSucessor.setPai(NodoPai)
                                NodoSucessor.setEsquerdo(NodoEsquerdo)
                                NodoEsquerdo.setPai(NodoSucessor)
                                NodoPai.setDireito(NodoSucessor)
                            else:
                                nodo.setDireito(None)
                                nodo.setEsquerdo(None)
                                nodo.setPai(None)
                                NodoSucessor.setPai(NodoPai)
                                NodoPai.setDireito(NodoSucessor)
                                if NodoSucessor.Direito() != None:
                                    NodoFilhoSucessor = NodoSucessor.Direito()
                                    NodoFilhoSucessor.setPai(NodoPaiSucessor)
                                    NodoPaiSucessor.setEsquerdo(NodoFilhoSucessor)
                                    NodoSucessor.setDireito(NodoDireito)
                                    NodoSucessor.setEsquerdo(NodoEsquerdo)
                                    NodoEsquerdo.setPai(NodoSucessor)
                                    NodoDireito.setPai(NodoSucessor)
                                else:
                                    NodoPaiSucessor.setEsquerdo(None)
                                    NodoSucessor.setDireito(NodoDireito)
                                    NodoSucessor.setEsquerdo(NodoEsquerdo)
                                    NodoEsquerdo.setPai(NodoSucessor)
                                    NodoDireito.setPai(NodoSucessor)

                        else:
                                NodoPaiSucessor = NodoSucessor.Pai()
                                if nodo == NodoPaiSucessor:
                                    nodo.setDireito(None)
                                    nodo.setPai(None)
                                    nodo.setEsquerdo(None)
                                    NodoSucessor.setPai(NodoPai)
                                    NodoSucessor.setEsquerdo(NodoEsquerdo)
                                    NodoEsquerdo.setPai(NodoSucessor)
                                    NodoPai.setEsquerdo(NodoSucessor)
                                else:
                                    if NodoSucessor.Direito() != None:
                                        NodoPaiSucessor.setEsquerdo(NodoSucessor.Direito())#Mesma Coisa aqui. O NodoSucessor receber? como dado o seu filho direito
                                        NodoSucessor.Direito().setPai(NodoPaiSucessor)
                                    else:
                                        NodoPaiSucessor.setEsquerdo(NodoNulo(NodoPaiSucessor))
                                    NodoSucessor.setPai(NodoPai)
                                    NodoSucessor.setDireito(NodoDireito)
                                    NodoSucessor.setEsquerdo(NodoEsquerdo)
                                    NodoPai.setEsquerdo(NodoSucessor)
                                    NodoDireito.setPai(NodoSucessor)
                                    NodoEsquerdo.setPai(NodoSucessor)
                                    nodo.setPai(None)
                                    nodo.setEsquerdo(None)
                                    nodo.setDireito(None)

                    #DELETANDO A RAIZ COM DOIS FILHOS!
                    else:
                        NodoPaiSucessor = NodoSucessor.Pai()
                        if nodo == NodoPaiSucessor:
                            if self.EhDireito(NodoSucessor): # e ele for filho direito.
                               NodoSucessor.setEsquerdo(NodoEsquerdo) # fazendo a rela??o do filho direito dele com o pai dele.
                               NodoEsquerdo.setPai(NodoSucessor)
                               NodoSucessor.setPai(None) # corto a liga??o dele com o pai dele.
                               self.RaizDaArvore=NodoSucessor
                            else: # se ele for filho esquerdo.
                                NodoPaiSucessor.setDireito(None)
                                NodoSucessor.setPai(None) # corto a liga??o dele com o pai dele
                                NodoSucessor.setCor("preto")
                        else:
                            NodoSucessorDireito=NodoSucessor.Direito()
                            self.RaizDaArvore=NodoSucessor
                            NodoSucessor.setDireito(NodoPaiSucessor)
                            NodoSucessor.setPai(None)
                            NodoPaiSucessor.setPai(NodoSucessor)
                            NodoSucessor.setEsquerdo(NodoEsquerdo)
                            NodoEsquerdo.setPai(NodoSucessor)
                            if NodoSucessor.Direito()!=None:
                                NodoPaiSucessor.setEsquerdo(NodoSucessorDireito)
                            else:
                                NodoPaiSucessor.setEsquerdo(NodoNulo(NodoPaiSucessor))
                        nodo.setPai(None)
                        nodo.setDireito(None)
                        nodo.setEsquerdo(None)

                NodoSubstituto=NodoSucessor
                nodo.setCor("preto")
        if nodo.Cor()=="preto" and NodoSubstituto.Info()!=None:
            self.RepararDelecao(NodoSubstituto)



    def RepararInsercao (self,nodo):
        NodoPai = nodo.Pai()

        #se o pai for vermelho, o loop come?a, pois se o pai ? preto n?o temos o que fazer
        while (NodoPai!=None and NodoPai.Cor() == "vermelho"):
            if NodoPai !=None:
                if NodoPai.Pai() !=None:
                    NodoAvo = NodoPai.Pai()
                    #O nodo av? ? necess?rio para opera??es de rota??o
                    if self.EhEsquerdo(NodoPai):
                        Tio = NodoAvo.Direito()
                        if Tio==None:
                            Tio=NodoNulo(NodoAvo)
                        if Tio.Info() == None:
                            #Se o tio n?o existe, dizemos que a cor do nodo inserido ser? diferente da de seu pai
                            #Usamos o break pois caso o pai do nodo fosse preto, ele nunca sairia do loop
                            if NodoPai.Cor()=="preto":
                                nodo.setCor("vermelho")
                                break
                            else:
                              nodo.setCor("preto")
                              break
##                            NodoPai().setCor("preto")
##                            if NodoAvo!=self.RaizDaArvore:
##                                NodoAvo.setCor("vermelho")
##                            nodo=nodo.Pai()
##                            NodoPai=nodo.Pai()
##                            continue
                        else:
                         if Tio.Cor()=="vermelho":
                                NodoPai.setCor("preto")
                                Tio.setCor("preto")
                                NodoAvo.setCor("vermelho")
                                nodo=NodoAvo
                                NodoPai=nodo.Pai()

                                #Se a cor do tio for vermelho, trocamos a cor do av? para vermelho
                                #A cor do pai e do tio para preto
                                #E dizemos que o nodo agora ? o Nodo Av?,e continuamos o loop

                         else:
                                if self.EhDireito(nodo):
                                    nodo=NodoPai
                                    self.RotacionarAEsquerda(nodo)
                                    nodo.Pai().setCor("preto")
                                    NodoPai=nodo.Pai()
                                    NodoAvo=NodoPai.Pai()
                                    NodoAvo.setCor("vermelho")
                                    self.RotacionarADireita(nodo.Pai().Pai())

                                    #Caso o nodo ? filho esquerdo, dizemos que o nodo agora ? o NodoPai
                                    #Rotacionamos o novo nodo ? esquerda
                                    #O nodo pai, que pode ser diferente ap?s a rota??o, recebe a cor preta
                                    #E o nodo av? recebe a cor vermelha
                                    #Assim, rotacionamos o noso av? ? direita

                    else:
                        #O else ? a mesma coisa, apenas trocamos o esquerdo pelo direito

                        Tio = NodoAvo.Esquerdo()
                        if Tio==None:
                            Tio=NodoNulo(NodoAvo)
                        if Tio.Info() == None:
                            if NodoPai.Cor()=="preto":
                                nodo.setCor("vermelho")
                                break
                            else:
                               nodo.setCor("preto")
                               break
##                            NodoPai.setCor("preto")
##                            if NodoAvo!=self.RaizDaArvore:
##                                NodoAvo.setCor("vermelho")
##                            nodo=nodo.Pai()
##                            NodoPai=nodo.Pai()
##                            continue
                        else:
                            if Tio.Cor()=="vermelho":
                                NodoPai.setCor("preto")
                                Tio.setCor("preto")
                                NodoAvo.setCor("vermelho")
                                nodo=NodoAvo
                                NodoPai=nodo.Pai()

                            else:
                                if self.EhEsquerdo(nodo):
                                    nodo=NodoPai
                                    self.RotacionarADireita(nodo)
                                    nodo.Pai().setCor("preto")
                                    NodoAvo=nodo.Pai().Pai()
                                    NodoAvo.setCor("vermelho")
                                    self.RotacionarAEsquerda(nodo.Pai().Pai())
                else:
                    break
            else:
                #Caso o nodo seja a raiz da arvore, ele receber? a cor preta
                nodo.setCor("preto")



    def RepararDelecao(self,nodo):
        while nodo !=self.RaizDaArvore and nodo.Cor() == "preto":
            NodoPai = nodo.Pai()
            if self.EhEsquerdo(nodo):
                Irmao = NodoPai.Direito()
                
                if Irmao.Esquerdo()==None or Irmao.Direito()==None:
                    if Irmao.Esquerdo()==None:
                        Irmao.setEsquerdo(NodoNulo(Irmao))
                    if Irmao.Direito()==None:
                        Irmao.setDireito(NodoNulo(Irmao))
                if Irmao.Cor() =="vermelho":
                    print "Entrou no primeiro if\n"
                    Irmao.setCor("preto")
                    NodoPai.setCor("vermelho")
                    self.RotacionarAEsquerda(NodoPai)
                    Irmao = NodoPai.Direito()
                
                if Irmao.Esquerdo().Cor() == "preto" and Irmao.Direito().Cor()=="preto":
                        print "Entrou no segundo if\n"
                        Irmao.setCor("vermelho")
                        nodo = NodoPai
                elif Irmao.Direito().Cor() == "preto":
                        print "Entrou no elif\n"
                        Irmao.Esquerdo().setCor("vermelho")
                        self.RotacionarADireita(Irmao)
                        Irmao = NodoPai.Direito()
                        Irmao.setCor(NodoPai.Cor())
                        NodoPai.setCor("preto")
                        Irmao.Direito().setCor("preto")
                        self.RotacionarAEsquerda(NodoPai)
                        nodo = self.RaizDaArvore
                else:
                    break
            else:
                Irmao = NodoPai.Esquerdo()
                if Irmao.Esquerdo()==None or Irmao.Direito()==None:
                    if Irmao.Esquerdo()==None:
                        Irmao.setEsquerdo(NodoNulo(Irmao))
                    if Irmao.Direito()==None:
                        Irmao.setDireito(NodoNulo(Irmao))
                        
                if Irmao.Cor()  == "vermelho":
                    Irmao.setCor("preto")
                    NodoPai.setCor("vermelho")
                    self.RotacionarADireita(NodoPai)
                    Irmao = NodoPai.Esquerdo()
                if Irmao.Esquerdo().Cor() == "preto" and Irmao.Direito().Cor() == "preto":
                        Irmao.setCor("vermelho")
                        nodo = NodoPai
                elif Irmao.Esquerdo().Cor() == "preto":
                        Irmao.Direito().setCor("vermelho")
                        self.RotacionarAEsquerda(Irmao)
                        Irmao = NodoPai.Direito()
                        Irmao.setCor(NodoPai.Cor())
                        NodoPai.setCor("preto")
                        Irmao.Esquerdo().setCor("preto")
                        self.RotacionarADireita(NodoPai)
                        nodo = self.RaizDaArvore
                else:
                    break

        nodo.setCor("preto")

    def CapturarNodo(self,dado):
        if self.RaizDaArvore != None:
            if dado == self.RaizDaArvore.Info():
                return self.RaizDaArvore
            else:
                if dado < self.RaizDaArvore.Info() and self.RaizDaArvore.Esquerdo() != None:
                    nodo = self.RaizDaArvore.Esquerdo()
                    while nodo != None:
                        if dado < nodo.Info():
                            nodo = nodo.Esquerdo()
                            continue
                        if dado > nodo.Info():
                            nodo = nodo.Direito()
                            continue
                        else:
                            return nodo
                if dado > self.RaizDaArvore.Info() and self.RaizDaArvore.Direito() != None:
                    nodo = self.RaizDaArvore.Direito()
                    while nodo != None:
                        if dado < nodo.Info():
                            nodo = nodo.Esquerdo()
                            continue
                        if dado > nodo.Info():
                            nodo = nodo.Direito()
                            continue
                        else:
                            return nodo
                else:
                    return None
        else:
            return None



    def RotacionarAEsquerda(self,nodo):
        FilhoDireito=nodo.Direito() #Filho Direito
        if FilhoDireito!=None:
            if FilhoDireito.Info()!=None:
                print nodo.Info()
                print FilhoDireito.Info()
                nodo.setDireito(FilhoDireito.Esquerdo()) #Faz o nodo ser pai do filho esquerdo do seu filho direito
                if FilhoDireito.Esquerdo()!=None:
                    FilhoDireito.Esquerdo().setPai(nodo) #o nodo agora ? pai do filho direito do seu antigo filho
                else:
                    NodoNulo(nodo)

                FilhoDireito.setPai(nodo.Pai()) #O pai do nodo agora ? pai do filho direito do nodo
                if nodo.Pai()==None:
                    self.RaizDaArvore=FilhoDireito #caso o nodo rodado fosse a raiz, o filho direito do nodo ser? a nova raiz
                elif self.EhEsquerdo(nodo):#caso o nodo rotacionado ? filho esquerdo, ele agora ser? filho esquerdo do antigo filho direito dele
                    nodo.Pai().setEsquerdo(FilhoDireito)
                else:
                    nodo.Pai().setDireito(FilhoDireito)

                #O nodo rodado agora ? filho do filho direito dele
                FilhoDireito.setEsquerdo(nodo)
                nodo.setPai(FilhoDireito)
    def RotacionarADireita(self,nodo):
        FilhoEsquerdo=nodo.Esquerdo() #Filho Esquerdo
        if FilhoEsquerdo!=None:
            if FilhoEsquerdo.Info()!=None:
                print nodo.Info()
                print FilhoEsquerdo.Info()
                nodo.setEsquerdo(FilhoEsquerdo.Direito()) #Faz o nodo ser pai do filho direito do seu filho esquerdo
                if FilhoEsquerdo.Direito()!=None:
                    FilhoEsquerdo.Direito().setPai(nodo) #o nodo agora ? pai do filho direito do seu antigo filho
                else:
                    NodoNulo(nodo)
                FilhoEsquerdo.setPai(nodo.Pai()) #O pai do nodo agora ? pai do filho esquerdo do nodo

                if nodo.Pai()==None:
                    self.RaizDaArvore=FilhoEsquerdo #caso o nodo rodado fosse a raiz, o filho esquerdo do nodo ser? a nova raiz
                elif self.EhDireito(nodo):#caso o nodo rotacionado ? filho direito, O filho esquerdo dele ser? o filho direito da raiz
                    nodo.Pai().setDireito(FilhoEsquerdo)
                else:
                    nodo.Pai().setEsquerdo(FilhoEsquerdo)

                #O nodo rodado agora ? filho do filho esquerdo dele
                FilhoEsquerdo.setDireito(nodo)
                nodo.setPai(FilhoEsquerdo)
    def Minimo(self,nodo):
        nodoMenor=nodo.Esquerdo()
        if nodoMenor.Info()==None:
            return nodo
        else:
            return self.Minimo(nodoMenor)

    def Maximo(self,nodo):
        nodoMaior=nodo.Direito()
        if nodoMaior.Info()==None:
            return nodo
        else:
            return self.Maximo(nodoMaior)




    def Busca(self,dado):
        return self.BuscaAuxiliar(self.RaizDaArvore, dado)

    def BuscaAuxiliar(self, nodo, dado):
        if dado==nodo.Info():
            self.nodoBusca=nodo
            return dado
        else:
            if dado<nodo.Info():
                if nodo.Esquerdo()!=None:
                    return self.BuscaAuxiliar(nodo.Esquerdo(),dado)
                else:
                     return "N?mero n?o encontrado!"
            elif dado>nodo.Info():
                if nodo.Direito()!=None:
                    return self.BuscaAuxiliar(nodo.Direito(), dado)
                else:
                    return "N?mero n?o encontrado!"

    def Sucessor(self, nodo):
        if nodo.Direito().Info()!=None:
            return self.Minimo(nodo.Direito())
        sucessor=nodo.Pai()
        try:
            while sucessor!=None and nodo==sucessor.Direito():
                sucessor,nodo=sucessor.Pai(), sucessor

            return sucessor
        except:
            return None


    def Predecessor(self, nodo):
        if nodo.Esquerdo().Info()!=None:
            return self.Maximo(nodo.Esquerdo())
        predecessor=nodo.Pai()
        try:
            while predecessor!=None and nodo==predecessor.Esquerdo():
                predecessor,nodo=predecessor.Pai(), predecessor

            return predecessor
        except:
            return None

    def EmOrdem(self):
        self.ListaOrdenada=[]
        self.EmOrdemAuxiliar(self.RaizDaArvore)
        return self.ListaOrdenada

    def EmOrdemAuxiliar(self, nodo):
        if nodo!=None:
            if nodo.Info()!=None:
                self.EmOrdemAuxiliar(nodo.Esquerdo())
                print nodo.Info()
                self.ListaOrdenada.append(nodo.Info())
                self.EmOrdemAuxiliar(nodo.Direito())
    def PaisEFilhos(self,nodo):
        if nodo!=None:
            if nodo.Esquerdo()!=None:
                self.PaisEFilhos(nodo.Esquerdo())
            print nodo.Info()
            if nodo.Direito()!=None:
                print "Filho direito: ", nodo.Direito().Info()
            else:
                print None
            if nodo.Esquerdo()!=None:
                print "Filho esquerdo: ", nodo.Esquerdo().Info()
            else:
                print None
            if nodo.Pai()!=None:
                print "Pai: ", nodo.Pai().Info()

            else:
                print None
            print "Cor: ",nodo.Cor()
            if nodo.Direito()!=None:
                self.PaisEFilhos(nodo.Direito())



