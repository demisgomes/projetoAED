from NodoArvore import NodoArvore
from ArvoreEleicao import Arvore
from random import*
from Candidato import Candidato

ArvoreEleitores = Arvore()
ArvoreVotos = Arvore()

eleitoresVotaram = []
nomeEleitores = []
candidatos = []
c = 1
print "Cadastre os candidatos que irão participar da eleição:\n"
while True:
    nome = raw_input("Digite o nome do %dº candidato ou aperte [ENTER] para encerrar: "%(c))
    if len(nome) == 0:
        break
    numero = randint(10,99)
    candidato = Candidato(nome,numero)
    candidatos.append(candidato)
    print "Candidato cadastrado com sucesso!!\n Nome: %s \n Número: %s"%(nome,numero)
    c+=1


print "\nEscolha uma das opções abaixo: \n"

cadastrar = 1
deletar = 2
votar = 3
relatorio = 4
reset = 5
sair = 6

x = 0
print "Cadastrar eleitor = 1\n Deletar eleitor = 2\n Votar = 3 \n Relatório = 4\nResetar votos = 5 \n Sair = 6\n"
while x != sair:
    x=input("Digite a operacao: ")
    if x==cadastrar:
        print "\nCadastro de eleitor: "
        titulo = raw_input("Digite o número do título: ")
        nodo = NodoArvore(titulo)
        consulta = ArvoreEleitores.CapturarNodo(titulo)
        if consulta == None:
            ArvoreEleitores.InsereNodo(nodo)
            print "Eleitor cadastrado com sucesso\n"
            nomeEleitores.append(nodo.Info())
        else:
            print "Eleitor já cadastrado.\n"
    elif x==deletar:
        print "\nDeleção de eleitor: "
        titulo = raw_input("Digite o número do título: ")
        nodo = ArvoreEleitores.CapturarNodo(titulo)
        if nodo == None:
            print "Esse título não está cadastrado.\n"
            continue
        else:
            ArvoreEleitores.DeletaNodo(nodo)
            print "Eleitor deletado com sucesso\n"
    elif x==votar:
        print "\nVotação: "
        titulo = raw_input("Digite o número do título: ")
        nodo = ArvoreEleitores.CapturarNodo(titulo)
        if nodo == None:
            print "Esse título não está cadastrado ou já votou.\n"
            continue
        else:
            ArvoreEleitores.DeletaNodo(nodo)
            ArvoreVotos.InsereNodo(nodo)
            print nodo.Info()
            c =randint(0,len(candidatos)-1)
            voto = candidatos[c].getNumero()
            candidato = candidatos[c].getNome()
            candidatos[c].setVotos()
            print"\nVoto computado com sucesso: \nNº Título: %s\nCandidato: %s\nNº Candidato: %s\n"%(nodo.Info(),candidato, voto)
            print"\nVotação parcial.\n"
            eleitoresVotaram.append(nodo.Info())
            i = 0
            while i<len(candidatos):
                nome = candidatos[i].getNome()
                votos = candidatos[i].getVotos()
                print"Candidato: %s  Votos: %d \n"%(nome,votos)
                i+=1
    elif x == reset:
        i = 0
        while i<len(candidatos):
            candidatos[i].LimparVotos()
            i+=1
        ArvoreVotos = Arvore()
        eleitoresVotaram = []
        print"\nVotos resetados com sucesso."
    elif x == relatorio:
        print "\nRelatório: "
        print "Relatório da votação:\n"
        print "Eleitores: "
        i = 0
        while i <= len(nomeEleitores)-1:
            print"Título Nº: %s"%(nomeEleitores[i])
            i+=1
        print"\nEleitores que votaram:\n "
        i=0
        while i<= len(eleitoresVotaram)-1:
                print"Título Nº: %s" %(eleitoresVotaram[i])
                i+=1
        print"\nCandidatos e votos:\n "
        i= 0
        while i <= len(candidatos)-1:
            nome = candidatos[i].getNome()
            votos = candidatos[i].getVotos()
            print "Candidato: %s  Votos: %d\n"%(nome,votos)
            i+=1
        j=0
        voto = 0
        vencedor = None
        while j<=len(candidatos)-1:
            if candidatos[j].getVotos() > voto:
                    voto = candidatos[j].getVotos()
                    vencedor = candidatos[j].getNome()
            elif candidatos[j].getVotos() == voto:
                voto = candidatos[j].getVotos()
                vencedor = None
            j+=1
        print "\nResultado:\n "
        if vencedor != None:
            print "%s é o vencedor"%(vencedor)
        else:
            print"Houve empate."
        
                
           
           

