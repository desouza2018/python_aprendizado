# Random Data Distributions 
# Distribuições aleatórias de dados
#No Machine Learning, os conjuntos de dados podem conter milhares, ou até milhões, de valores. 
# Você pode não ter dados do mundo real quando está testando um algoritmo, você pode ter que 
# usar valores gerados aleatoriamente. 
# Como aprendemos no capítulo anterior, o módulo NumPy pode nos ajudar com isso! 
# Vamos criar duas matrizes que estão cheias com 1000 números aleatórios de uma distribuição normal de dados.
# A primeira matriz terá a média definida para 5.0 com um desvio padrão de 1.0.
#A segunda matriz terá a média definida para 10.0 com um desvio padrão de 2.0: 
# Exemplo
# Um gráfico de dispersão com 1000 pontos:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

# Gráfico de dispersão explicado  
# Podemos ver que os pontos estão concentrados em torno do valor 5 no eixo x, e 10 no eixo y. 
# Também podemos ver que o spread é mais amplo no eixo y do que no eixo x.