# -*- coding: utf-8 -*- 

arquivo = open("MeuArquivo.txt")

linhas = arquivo.readlines()
for linha in linhas:
    print(linha)

#.read traz tudo

# w escreve, e o a faz append
w = open("arquivo2.txt", "w")

w.write("Nothing is true, everything is permitted!")

w.close()