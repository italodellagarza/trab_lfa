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
        self.letras.append(letras)              # Lista de letras do alfabeto
                                                # em que é feita a transição

class Automato(object):
    def __init__(self):
        '''Construtor de classe.'''
        entrada = open(arquivoEntrada, 'r')
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
        entrada.readline()
        # Acusa como errado. Testar:
        while temp = entrada.readline().replace(",", " ").replace("(", "").replace("),","").replace("->","").split():
            ja_existe = False
            for estado in self.estados:
                if estado.estadoAtual == temp[0] and estado.estadoSeguinte == temp[2]:
                    ja_existe = True
                    estado.letras.append(temp[1])
            if not ja_existe:
                self.transicoes.append(Transicao(temp[0],temp[2],temp[1]))

        # Para o estado inicial, basta ler seu nome e buscá-lo na lista já existente:
        entrada.readline()
        temp = entrada.readline().replace(",", "")
        for estado in self.estados:
            if estado.nomeEstado == temp:
                self.inicial = estado

        # Para os estados finais, procurar cada um na lista de estados e setá-los como final = True
        temp = entrada.readline().replace(",", " ").replace("{", "").replace("}", "").split()
        for tempEstado in temp:
            for estado in self.estados:
                if tempEstado.nomeEstado == estado.nomeEstado:
                    estado.final = True

        # TODO TESTAR E CORRIGIR!!!!

        entrada.close()

    def minimizaAutomato(self, automatoSaida, tabelaSaida):
        automato = open(automatoSaida)
        tabela = open(tabelaSaida)
        # TODO
        tabela.close()
        automato.close()

# main
if __name__ == "__main__":
    #print ("TODO")
    #e = Estado()
    #print (e.nomeEstado)
    #print (len(e.final))
