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
print "Cadastre os candidatos que ir�o participar da elei��o:\n"
while True:
    nome = raw_input("Digite o nome do %d� candidato ou aperte [ENTER] para encerrar: "%(c))
    if len(nome) == 0:
        break
    numero = randint(10,99)
    candidato = Candidato(nome,numero)
    candidatos.append(candidato)
    print "Candidato cadastrado com sucesso!!\n Nome: %s \n N�mero: %s"%(nome,numero)
    c+=1


print "\nEscolha uma das op��es abaixo: \n"

cadastrar = 1
deletar = 2
votar = 3
relatorio = 4
reset = 5
sair = 6

x = 0
print "Cadastrar eleitor = 1\n Deletar eleitor = 2\n Votar = 3 \n Relat�rio = 4\nResetar votos = 6 \n Sair = 6\n"
while x != sair:
    x=input("Digite a operacao: ")
    if x==cadastrar:
        print "\nCadastro de eleitor: "
        titulo = raw_input("Digite o n�mero do t�tulo: ")
        nodo = NodoArvore(titulo)
        consulta = ArvoreEleitores.CapturarNodo(titulo)
        if consulta == None:
            ArvoreEleitores.InsereNodo(nodo)
            print "Eleitor cadastrado com sucesso\n"
        else:
            print "Eleitor j� cadastrado.\n"
    elif x==deletar:
        print "\nDele��o de eleitor: "
        titulo = raw_input("Digite o n�mero do t�tulo: ")
        nodo = ArvoreEleitores.CapturarNodo(titulo)
        if nodo == None:
            print "Esse t�tulo n�o est� cadastrado.\n"
            continue
        else:
            ArvoreEleitores.DeletaNodo(nodo)
            print "Eleitor deletado com sucesso\n"
    elif x==votar:
        print "\nVota��o: "
        titulo = raw_input("Digite o n�mero do t�tulo: ")
        nodo = ArvoreEleitores.CapturarNodo(titulo)
        if nodo == None:
            print "Esse t�tulo n�o est� cadastrado ou j� votou.\n"
            continue
        else:
            ArvoreEleitores.DeletaNodo(nodo)
            ArvoreVotos.InsereNodo(nodo)
            print nodo.Info()
            c =randint(0,len(candidatos)-1)
            voto = candidatos[c].getNumero()
            candidato = candidatos[c].getNome()
            candidatos[c].setVotos()
            print"\nVoto computado com sucesso: \nN� T�tulo: %s\nCandidato: %s\nN� Candidato: %s\n"%(nodo.Info(),candidato, voto)
            print"\nVota��o parcial.\n"
            eleitoresVotaram.append(nodo.Info())
            i = 0
            while i<len(candidatos):
                nome = candidatos[i].getNome()
                votos = candidatos[i].getVotos()
                print"Candidato: %s  Votos: %d \n"%(nome,votos)
                i+=1
            ArvoreEleitores.PaisEFilhos(ArvoreEleitores.RaizDaArvore)
    elif x == reset:
        i = 0
        while i<len(candidatos):
            candidatos[i].LimparVotos()
            i+=1
        ArvoreVotos = Arvore()
    elif x == relatorio:
        ListaEleitores=ArvoreEleitores.EmOrdem()
        ListaVotos=ArvoreVotos.EmOrdem()
        y = open("relatorio.txt","w")
        y.write("Relat�rio da vota��o.\n")
        y.write("Eleitores: ")
        for g in range(0, len(ListaEleitores)):
            y.write('\n%d'%int(ListaEleitores[g]))
        y.write("\nEleitores que votaram: ")
        for g in range(0, len(ListaVotos)):
            y.write('\n%d'%int(ListaVotos[g]))
        y.write("\nCandidatos e votos")
        i= 0
        while i < len(candidatos):
            nome = candidatos[i].getNome()
            votos = candidatos[i].getVotos()
            y.write("Candidato: %s  Votos: %d\n"%(nome,votos)) 
            i+=1
        j=0
        voto = 0
        vencedor=""
        while j<len(candidatos)-1:
            if candidatos[i].getVotos() > voto:
                        voto = candidatos[i]
                        vencedor = candidatos[i].getNome()
                        j+=1
        y.write("\nResultado")
        if vencedor!="":
            y.write(vencedor)
        else:
            y.write ("\nEmpate!")
        
                
           
           

