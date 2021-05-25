# https://www.w3schools.com/python/python_ml_train_test.asp
# Machine Learning - Train/Test - Treinar/Testar
# Avalie seu modelo
# No Machine Learning criamos modelos para prever o resultado de certos eventos,
# como no capítulo anterior, onde previmos a emissão de CO2 de um carro quando 
# sabíamos o peso e o tamanho do motor.
# Para medir se o modelo é bom o suficiente, podemos usar um método chamado Train/Test( Treinar/Testar).
# O que é Train/Test -Treinar/Testar
# Train/Test é um método para medir a precisão do seu modelo.
# Chama-se Train/Test porque você divide o conjunto de dados em dois conjuntos: 
# um conjunto de treinamento e um conjunto de testes.
# 80% para treinamento e 20% para testes.
# Você treina o modelo usando o conjunto de treinamento.
# Você testa o modelo usando o conjunto de testes.
# Treinar o modelo significa criar o modelo.
# Testar o modelo significa testar a precisão do modelo.
# Comece com um conjunto de dados
# Comece com um conjunto de dados que deseja testar.
# Nosso conjunto de dados ilustra 100 clientes em uma loja e seus hábitos de compra.
# Exemplo

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()
# Resultado: executeo código acima para ver o resultado.
# O eixo x representa o número de minutos antes de fazer uma compra.
# O eixo y representa a quantidade de dinheiro gasto na compra. 

# Split Into Train/Test - Dividido em trem/teste
# O conjunto de treinamento deve ser uma seleção aleatória de 80% dos dados originais.
# O conjunto de testes deve ser os 20% restantes.
# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# Ver os arquivos: treinar.py e teste.py