# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
# Bad Fit?
# Mau Ajuste? Regressao Polinomial Mau Ajuste
# Vamos criar um exemplo onde a regressão polinomial não seria 
# o melhor método para prever valores futuros.
# Exemplo
# Esses valores para o eixo x e y devem resultar em um ajuste muito ruim para a regressão polinomial:
# Execute o código abaixo para ver o resultado.

import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# E o valor r-quadrado?
# Exemplo
# Você deve obter um valor muito baixo de r-quadrado.

import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))
# O resultado: 0,00995 indica uma relação muito ruim, 
# e nos diz que este conjunto de dados não é adequado para regressão polinomial.