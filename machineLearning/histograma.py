# Histogram 
# histograma 
# Para visualizar o conjunto de dados podemos desenhar um histograma com os dados coletados. 
# Usaremos o módulo Python Matplotlib para desenhar um histograma. 
# Conheça o módulo Matplotlib em: https://www.w3schools.com/python/matplotlib_intro.asp

# Exemplo
# Desenhe um histograma:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

# Histograma Explicado 
# Usamos a matriz do exemplo acima para desenhar um histograma com 5 barras. 
# A primeira barra representa quantos valores na matriz estão entre 0 e 1. 
# A segunda barra representa quantos valores estão entre 1 e 2. etc. 
# O que nos dá esse resultado:

# 52 valores estão entre 0 e 1
# 48 valores estão entre 1 e 2
# 49 values are between 2 and 3
# 51 values are between 3 and 4
# 50 values are between 4 and 5
# Nota: Os valores de matriz são números aleatórios 
# e não mostrarão exatamente o mesmo resultado no seu computador.