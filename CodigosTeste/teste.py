#!/usr/bin/env python3.5

class teste1:
	def __init__(self):
		self.arquivo = open("../desc_af1.txt", 'r')
		self.arquivo.readline() # lendo so a primeira linha
		self.estados = self.arquivo.readline().split()

class teste:
	def __init__(self):
		self.t = teste1()

# main
if __name__ == "__main__":
    teste = teste()
    print (teste.t.estados)