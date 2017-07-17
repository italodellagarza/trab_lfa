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
        self.letras = []
        self.letras.append(letras)              # Lista de letras do alfabeto
                                                # em que é feita a transição

class Automato(object):
    def __init__(self, arquivoEntrada):
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
        entrada.readline() # Lê o '{'
        # Acusa como errado. Testar:
        temp = entrada.readline()
        self.transicoes = []
        while temp[0] == '(':
            temp = temp.replace(",", " ").replace("(", "").replace("),", "").replace("->", " ").split()
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
        print("inicial = " + temp)
        self.inicial = self.estados[0]
        for estado in self.estados:
            print("aqui1")
            if estado.nomeEstado == temp:
                print("aqui1")
                self.inicial = estado

        # Para os estados finais, procurar cada um na lista de estados e setá-los como final = True
        temp = entrada.readline().replace(",", " ").replace("{", "").replace("}", "").split()
        for tempEstado in temp:
            for estado in self.estados:
                if tempEstado == estado.nomeEstado:
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
    print ("TODO")
    a = Automato("desc_af1.txt")
    for estado in a.estados:
        print(estado.nomeEstado)
        if estado.final:
            print('final')
    for transicao in a.transicoes:
        print(transicao.estadoAtual.nomeEstado + " -> " + transicao.estadoSeguinte.nomeEstado)
        print(transicao.letras)

    print (a.estados[0] == a.transicoes[0].estadoAtual) # está apontando corretamente

    print (a.inicial.nomeEstado)


