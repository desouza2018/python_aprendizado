# Split Into Train/Test - Dividido em trem/teste
# O conjunto de treinamento deve ser uma seleção aleatória de 80% dos dados originais.
# O conjunto de testes deve ser os 20% restantes.
# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# Exibir o conjunto de testes
# Para garantir que o conjunto de testes não seja completamente diferente,
# vamos dar uma olhada no conjunto de testes também.
# Exemplo de teste
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
test_x = x[80:]
test_y = y[80:]

plt.scatter(test_x, test_y)
plt.show()
# Resultado:
# O conjunto de testes também se parece com o conjunto de dados original: