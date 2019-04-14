#visualização de dados

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,2,1]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x,y)
plt.plot(x,y)

plt.bar(x, y)
plt.show()