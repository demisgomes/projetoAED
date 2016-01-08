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
                    print "\nNodo já inserido!(Igual)\n"
                    break
        self.RaizDaArvore.setCor("preto")

    def DeletaNodo(self, nodo):
        if nodo.Direito().Info() == None and nodo.Esquerdo().Info() == None: # se o nodo a ser deletado não tiver filhos
            NodoPai = nodo.Pai() # capturo o pai dele.
            if NodoPai != None: # se ele tiver pai.
                if self.EhDireito(nodo): # vejo se ele é direito.
                    NodoPai.setDireito(nodo.Direito()) # corto a ligação do pai com ele.
                    nodo.setPai(None) # corto a ligação dele com o pai.
                else: # se ele for filho esquerdo.
                    NodoPai.setEsquerdo(nodo.Esquerdo()) # corto a ligação do pai dele com ele.
                    nodo.setPai(None) # corto a ligação dele com o pai.
                NodoSubstituto=NodoNulo(NodoPai)
            else: # se ele não tiver pai (ou seja for raiz).
                self.RaizDaArvore = None # a raiz da árvore recebe None
        else:
            if (nodo.Direito().Info() == None and nodo.Esquerdo().Info() != None) or (nodo.Esquerdo().Info() == None and nodo.Direito().Info() != None): # se ele tiver somente um filho esquerdo ou um filho direito.
                if nodo.Esquerdo().Info() == None: # se o filho que ele tiver for o direito.
                    NodoFilho = nodo.Direito() # o nodo filho recebe o filho direito dele.
                    NodoPai = nodo.Pai() # o nodo pai recebe o pai dele.
                    if NodoPai != None: # se ele tiver pai.
                        if self.EhDireito(nodo): # e ele for filho direito.
                           NodoPai.setDireito(NodoFilho) # O filho direito dele vira filho direito do pai dele.
                           NodoFilho.setPai(NodoPai) # fazendo a relação do filho direito dele com o pai dele.
                           nodo.setPai(None) # corto a ligação dele com o pai dele.
                           nodo.setDireito(None) # corto a ligação dele com o filho direito dele.
                        else: # se ele for filho esquerdo.
                            NodoPai.setEsquerdo(NodoFilho) # O filho direito dele vira filho esquerdo do pai dele.
                            NodoFilho.setPai(NodoPai) # fazendo a relação do filho direito dele com o pai dele.
                            nodo.setPai(None) # corto a ligação dele com o pai dele.
                            nodo.setDireito(None) # corto a ligação com o filho direito dele.
                        NodoSubstituto=NodoFilho
                    else: # se ele não tiver pai (ou seja for raiz)
                        NodoFilho = nodo.Direito() # O nodo filho recebe o filho direito dele.
                        nodo.setDireito(None) # corto a ligação dele com o filho direito.
                        self.RaizDaArvore = NodoFilho # transformo o filho direito dele na raiz da árvore.
                        NodoFilho.setPai(None) # corto a ligação do filho direito dele com ele
                        NodoSubstituto=NodoFilho
                else: # se não
                    if nodo.Direito().Info() == None: # se o filho que ele tive for o esquerdo.
                        NodoFilho = nodo.Esquerdo() # o nodo filho recebe o filho esquerdo dele.
                        NodoPai = nodo.Pai() # o nodo pai recebe o pai dele.
                        if NodoPai != None: # se ele tiver pai.
                            if self.EhDireito(nodo): # e for filho direito.
                                NodoPai.setDireito(NodoFilho) # O seu filho esquerdo vira filho direito do seu pai
                                NodoFilho.setPai(NodoPai) # fazendo a relação do filho esquerdo com o pai
                                nodo.setPai(None) # corto a relação do nodo com o pai
                                nodo.setEsquerdo(None) # corto a relação do nodo com o filho esquerdo
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
                    #DELETANDO NÓ COM DOIS FILHOS
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
                                        NodoPaiSucessor.setEsquerdo(NodoSucessor.Direito())#Mesma Coisa aqui. O NodoSucessor receberá como dado o seu filho direito
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
                               NodoSucessor.setEsquerdo(NodoEsquerdo) # fazendo a relação do filho direito dele com o pai dele.
                               NodoEsquerdo.setPai(NodoSucessor)
                               NodoSucessor.setPai(None) # corto a ligação dele com o pai dele.
                               self.RaizDaArvore=NodoSucessor
                            else: # se ele for filho esquerdo.
                                NodoPaiSucessor.setDireito(None)
                                NodoSucessor.setPai(None) # corto a ligação dele com o pai dele
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
        if NodoSubstituto!=None:
            print "Nodo Substituto: ", NodoSubstituto.Info()
        else:
            print None
        if nodo.Cor()=="preto" and NodoSubstituto.Info()!=None:
            print NodoSubstituto.Info()
            self.RepararDelecao(NodoSubstituto)
                                
                

    def RepararInsercao (self,nodo):
        NodoPai = nodo.Pai()
        
        #se o pai for vermelho, o loop começa, pois se o pai é preto não temos o que fazer
        while (NodoPai!=None and NodoPai.Cor() == "vermelho"):
            print NodoPai.Info()
            print NodoPai.Cor()
            if NodoPai !=None:
                if NodoPai.Pai() !=None:
                    NodoAvo = NodoPai.Pai()
                    #O nodo avô é necessário para operações de rotação
                    if self.EhEsquerdo(NodoPai):
                        Tio = NodoAvo.Direito()
                        
                        if Tio.Info() == None:
                            #Se o tio não existe, dizemos que a cor do nodo inserido será diferente da de seu pai
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

                                #Se a cor do tio for vermelho, trocamos a cor do avô para vermelho
                                #A cor do pai e do tio para preto
                                #E dizemos que o nodo agora é o Nodo Avô,e continuamos o loop
                                
                         else:
                                if self.EhDireito(nodo):
                                    nodo=NodoPai
                                    self.RotacionarAEsquerda(nodo)
                                    nodo.Pai().setCor("preto")
                                    NodoPai=nodo.Pai()
                                    NodoAvo=NodoPai.Pai()
                                    NodoAvo.setCor("vermelho")
                                    self.RotacionarADireita(nodo.Pai().Pai())

                                    #Caso o nodo é filho esquerdo, dizemos que o nodo agora é o NodoPai
                                    #Rotacionamos o novo nodo à esquerda
                                    #O nodo pai, que pode ser diferente após a rotação, recebe a cor preta
                                    #E o nodo avô recebe a cor vermelha
                                    #Assim, rotacionamos o noso avô à direita
                                    
                    else:
                        #O else é a mesma coisa, apenas trocamos o esquerdo pelo direito
                        
                        Tio = NodoAvo.Esquerdo()
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
                #Caso o nodo seja a raiz da arvore, ele receberá a cor preta
                nodo.setCor("preto")



    def RepararDelecao(self,nodo):
        print "Entrou no método RepararDeleção!\n"
        while nodo !=self.RaizDaArvore and nodo.Cor() == "preto":
            print "Novo Nodo:", nodo.Info()
            print "Cor do Nodo: ", nodo.Cor()
            NodoPai = nodo.Pai()
            if self.EhEsquerdo(nodo):
                Irmao = NodoPai.Direito()
                if Irmao.Cor() =="vermelho":
                    print "Entrou no primeiro if\n"
                    Irmao.setCor("preto")
                    NodoPai.setCor("vermelho")
                    self.RotacionarAEsquerda(NodoPai)
                    Irmao = NodoPai.Direito()
                if Irmao.Esquerdo().Cor == "preto" and Irmao.Direito().Cor()=="preto":
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
                if Irmao.Cor()  == "vermelho":
                    print "Entrou no primeiro if\n"
                    Irmao.setCor("preto")
                    NodoPai.setCor("vermelho")
                    self.RotacionarADireita(NodoPai)
                    Irmao = NodoPai.Esquerdo()
                if Irmao.Esquerdo().Cor() == "preto" and Irmao.Direito().Cor() == "preto":
                    print "Entrou no segundo if\n"
                    Irmao.setCor("vermelho")
                    nodo = NodoPai
                elif Irmao.Esquerdo().Cor() == "preto":
                    print "Entrou no primeiro if\n"
                    Irmao.Direito().setCor("vermelho")
                    self.RotacionarAEsquerda(Irmao)
                    Irmao = NodoPai.Direito()
                    Irmao.setCor(NodoPai.Cor())
                    NodoPai.setCor("preto")
                    Irmao.Esquerdo().setCor("preto")
                    self.RotacionarADireita(NodoPai)
                    nodo = self.RaizDaArvore
            
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
                    FilhoDireito.Esquerdo().setPai(nodo) #o nodo agora é pai do filho direito do seu antigo filho
                else:
                    NodoNulo(nodo)

                FilhoDireito.setPai(nodo.Pai()) #O pai do nodo agora é pai do filho direito do nodo
                if nodo.Pai()==None:
                    self.RaizDaArvore=FilhoDireito #caso o nodo rodado fosse a raiz, o filho direito do nodo será a nova raiz
                elif self.EhEsquerdo(nodo):#caso o nodo rotacionado é filho esquerdo, ele agora será filho esquerdo do antigo filho direito dele
                    nodo.Pai().setEsquerdo(FilhoDireito)
                else:
                    nodo.Pai().setDireito(FilhoDireito)
                    
                #O nodo rodado agora é filho do filho direito dele    
                FilhoDireito.setEsquerdo(nodo)
                nodo.setPai(FilhoDireito)
        print "Após a Rotação à esquerda\n"
        print "--------------------------------------------------------------"
        self.PaisEFilhos(self.RaizDaArvore)
        print "Fim a rotação à esquerda\n"
        print "-----------------------------------------------------"


    def RotacionarADireita(self,nodo):
        FilhoEsquerdo=nodo.Esquerdo() #Filho Esquerdo
        if FilhoEsquerdo!=None:
            if FilhoEsquerdo.Info()!=None:
                print nodo.Info()
                print FilhoEsquerdo.Info()
                nodo.setEsquerdo(FilhoEsquerdo.Direito()) #Faz o nodo ser pai do filho direito do seu filho esquerdo
                if FilhoEsquerdo.Direito()!=None:
                    FilhoEsquerdo.Direito().setPai(nodo) #o nodo agora é pai do filho direito do seu antigo filho
                else:
                    NodoNulo(nodo)
                FilhoEsquerdo.setPai(nodo.Pai()) #O pai do nodo agora é pai do filho esquerdo do nodo    
                    
                if nodo.Pai()==None:
                    self.RaizDaArvore=FilhoEsquerdo #caso o nodo rodado fosse a raiz, o filho esquerdo do nodo será a nova raiz
                elif self.EhDireito(nodo):#caso o nodo rotacionado é filho direito, O filho esquerdo dele será o filho direito da raiz
                    nodo.Pai().setDireito(FilhoEsquerdo)
                else:
                    nodo.Pai().setEsquerdo(FilhoEsquerdo)
                    
                #O nodo rodado agora é filho do filho esquerdo dele    
                FilhoEsquerdo.setDireito(nodo)
                nodo.setPai(FilhoEsquerdo)
        print "Após a Rotação à Direita\n"
        print "--------------------------------------------------------------"
        self.PaisEFilhos(self.RaizDaArvore)
        print "Fim a rotação à Direita\n"
        print "-----------------------------------------------------"

    
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
                     return "Número não encontrado!"
            elif dado>nodo.Info():
                if nodo.Direito()!=None:
                    return self.BuscaAuxiliar(nodo.Direito(), dado)
                else:
                    return "Número não encontrado!"

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
        
    


