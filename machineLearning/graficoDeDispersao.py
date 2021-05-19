# Machine Learning - Scatter Plot 
# Gráfico de dispersão
# Um Diagrama ou gráfico de dispersão é um diagrama onde cada valor no conjunto de dados
# é representado por um ponto.
# O módulo Matplotlib tem um método para desenhar parcelas de dispersão, 
# ele precisa de duas matrizes do mesmo comprimento, uma para os valores do eixo x, 
# e outra para os valores do eixo y:

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# A matriz representa a idade de cada carro.x

# A matriz representa a velocidade de cada carro.y
# Exemplo
# Use o método para desenhar um diagrama de parcela de dispersão:scatter()

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# Gráfico de dispersão explicado
# O eixo x representa idades, e o eixo y representa velocidades.

# O que podemos ler no diagrama é que os dois carros mais rápidos tinham 2 anos, 
# e o carro mais lento tinha 12 anos.
# Nota: Parece que quanto mais novo o carro, mais rápido ele dirige, mas isso pode
# ser uma coincidência, afinal só registramos 13 carros.

# treinando o aprendizado no código abaixo
import matplotlib.pyplot as plt

x = ["Zete", "lucio", "Laércio", "Bete", "Ivanete", "Adelson", "Rayssa"]
y = [49, 47, 55, 53, 45, 43, 15]

plt.scatter(x, y)
plt.show()
