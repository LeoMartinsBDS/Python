# -*- coding: utf-8 -*-
#para evitar problemas com acento
#isto é um comentário

print("Hello world!")
print("Another message")
print("Olá mundo!")

print(2+2)
print(2-2)
print(2/2)
print(2*2)
# exponenciacao
print(2 ** 3)
# modulo
print(10 % 3)

my_var = "Hello word" #string
print(my_var)

var1 = 1 # integer var
print(var1)

var2 = 1.1 # float var
print(var2)

var3 = True # bool var
var4 = False

print(var3)
print(var4)

x = 1
y = 2

#condição logica
if x==y:
    print("numeros iguais")
elif x > y:
    print("x é maior que y")
elif y > x:
    print("y é maior que x")
else:
    print("x e y são diferentes")

#estruturas de repetição
while x < 10:
    print(x)
    x = x + 1

lista = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]

for i in lista2:
    print(i)

for i in range(10,20,2):
    print(i)

minha_string = "O rato roeu a roupa do rei de Roma"
busca = minha_string.find("rei")
print(minha_string[busca:])

numero = input("Digite um numero: ")
print("O numero digitado eh: " + numero)

nome = input("Digite o seu nome: ")
print("Bem-vindo " + nome)
print(nome[2])
print(nome[0:5])
print(nome.lower())
print(nome.upper())

tamanho = len(nome)
print(tamanho)

"""
comentario de muitas linhas
.strip(remove carecteres especiais)
.find("palavra") -> me retorna aonde foi encontrado a palavra informado
"""