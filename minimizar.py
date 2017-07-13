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

class Estado:
    def __init__(self):
        '''Construtor de classe'''
        self.arquivo = open("desc_af1.txt", 'r')
        self.arquivo.readline()
        self.nomeEstado = self.arquivo.readline().replace(",", " ").replace("{","").replace("}","").split() #funçao que pega todos os estados do arquivo
        self.final = [False]*len(self.nomeEstado)

class Transicao(object):
    def __init__(self, estadoAtual, estadoSeguinte, letras):
        '''Construtor de classe'''
        # A transição vai de estadoAtual para estadoSeguinte
        self.estadoAtual = estadoAtual
        self.estadoSeguinte = estadoSeguinte
        self.letras = letras                    # Lista de letras do alfabeto
                                                # em que é feita a transição

class Automato(object):
    def __init__(self, estados, alfabeto ,transicoes, estadoInicial):
        '''Construtor de classe.'''
        self.estadoInicial = estadoInicial
        self.alfabeto = alfabeto
        self.estados = estados
        self.transicoes = transicoes

    def leAutomatoDoArquivo(self, arquivoEntrada):
        entrada = open(arquivoEntrada, 'r')
        # TODO Primeiro ele deve ler no arquivo o caractere '('. Se não leu sai do programa e dispara excessão!
        # TODO Depois ele deve ler no arquivo os caracteres '{' , '}'. Se não leu sai do programa e dispara excessão!
        # TODO Lê estado por estado, separados por ',' (vírgula)
        # TODO Depois lê o alfabeto, separados por ',' (vírgula)
        # TODO Depois lê as transições, do tipo (estado1, letra -> estado2)
        # TODO Por fim lê o estado inicial e aponta para o mesmo
        # TODO Lê um conjunto de estados finais e muda o atributo deles para True
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
    e = Estado()
    print (e.nomeEstado)
    print (len(e.final))