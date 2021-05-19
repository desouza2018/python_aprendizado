# Machine Learning - Normal Data Distribution 
# Distribuição normal de dados
#No capítulo anterior aprendemos como criar uma matriz completamente aleatória, 
# de um determinado tamanho, e entre dois valores.
# Neste capítulo aprenderemos como criar uma matriz onde os valores estão 
# concentrados em torno de um determinado valor.
# Na teoria da probabilidade, esse tipo de distribuição de dados é conhecido 
# como a distribuição normalde dados , ou a distribuição de dados gaussianos, 
# em homenagem ao matemático Carl Friedrich Gauss que veio com a fórmula dessa distribuição de dados. 
# Exemplo
# Uma distribuição típica de dados normais:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

# Nota: Um gráfico de distribuição normal também é conhecido 
# como a curva do sino por causa de sua forma característica de um sino.
# Histograma Explicado
# Usamos a matriz do método, com valores de 100000, para 
# desenhar um histograma com 100 barras.numpy.random.normal()

# Especificamos que o valor médio é 5.0, e o desvio padrão é 1.0. 
# O que significa que os valores devem ser concentrados em torno de 5.0,
# e raramente mais longe do que 1,0 da média. 
# E como você pode ver no histograma, a maioria dos valores estão 
# entre 4.0 e 6.0, com um topo de aproximadamente 5.0.