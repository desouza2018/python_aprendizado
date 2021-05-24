# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
# R-Squared 
# R-Quadrado
# É importante saber o quão bem a relação entre os valores do eixo x e y é, 
# se não há relação a regressão polinomial não pode ser usada para prever nada.
# A relação é medida com um valor chamado r-quadrado(r-squared).
# O valor r-quadrado varia de 0 a 1, onde 0 significa sem relação, e 1 significa 100% relacionado.
# Python e o módulo Sklearn calcularão esse valor para você, 
# tudo o que você precisa fazer é alimentá-lo com as matrizes x e y:

# Exemplo
# Quão bem meus dados se encaixam em uma regressão polinomial?
# Execute o código abaixo para ver o resultado.
# numpy e scipy devem estar instalados.
# se não conseguir rodar o código e ver o  erro: no module named sklearn, 
# abra o cmd(windows), e use o seguinte comando: pip install numpy scipy scikit-learn
# Feito isso, execute o código abaixo. 

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

# Nota: O resultado 0,94 mostra que há uma relação muito boa, 
# e podemos usar a regressão polinomial em previsões futuras.

# Prever valores futuros
# Agora podemos usar as informações que reunimos para prever valores futuros.

# Exemplo: Vamos tentar prever a velocidade de um carro que passa 
# pelo pedágio por volta das 17 P.M:

# Para isso, precisamos da mesma matriz do exemplo acima:mymodel

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Exemplo
#Prever a velocidade de um carro que passa a 17 P.M:

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)
# O exemplo previu uma velocidade de 88,87, que também pudemos ler a partir do diagrama:
# veja o arquivo regressaoPolinomial.py

