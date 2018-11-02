print("\nRetornando somente as linhas que cotenham a palavra digitada")
palavra = input("Digite a palvra para busca:")
arq = open("arquivo.txt", "r")
contador =0
for linha in arq:
	linha =linha.rstrip()
	if palavra in linha:
		contador = contador + 1
		print(linha)
print("\n Foram retornados", contador, "linhas")
arq.close()