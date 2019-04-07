import re

seq1 = input("Digite a sequencia 1: ")
seq2 = input("Digite a sequencia 2: ")

busca = re.match(seq1, seq2)

if busca:
    print("Sequencias identicas")
    print(busca.group())
else:
    print("Sequencias diferentes")