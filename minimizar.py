# Desenvolvido por:  Ítalo Della Garza Silva
#                    Bruno Queiróz Santos
#                    Márcio Inácio
# Para a disciplina de Linguagens Formais e Autômatos
# na Universidade Federal de Lavras - UFLA
# Data: 

class Automato(object):
    def __init__(self, alfabeto ,estados ,transicoes):
        self.alfabeto = alfabeto
        self.estados = estados
        self.transicoes = transicoes

    def leAutomatoDoArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, 'r')
        # TODO
        arquivo.close()

    def minimizaAutomato(self):
	    # TODO

#main
if __name__ == "__main__":
    print "TODO"