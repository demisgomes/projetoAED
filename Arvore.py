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
                    if NodoAuxiliar.Esquerdo().Info() == None:
                        nodo.setPai(NodoAuxiliar)
                        NodoAuxiliar.setEsquerdo(nodo)
                        NodoAuxiliar=None
                        self.RepararInsercao(nodo)
                    else:
                        NodoAuxiliar=NodoAuxiliar.Esquerdo()
                elif nodo.Info() > NodoAuxiliar.Info():
                    if NodoAuxiliar.Direito().Info() == None:
                        nodo.setPai(NodoAuxiliar)
                        NodoAuxiliar.setDireito(nodo)
                        NodoAuxiliar=None
                        self.RepararInsercao(nodo)
                    else:
                        NodoAuxiliar=NodoAuxiliar.Direito()
                        
                else:
                    print "\nNodo já inserido!(Igual)\n"
                    break
            self.RepararInsercao(nodo)

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
                    else: # se ele não tiver pai (ou seja for raiz)
                        NodoFilho = nodo.Direito() # O nodo filho recebe o filho direito dele.
                        nodo.setDireito(None) # corto a ligação dele com o filho direito.
                        self.RaizDaArvore = NodoFilho # transformo o filho direito dele na raiz da árvore.
                        NodoFilho.setPai(None) # corto a ligação do filho direito dele com ele
                        NodoFilho.setCor("preto")
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
                            NodoFilho.setCor("preto")
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
                                    nodo.setDireito(None)
                                    nodo.setPai(None)
                                    nodo.setEsquerdo(None)
                                    NodoSucessor.setPai(NodoPai)
                                    NodoSucessor.setEsquerdo(NodoEsquerdo)
                                    NodoEsquerdo.setPai(NodoSucessor)
                                    NodoPai.setEsquerdo(NodoSucessor) 
                                    if NodoSucessor.Direito() != None:
                                        NodoPaiSucessor.setEsquerdo(NodoSucessor.Direito())#Mesma Coisa aqui. O NodoSucessor receberá como dado o seu filho direito
                                        NodoSucessor.Direito().setPai(NodoPaiSucessor)
                                        NodoSucessor.setPai(None)#E deletamos o filho direito. Ou seja, o filho do sucessor entra no lugar do sucessor e não tem filhos, deixando o código correto.
                                    else:
                                        NodoPaiSucessor.setEsquerdo(None)

                    #DELETANDO A RAIZ COM DOIS FILHOS!
                    else:
                        NodoPaiSucessor = NodoSucessor.Pai()
                        if nodo == NodoPaiSucessor:
                            nodo.setDado(NodoSucessor.Info())
                            if self.EhDireito(NodoSucessor): # e ele for filho direito.
                               nodo.setDireito(NodoSucessor.Direito()) # O filho direito dele vira filho direito do pai dele.
                               NodoSucessor.Direito().setPai(nodo) # fazendo a relação do filho direito dele com o pai dele.
                               NodoSucessor.setPai(None) # corto a ligação dele com o pai dele.
                               NodoSucessor.setDireito(None) # corto a ligação dele com o filho direito dele.
                               NodoSucessor.setCor("preto")
                            else: # se ele for filho esquerdo.
                                NodoPaiSucessor.setDireito(None)
                                NodoSucessor.setPai(None) # corto a ligação dele com o pai dele
                                NodoSucessor.setCor("preto")
                        else:
                            nodo.setDado(NodoSucessor.Info())
                            if NodoSucessor.Direito()!=None:
                                NodoPaiSucessor.setEsquerdo(NodoSucessor.Direito())
                                NodoSucessor.Direito().setPai(NodoPaiSucessor)
                                NodoSucessor.setPai(None)
                                NodoSucessor("preto")
                            else:
                                NodoPaiSucessor.setEsquerdo(None)
                            
                            
                                
                                
                

    def RepararInsercao(self,nodo):

        while nodo.Cor() =="vermelho":
            NodoPai = nodo.Pai()

            if NodoPai != None:
                if NodoPai.Pai() !=None:
                    NodoAvo = NodoPai.Pai()

                    if NodoPai.EhEsquerdo():

                        Tio = NodoAvo.Direito()
                        if Tio.Cor() =="vermleho":
                            NodoPai.setCor("preto")
                            Tio.setCor("preto")
                            NodoAvo.setCor("vermelho")
                            nodo = NodoAvo
                        elif nodo.EhDireito():
                            nodo = NodoPai
                            self.Rotacionar(nodo)
                            NodoPai.setCor("preto")
                            NodoAvo.setCor("vermelho")
                            self.Rotacionar(NodoAvo)
                    else:
                        Tio = Nodo.Esquerdo()
                        if Tio.Cor() =="vermelho":
                            NodoPai.setCor("preto")
                            Tio.setCor("preto")
                            NodoAvo.setCor("vermelho")
                            nodo = NodoAvo()
                        elif nodo.EhEsquerdo():
                            nodo = NodoPai
                            self.Rotacionar(nodo)
                            NodoPai.setCorr("preto")
                            NodoAvo.setCor("vermelho")
                            self.Rotacionar(NodoAvo)
            self.RaizDaArvore.setCor("preto")

    def RepararDelecao(self,nodo):

        while nodo !=self.RaizDaArvore and nodo.Cor() == "preto":
            NodoPai = nodo.Pai()
            if nodo.EhEsquerdo():
                Irmao = NodoPai.Direito()
                if Irmao.Cor() =="vermelho":
                    Irmao.setCor("preto")
                    NodoPai.setCor("vermelho")
                    self.Rotacionar(NodoPai)
                    Irmao = NodoPai.Direito()
                if Irmao.Esquerdo().Cor == "preto" and Irmao.Direito().Cor()=="preto":
                    Irmao.setCor("vermelho")
                    nodo = NodoPai
                elif Irmao.Direito().Cor() == "preto":
                    Irmao.Esquerdo().setCor("vermelho")
                    self.Rotacionar(Irmao)
                    Irmao = NodoPai.Direito()
                    Irmao.setCor(NodoPai.Cor())
                    NodoPai.setCor("preto")
                    Irmao.Direito().setCor("preto")
                    self.Rotacionar(NodoPai)
                    nodo = self.RaizDaArvore
            else:
                Irmao = NodoPai.Esquerdo()
                if Irmao.Cor()  == "vermelho":
                    Irmao.setCor("preto")
                    NodoPai.setCor("vermelho")
                    self.Rotacionar(NodoPai)
                    Irmao = NodoPai.Esquerdo()
                if Irmao.Esquerdo().Cor() == "preto" and Irmao.Direito().Cor() == "preto":
                    Irmao.setCor("vermelho")
                    nodo = NodoPai
                elif Irmao.Esquerdo().Cor() == "preto":
                    Irmao.Direito().setCor("vermelho")
                    self.Rotacionar(Irmao)
                    Irmao = NodoPai.Direito()
                    Irmao.setCor(NodoPai.Cor())
                    NodoPai.setCor("preto")
                    Irmao.Esquerdo().setCor("preto")
                    self.Rotacionar(NodoPai)
                    nodo = self.RaizDaArvore
            
        nodo.SetCor("preto")        

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

            
                    
    def Rotacionar(self,nodo):
        NodoPai = nodo.Pai()
        if NodoPai.Direito().Info() == None: 
            if NodoPai.Pai() != None:
                NodoAvo = NodoPai.Pai()
                if NodoPai.EhDireito():
                    nodo.setDireito(NodoPai)
                    NodoPai.setPai(nodo)
                    nodo.setPai(NodoAvo)
                    NodoAvo.setDireito(nodo)
                    NodoPai.setEsquerdo(NodoNulo())
                else:
                    nodo.setDireito(NodoPai)
                    NodoPai.setPai(nodo)
                    nodo.setPai(NodoAvo)
                    NodoAvo.setEsquerdo(nodo)
                    NodoPai.setEsquerdo(NodoNulo())
            else:
                nodo.setDireito(NodoPai)
                NodoPai.setPai(nodo)
                NodoPai.setEsquerdo(NodoNulo())
                nodo.setPai(None)
        else: 
            if NodoPai.Pai() != None:
                NodoAvo = NodoPai.Pai()
                if NodoPai.EhDireito():
                    nodo.setEsquerdo(NodoPai)
                    NodoPai.setPai(nodo)
                    nodo.setPai(NodoAvo)
                    NodoAvo.setDireito(nodo)
                    NodoPai.setDireito(NodoNulo())
                else:
                    nodo.setEsquerdo(NodoPai)
                    NodoPai.setPai(nodo)
                    nodo.setPai(NodoAvo)
                    NodoAvo.setEsquerdo(nodo)
                    NodoPai.setDireito(NodoNulo())
            
        
                
    
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
        self.EmOrdemAuxiliar(self.RaizDaArvore)

    def EmOrdemAuxiliar(self, nodo):
        if nodo!=None:
            if nodo.Info()!=None:
                self.EmOrdemAuxiliar(nodo.Esquerdo())
                print nodo.Info()
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
Tree.EmOrdem(Tree.RaizDaArvore)
ValorNodo = 0
while ValorNodo != -99:
    ValorNodo = input("Digite um número para ser deletado da árvore. Digite -99 para sair: ")
    if ValorNodo == -99:
        break
    Nodo = Tree.CapturarNodo(ValorNodo)
    print Nodo.Info()
    if Nodo == None:
        print "Esse nodo não existe"
    Tree.DeletaNodo(Nodo)
    Tree.PaisEFilhos(Tree.RaizDaArvore)
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


