num1 = float(input("Digite o primeiro numero: "))
operador = input("Digite operador: ")
num2 = float(input("Digite o segundo numero: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "/":
    resultado = num1 / num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "%":
    resultado = num1 % num2
elif operador == "**":
    resultado = num1 ** num2
else:
    resultado = "Operação inválida"

print(resultado)