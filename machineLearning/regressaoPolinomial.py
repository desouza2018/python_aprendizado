# Machine Learning - Polynomial Regression
# site: https://www.w3schools.com/python/python_ml_polynomial_regression.asp
# Regressão polinomial
# Se seus pontos de dados claramente não se encaixarem em uma regressão linear
# (uma linha reta através de todos os pontos de dados), pode ser ideal para regressão polinomial.
# A regressão polinomial, como a regressão linear, utiliza a relação entre as variáveis x e y 
# para encontrar a melhor maneira de desenhar uma linha através dos pontos de dados.
# Como funciona?
# Python tem métodos para encontrar uma relação entre pontos de dados e 
# desenhar uma linha de regressão polinomial. 
# Vamos mostrar como usar esses métodos em vez de passar pela fórmula matemática. 
# No exemplo abaixo, registramos 18 carros enquanto passavam por um certo pedágio. 
# Registramos a velocidade do carro, e a hora do dia (hora) ocorreu a passagem. 
# O eixo x representa as horas do dia e o eixo y representa a velocidade: 
# Exemplo
# Comece desenhando um gráfico de dispersão:
# Execute o código abaixo para ver o resultado

import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()

# Exemplo
# Importe e, em seguida, desenhe a linha de Regressão Polinomial:numpy matplotlib
# Execute o código abaixo para ver o resultado.

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# Exemplo Explicado
# Importe os módulos que você precisa.
# Você pode aprender sobre o módulo NumPy em: https://www.w3schools.com/python/numpy/default.asp 
# Você pode aprender sobre o módulo SciPy em: https://www.w3schools.com/python/scipy/scipy_intro.php

# import numpy
# import matplotlib.pyplot as plt

# Crie as matrizes que representam os valores do eixo x e y:

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy tem um método que nos permite fazer um modelo polinomial:

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Em seguida, especifique como a linha será exibida, começamos na posição 1 e terminamos na posição 22:

# myline = numpy.linspace(1, 22, 100)

# Desenhe o gráfico de dispersão original:

# plt.scatter(x, y)

# Desenhe a linha de regressão polinomial:

# plt.plot(myline, mymodel(myline))

# Exibir o diagrama:

# plt.show()





