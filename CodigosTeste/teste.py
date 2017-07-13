#!/usr/bin/env python3.5

class teste:
	def __init__(self):
		self.arquivo = open("desc_af1.txt", 'r')
		self.arquivo.readline() # lendo so a primeira linha
		self.estados = self.arquivo.readline().split()

# main
if __name__ == "__main__":
    t = teste()
    print (t.estados[2])