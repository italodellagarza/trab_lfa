#!/usr/bin/env python3
# Desenvolvido por:  Ítalo Della Garza Silva
#                    Bruno Queiroz Santos
#                    Márcio Inácio
# Para a disciplina de Linguagens Formais e Autômatos
# na Universidade Federal de Lavras - UFLA
# Data: 22/07/2017

'''O programa minimiza um autômato finito determinístico conforme o arquivo de entrada
   O autômato é aqui formalizado em uma quíntupla (estados, alfabeto, transições, iniciais e finais)
   Na qual a informação de estado final é armazenada na própria estrutura Estado'''

# Biblioteca necessaria para utilizar argv 
import sys; 

class Estado(object):
	'''Representa os estados do autômato'''
	def __init__(self, nome_estado):
		'''Construtor de classe'''
		self.nome_estado = nome_estado
		self.final = False

class Transicao(object):
	'''Representa as transições do autômato'''
	def __init__(self, estado_atual, estado_seguinte, letra):
		'''Construtor de classe'''
		# A transição vai de estado_atual para estado_seguinte
		self.estado_atual = estado_atual
		self.estado_seguinte = estado_seguinte
		self.letra = letra

class Automato(object):
	'''O autômato em sí. Possui uma lista de estados, uma lista de transições e um estado inicial'''
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
				if estado.nome_estado == ida.nome_estado:
					ida = estado
				if estado.nome_estado == chega.nome_estado:
					chega = estado
			self.transicoes.append(Transicao(ida, chega, temp[1]))
			temp = entrada.readline()

		# Para o estado inicial, basta ler seu nome e buscá-lo na lista já existente:
		temp = entrada.readline().replace(",", "")
		self.inicial = self.estados[0]
		for estado in self.estados:
			if temp == estado.nome_estado + '\n': # Adicionei o \n porque a string temp o possui quando lê do arquivo.
				self.inicial = estado

		# Para os estados finais, procurar cada um na lista de estados e setá-los como final = True
		temp = entrada.readline().replace(",", " ").replace("{", "").replace("}", "").split()
		for temp_estado in temp:
			for estado in self.estados:
				if temp_estado == estado.nome_estado:
					estado.final = True

		entrada.close()

	def minimiza_automato(self):
		'''Função que minimiza o automato completo'''

		# Para cada estado, criam-se os pares, que são armazenados em uma lista:
		lista_pares = []
		for e1 in range(len(self.estados)):
			for e2 in range(len(self.estados)-e1-1):
				lista_pares.append(Par(self.estados[e1], self.estados[e1 + e2 + 1]))

		# Faz com que o D[i,j] de estados finais com não-finais seja sempre False.
		for par in lista_pares:
			if par.estado1.final != par.estado2.final:
				par.dij = False
				par.motivo = "final/nao final"
				
		for par in lista_pares:
			if par.dij: # Isso garante que a função não leia o par desnecessariamente.
				lista_t1 = self.transicoes_de_estado(par.estado1)
				lista_t2 = self.transicoes_de_estado(par.estado2)
				for t1 in lista_t1:
					for t2 in lista_t2:
						if t1.letra == t2.letra and par.dij:
							par_seguinte = par # Para inicialiar o par_seguinte
							# Aqui a função busca o par seguinte a partir daquela letra.
							for par2 in lista_pares:
								if ((t1.estado_seguinte == par2.estado1 and t2.estado_seguinte == par2.estado2) or 
								   (t2.estado_seguinte == par2.estado1 and t1.estado_seguinte == par2.estado2)):
									par_seguinte = par2
							# Se o D[i,j] do par seguinte for False, ele negará o D[i,j] do par atual.	
							if not par_seguinte.dij:
								par.nega_dij(t1.letra + par_seguinte.para_string())
							# Senão, ele adicionará o par atual ao S[i,j] do par seguinte.
							elif par_seguinte != par:
								par_seguinte.sij.append(par)

		# Imprimindo a tabela e o autômato minimizado.
		self.escreve_tabela(lista_pares)
		self.atualiza_automato(lista_pares)
		self.escreve_afd_minimizado(lista_pares)

	def transicoes_de_estado(self, estado):
		'''Esta função retorna uma lista com todas as transições de um estado.'''
		lista_transicoes = []
		for transicao in self.transicoes:
			if transicao.estado_atual == estado:
				lista_transicoes.append(transicao)
		return lista_transicoes
	
	def atualiza_automato(self,lista_tabela):
		'''Função que altera a estrutura autômato a partir da tabela encontrada em minimiza_automato()'''
		# Para todo par em que D[i,j] = True, junta-se os dois num só estado.
		for par in lista_tabela:
			if par.dij:
				self.junta_dois_estados(par.estado1, par.estado2, lista_tabela)
		
	def junta_dois_estados(self, estado1, estado2, lista_tabela):
		'''Função que junta dois estados em um único estado e faz as devidas 
		   alterações na estrutura do autômato e na lista'''
		# Copia as informações do estado 2 para o 1.   
		estado1.nome_estado += estado2.nome_estado

		# Arruma a tabela.
		for par in lista_tabela:
			if par.estado1 == estado2:
				par.estado1 = estado1
			if par.estado2 == estado2:
				par.estado2 = estado2

		# Elimina os pares iguais.
		for p1 in range(len(lista_tabela)):
			p2 = p1+1
			while(p2 < len(lista_tabela)):
				if(lista_tabela[p1].estado1 == lista_tabela[p2].estado1 and 
					lista_tabela[p1].estado2 == lista_tabela[p2].estado2):
					del lista_tabela[p2]
				p2 += 1

		# Arruma as transiçoes.
		for transicao in self.transicoes:
			if transicao.estado_atual == estado2:
				transicao.estado_atual = estado1
			if transicao.estado_seguinte == estado2:
				transicao.estado_seguinte = estado1
		if self.inicial == estado2:
			self.inicial = estado1

		# Elimina as transições iguais:
		for t1 in range (len(self.transicoes)):
			t2 = t1+1
			while(t2 < len(self.transicoes)):
				if(self.transicoes[t1].estado_atual == self.transicoes[t2].estado_atual and 
					self.transicoes[t1].estado_seguinte == self.transicoes[t2].estado_seguinte and
					self.transicoes[t1].letra == self.transicoes[t2].letra):
					del self.transicoes[t2]
				t2 += 1
		# Apaga o estado 2 da estrutura.
		i = 0
		while i < len(self.estados):
			if self.estados[i] == estado2:
				del self.estados[i]
			i += 1


	def escreve_tabela(self, lista_tabela):
		'''Função que escreve a tabela no arquivo'''
		tabela_saida = open(sys.argv[2], 'w+')
		tabela_saida.write("INDICE\t\tD[i,j]=\t\t\tS[i,j]=\t\t\t\tMOTIVO")
		for linha in lista_tabela:
			tabela_saida.write("\n[" + str(linha.estado1.nome_estado).replace("q","") + "," + str(linha.estado2.nome_estado).replace("q","") + "]")
			if linha.dij:
				tabela_saida.write("\t\t0")
			else:
				tabela_saida.write("\t\t1")
			dependencias = "{ "
			if len(linha.sij) > 0:
				dependencias += linha.sij[0].para_string()
			for s in linha.sij:
				if linha.sij[0] != s:
					dependencias += ","
					dependencias += s.para_string()
			dependencias += " }"
			tabela_saida.write("\t\t\t" + dependencias)
			tabela_saida.write("\t\t\t\t" + linha.motivo)
		tabela_saida.close()   

	#escreve o automato minimizado, que foi atualizado na funçao atualiza_automato
	def escreve_afd_minimizado(self, lista_tabela):
		'''Escreve o autômato já minimizado no arquivo'''
		afd_minimizado = open(sys.argv[3], 'w+')
		afd_minimizado.write("(")
		afd_minimizado.write("\n{")
		afd_minimizado.write(self.estados[0].nome_estado)
		for i in range(1, len(self.estados)):
			afd_minimizado.write("," + self.estados[i].nome_estado)
		afd_minimizado.write("}")
		afd_minimizado.write("\n{" + str(self.alfabeto).replace("[","").replace("'","").replace("]","") + "},")
		afd_minimizado.write("\n{")
		for transicao in self.transicoes:
			afd_minimizado.write("\n(" + transicao.estado_atual.nome_estado + "," + transicao.letra + "->" + transicao.estado_seguinte.nome_estado + "),")
		afd_minimizado.write("\n},")
		afd_minimizado.write("\n" + self.inicial.nome_estado + ",")
		afd_minimizado.write("\n{")
		virgula = False;
		for estado in self.estados:
			if estado.final:
				if virgula:
					afd_minimizado.write(",")
				afd_minimizado.write(estado.nome_estado)
				virgula = True

		afd_minimizado.write("}\n)")
		afd_minimizado.close()

 # Extra: Transformação de um AFD qualquer em um AFD completo
	def e_completo(self):
		'''Função que verifica se o AFD é completo. Se sim, retorna True, senão, False.'''
		for estado in self.estados:
			transicoes = self.transicoes_de_estado(estado)
			if len(transicoes) != len(self.alfabeto):
				return False
		return True

	def transforma_em_completo(self):
		'''Função que transforma um AFD incompleto em um AFD completo.'''
		if not self.e_completo():
			qerro = Estado("qerro")
			self.estados.append(qerro)

			for estado in self.estados:
				transicoes = self.transicoes_de_estado(estado)
				simbolos_de_trans = []
				for transicao in transicoes:
					simbolos_de_trans.append(transicao.letra)

				for simbolo in self.alfabeto:
					if not simbolos_de_trans.__contains__(simbolo):
						self.transicoes.append(Transicao(estado, qerro, simbolo))

class Par:
	'''Classe que referencia um par de estados, usado na função minimiza_automato().'''
	def __init__(self, estado1, estado2):
		'''Construtor de classe.'''
		self.estado1 = estado1
		self.estado2 = estado2
		self.dij = True
		self.sij = []
		self.motivo = ""

	def nega_dij(self, motivo):
		'''Função que nega o D[i,j] de um par, adiciona o motivo e 
		   nega todos os D[i,j] de seu S[i,j].'''
		self.dij = False
		self.motivo = motivo
		for s in self.sij:
			if s.dij:
				s.nega_dij(("prop[" + self.estado1.nome_estado.replace("q","") + "," + self.estado2.nome_estado.replace("q","") + "]"))
	
	def para_string(self):
		'''Função que retorna uma string para um Par, do tipo [estado1,estado2] para fins de impressão.'''
		str = "[" + self.estado1.nome_estado.replace("q","") + "," + self.estado2.nome_estado.replace("q","") + "]"
		return str

# Função Principal:
if __name__ == "__main__":
	a = Automato()
	if not a.e_completo():
		a.transforma_em_completo()
	a.minimiza_automato()

