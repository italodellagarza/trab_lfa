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
    def __init__(self, estadoAtual, estadoSeguinte, letras):
        '''Construtor de classe'''
        # A transição vai de estadoAtual para estadoSeguinte
        self.estadoAtual = estadoAtual
        self.estadoSeguinte = estadoSeguinte
        self.letras = []
        self.letras.append(letras)              # Lista de letras do alfabeto
                                                # em que é feita a transição

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
            ja_existe = False
            for transicao in self.transicoes:
                if transicao.estadoAtual.nomeEstado == temp[0] and transicao.estadoSeguinte.nomeEstado == temp[2]:
                    ja_existe = True
                    transicao.letras.append(temp[1])
            if not ja_existe:
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
        automato = open(sys.argv[2], 'w')
        tabela = open(sys.argv[3], 'w')
        # TODO (Tratar por estrutura, se necessário)
        # TODO 1. O programa cria uma lista de pares (para cada par, define-se  um boolean D[i,j], uma lista de pares S[i,j] e uma string Motivo)
        # TODO 2. D[final,nao-final] e D[nao-final,final] = False
        lista_pares = []
        for e1 in range(len(self.estados)):
        	for e2 in range(len(self.estados)-e1-1):
        		lista_pares.append(Par(self.estados[e1], self.estados[e1 + e2 + 1]))

        for par in lista_pares:
        	if(par.estado1.final and not par.estado2.final) or (not par.estado1.final and par.estado2.final):
        		par.dij = False
        		par.motivo = "final/nao final"

        for par in lista_pares:
        	print(par.estado1.nomeEstado, par.estado2.nomeEstado)
        	print(par.dij)
        	print(par.motivo)
        	

        # TODO 3.2 Senao:
        tabela.close()
        automato.close()

class Par:
	def __init__(self, estado1, estado2):
		self.estado1 = estado1
		self.estado2 = estado2
		self.dij = True
		self.sij = []
		self.motivo = ""
	



# Função Principal
if __name__ == "__main__":
	print ("TODO")
	a = Automato()
	a.minimizaAutomato()
'''	for estado in a.estados:
		print(estado.nomeEstado)
		if estado.final:
			print('final')
	for transicao in a.transicoes:
		print(transicao.estadoAtual.nomeEstado + " -> " + transicao.estadoSeguinte.nomeEstado)
		print(transicao.letras)

	print(a.estados[0] == a.transicoes[0].estadoAtual) # está apontando corretamente

	print(a.inicial.nomeEstado)'''

