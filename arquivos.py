
a=eval(input("Numero:"))
print("Resultado da raiz quadrada:",sqrt(a))
import pygame
from math import sqrt
import sys
arq = open("arquivo.txt", "w")
arq.write("Aprendendo python")
arq.write("\n")
arq.write("Manipulando arquivos")
arq.close()

arq = open("arquivo.txt")
for i in arq:
	sys.stdout.write(i)
arq.close()

