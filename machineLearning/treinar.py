# Split Into Train/Test - Dividido em trem/teste
# O conjunto de treinamento deve ser uma seleção aleatória de 80% dos dados originais.
# O conjunto de testes deve ser os 20% restantes.
# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# Display the Training Set - Exibir o conjunto de treinamento
# Exibir o mesmo gráfico de dispersão com o conjunto de treinamento:
# Exemplo de treino
# plt.scatter(train_x, train_y)
# plt.show()
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]

plt.scatter(train_x, train_y)
plt.show()
# Resultado: execute o código acima para ver o resultado.
# Parece o conjunto de dados original, então parece ser uma seleção justa:
