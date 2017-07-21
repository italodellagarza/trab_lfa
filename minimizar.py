#!/usr/bin/env python3.5
# Desenvolvido por:  Ítalo Della Garza Silva
#                    Bruno Queiróz Santos
#                    Márcio Inácio
# Para a disciplina de Linguagens Formais e Autômatos
# na Universidade Federal de Lavras - UFLA
# Data: 

'''O programa minimiza um autômato finito determinístico conforme o arquivo de entrada
   O autômato é aqui formalizado em uma quíntupla (estados, alfabeto, transições, iniciais e finais)
   Na qual a informação de estado final é armazenada na própria estrutura Estado'''

# Biblioteca necessaria para utilizar argv 
import sys; 

class Estado(object):
    def __init__(self, nomeEstado):
        '''Construtor de classe'''
        self.nomeEstado = nomeEstado
        self.final = False

class Transicao(object):
    def __init__(self, estadoAtual, estadoSeguinte, letra):
        '''Construtor de classe'''
        # A transição vai de estadoAtual para estadoSeguinte
        self.estadoAtual = estadoAtual
        self.estadoSeguinte = estadoSeguinte
        self.letra = letra

class Automato(object):
    def __init__(self):
        '''Construtor de classe.'''
        entrada = open(sys.argv[1], 'r')
        # Aqui, começamos a pegar todos os estados do arquivo e eliminar caracteres inúteis:
        entrada.readline()
        temp = entrada.readline().replace(",", " ").replace("{", "").replace("}","").split()
        self.estados = []
        for nome in temp:
            self.estados.append(Estado(nome))

        # A seguir, aplicamos a mesma logica acima para o alfabeto
        temp = entrada.readline().replace(",", " ").replace("{", "").replace("}","").split()
        self.alfabeto = []
        for letra in temp:
            self.alfabeto.append(letra)

        # Para as transições, temos que ler várias linhas. Precisamos de um critério de parada:
        entrada.readline() # Lê o '{'
        # Acusa como errado. Testar:
        temp = entrada.readline()
        self.transicoes = []
        while temp[0] == '(':
            temp = temp.replace(",", " ").replace("(", "").replace(")", "").replace("->", " ").split()
            ida = Estado(temp[0])
            chega = Estado(temp[2])
            for estado in self.estados:
                if estado.nomeEstado == ida.nomeEstado:
                    ida = estado
                if estado.nomeEstado == chega.nomeEstado:
                    chega = estado
            self.transicoes.append(Transicao(ida, chega, temp[1]))
            temp = entrada.readline()

        # Para o estado inicial, basta ler seu nome e buscá-lo na lista já existente:
        temp = entrada.readline().replace(",", "")
        self.inicial = self.estados[0]
        for estado in self.estados:
            if temp == estado.nomeEstado + '\n': # Adicionei o \n porque a string temp o possui quando lê do arquivo.
                self.inicial = estado

        # Para os estados finais, procurar cada um na lista de estados e setá-los como final = True
        temp = entrada.readline().replace(",", " ").replace("{", "").replace("}", "").split()
        for tempEstado in temp:
            for estado in self.estados:
                if tempEstado == estado.nomeEstado:
                    estado.final = True

        # TODO Melhorar !!! (E tratar excessão)

        entrada.close()

    def minimizaAutomato(self):
        #automato = open(sys.argv[2], 'w')
        #tabela = open(sys.argv[3], 'w')
        # TODO (Tratar por estrutura, se necessário)
        # TODO 1. O programa cria uma lista de pares (para cada par, define-se  um boolean D[i,j], uma lista de pares S[i,j] e uma string Motivo)
        # TODO 2. D[final,nao-final] e D[nao-final,final] = False
        lista_pares = []
        for e1 in range(len(self.estados)):
            for e2 in range(len(self.estados)-e1-1):
                lista_pares.append(Par(self.estados[e1], self.estados[e1 + e2 + 1]))

        for par in lista_pares:
            if par.estado1.final != par.estado2.final:
                par.dij = False
                par.motivo = "final/nao final"
                
        for par in lista_pares:
            if par.dij: # Isso garante que a função não leia o par desnecessariamente
                lista_t1 = self.transicoesDeEstado(par.estado1)
                lista_t2 = self.transicoesDeEstado(par.estado2)
                for t1 in lista_t1:
                    for t2 in lista_t2:
                        if t1.letra == t2.letra and par.dij:
                            par_seguinte = par
                            for par2 in lista_pares:
                                if ((t1.estadoSeguinte == par2.estado1 and t2.estadoSeguinte == par2.estado2) or 
                                   (t2.estadoSeguinte == par2.estado1 and t1.estadoSeguinte == par2.estado2)):
                                    par_seguinte = par2
                                
                                if not par_seguinte.dij:
                                    par.nega_dij(t1.letra + "[" + par_seguinte.estado1.nomeEstado.replace("q","")
                                                 +"," +par_seguinte.estado2.nomeEstado.replace("q","") + "]")
                                else:
                                    par_seguinte.sij.append(par)
        for par in lista_pares:
            print("[", par.estado1.nomeEstado, ",", par.estado2.nomeEstado, "] \t\t", par.dij, par.motivo)
            # TODO 3.2 Senao:
            #tabela.close()
            #automato.close()
        self.escreve_tabela(lista_pares)
        #self.escreve_afd_minimizado(lista_pares)

    def transicoesDeEstado(self, estado):
        listaTransicoes = []
        for transicao in self.transicoes:
            if transicao.estadoAtual == estado:
                listaTransicoes.append(transicao)
        return listaTransicoes	

    def escreve_tabela(self, lista_tabela):
    	tabela_saida = open(sys.argv[2], 'w')
    	tabela_saida.write("INDICE\t\tD[i,j] =\t\tS[i,j] =\t\t\tMOTIVO")
    	for linha in lista_tabela:
    		tabela_saida.write("\n[" + str(linha.estado1.nomeEstado).replace("q","") + "," + str(linha.estado2.nomeEstado).replace("q","") + "]")
    		tabela_saida.write("\t\t" + str(linha.dij))
    		# tabela_saida.write("\t\t\t{ " + str(linha.sij) + " }")
    		tabela_saida.write("\t\t\t{   }")
    		tabela_saida.write("\t\t\t" + linha.motivo)
    	tabela_saida.close()	

    def escreve_afd_minimizado(self, lista_tabela):
        # TODO: Ler a lista de dados do minimiza automato e juntar estados onde o Dij for True
        afd_minimizado = open(sys.argv[3], 'w')
        afd_minimizado.write("\n(")
        cont = 0
        for linha in lista_tabela:
        	if linha.dij:
        		pass
        	else:
        		pass
        	cont+=1

        afd_minimizado.write("\n{" + str(self.alfabeto) + "},")

class Par:
    def __init__(self, estado1, estado2):
        self.estado1 = estado1
        self.estado2 = estado2
        self.dij = True
        self.sij = []
        self.motivo = ""

    def nega_dij(self, motivo):
        self.dij = False
        self.motivo = motivo
        for s in self.sij:
            if s.dij:
                s.nega_dij(("prop[" + self.estado1.nomeEstado.replace("q","") + "," + self.estado2.nomeEstado.replace("q","") + "]"))

# Função Principal
if __name__ == "__main__":
    print ("TODO")
    a = Automato()
    a.minimizaAutomato()

    for estado in a.estados:
    	print(estado.nomeEstado)
    	if estado.final:
    		print('final')
    for transicao in a.transicoes:
    	print(transicao.estadoAtual.nomeEstado + " -> " + transicao.estadoSeguinte.nomeEstado)
    	print(transicao.letra)
    print(a.estados[0] == a.transicoes[0].estadoAtual) # está apontando corretamente
    print(a.inicial.nomeEstado)

    #gerando valores aleatorios 
'''    lista = []
    for i in range(10):
        lista.append(Par(i, i+1))

    for j in lista:
        j.sij.append(1)
        j.motivo = "a"

    a.escreve_tabela(lista)
'''

