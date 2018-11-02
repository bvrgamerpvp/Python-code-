
from math import sqrt

import sys

i = 0

x = []

for i in range(0, 20):
       
       for i in range(0, 20):
              
              if i % 2 == 0:
                     
                     x += [i] 
   
print(x)

b = eval(input("99/1:"))

arq = open("arquivo.txt", "w")

a=eval(input("Numero:"))

arq = open("arquivo.txt", "w")

print("Resultado da raiz quadrada:",sqrt(a))

arq.write("Aprendendo python")

arq.write("\n")

arq.write("Manipulando arquivos")

arq.write("\n")

arq.write(str(sqrt(a)))

arq.write("\n")

arq.write(str(sqrt(a ** 2)))

arq.write("\n")

arq.write(str(x))

arq.close()


arq = open("arquivo.txt", "r")

for i in arq:
       arq = open("arquivo.txt", "r")
       sys.stdout.write(i)
arq.close()









def sys():
       
      print("While ok")
      
      arq = open("arquivo.txt", "w")
      
while b != 99:
       
       sys()
       
