from math import sqrt

valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))

print( str(valorA) + "x²" + str(valorB) + "x" + str(valorC) + "=" + str(0))

delta = valorB ** 2 - 4 * valorA * valorC
print("O valor de delta é: " + str(delta))

raizQuadrada = sqrt(delta)

x1= ((-1 * valorB) + raizQuadrada) / (2 * valorA)
x2=  (((-1 * valorB) - raizQuadrada)) / (2 * valorA)

print("x1 = " + str(x1))
print("x2 = " + str(x2))