Tree=Arvore()
ValorNodo=0
while ValorNodo!=-99:
    ValorNodo=input("Insira um número na árvore. Digite -99 para sair: ")
    if ValorNodo==-99:
        break
    Nodo=NodoArvore(ValorNodo)
    Tree.InsereNodo(Nodo)
Tree.PaisEFilhos(Tree.RaizDaArvore)
ListaOrdenada=Tree.EmOrdem()
for g in range(0, len(ListaOrdenada)):
            print '\n',ListaOrdenada[g]
ValorNodo = 0
while ValorNodo != -99:
    ValorNodo = input("Digite um número para ser deletado da árvore. Digite -99 para sair: ")
    if ValorNodo == -99:
        break
    Nodo = Tree.CapturarNodo(ValorNodo)
    if Nodo == None:
        print "Esse nodo não existe"
    Tree.DeletaNodo(Nodo)
    Tree.PaisEFilhos(Tree.RaizDaArvore)
    ListaOrdenada=Tree.EmOrdem()
    for g in range(0, len(ListaOrdenada)):
            print '\n',ListaOrdenada[g]
busca = 0   
while busca !=-99:
    busca=input("Digite um número para buscar na árvore. Para sair digite -99: ")
    print Tree.Busca(busca)
    if Tree.Busca(busca)!="Número não encontrado!":
        if Tree.nodoBusca.Pai()!=None:
            print "Seu pai é o nodo cujo número é : ", Tree.nodoBusca.Pai().Info(), "\n"
            if Tree.EhDireito(Tree.nodoBusca)==True:
                print "%i é filho direito de %i\n"%(busca, Tree.nodoBusca.Pai().Info())
            else:
                print "%i é filho esquerdo de %i\n"%(busca, Tree.nodoBusca.Pai().Info())
        if Tree.Sucessor(Tree.nodoBusca)!=None:
            print "Seu sucessor é: %i\n"%(Tree.Sucessor(Tree.nodoBusca).Info())

        if Tree.Predecessor(Tree.nodoBusca)!=None:
            print "Seu predecessor é %i\n"%(Tree.Predecessor(Tree.nodoBusca).Info())
print "o Nodo mínimo é: ", Tree.Minimo(Tree.RaizDaArvore).Info()
print "o Nodo máximo é: ", Tree.Maximo(Tree.RaizDaArvore).Info()


