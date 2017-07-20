#!/usr/bin/env python3.5

# main
if __name__ == "__main__":
	arquivo = open("saida.txt", 'w')
	l = {1,2,3,4,5}
	arquivo.write(str(l))
	arquivo.write("s")
	arquivo.writelines("s")
	arquivo.write("\nfoi")