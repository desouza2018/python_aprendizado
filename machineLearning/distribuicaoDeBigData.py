# Big Data Distributions 
# Distribuições de Big Data
# Uma matriz contendo 250 valores não é considerada muito grande, 
# mas agora você sabe como criar um conjunto aleatório de valores, 
# e alterando os parâmetros, você pode criar o conjunto de dados tão grande quanto quiser. 
# exemplo
# Crie uma matriz com 100000 números aleatórios e exiba-os usando um histograma com 100 barras:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()