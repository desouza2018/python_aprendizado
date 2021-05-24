# https://www.w3schools.com/python/python_ml_multiple_regression.asp
# Coefficient - Coeficiente
# O coeficiente é um fator que descreve a relação com uma variável desconhecida. 
# Exemplo: se for uma variável, então é duas vezes. é a variável desconhecida,
# e o número é o coeficiente.x2xxx2
# Neste caso, podemos pedir o valor do coeficiente de peso contra o CO2,
# e para o volume contra o CO2. 
# A resposta que recebemos nos diz o que aconteceria se aumentarmos, 
# ou diminuirmos, um dos valores independentes.
# Exemplo
# Imprima os valores do coeficiente do objeto de regressão:

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
# Resultado: [0.00755095 0.00780526]

# Resultado explicado
#A matriz de resultados representa os valores de coeficiente de peso e volume.

# Peso: 0,00755095
# Volume: 0,00780526

# Esses valores nos dizem que se o peso aumentar em 1kg, a emissão de CO2 aumenta em 0,00755095g.
# E se o tamanho do motor (Volume) aumentar em 1 cm3, a emissão de CO2 aumenta em 0,00780526 g.
# Acho que é um palpite justo, mas deixe testá-lo!
# Nós já prevíamos que se um carro com um 1300cm3 motor pesa 2300kg, 
# a emissão de CO2 será de aproximadamente 107g.

# E se aumentarmos o peso com 1000kg?
# Exemplo
#Copie o exemplo de antes, mas altere o peso de 2300 para 3300:

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)
# Resultado: [114.75968007]

# Prevemos que um carro com motor de 1,3 litro, e um peso de 3300 kg, liberará aproximadamente 115 gramas de CO2 para cada quilômetro que dirige.
# O que mostra que o coeficiente de 0,00755095 está correto:
# 107.2087328 + (1000 * 0,00755095) = 114,75968


