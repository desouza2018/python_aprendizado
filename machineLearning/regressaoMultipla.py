# https://www.w3schools.com/python/python_ml_multiple_regression.asp
# Multiple Regression - Regressão Múltipla
# A regressão múltipla é como regressão linear,mas com mais de um valor independente, 
# o que significa que tentamos prever um valor baseado em duas ou mais variáveis. 
# Dê uma olhada no conjunto de dados no arquivo cars.csv

# Podemos prever a emissão de CO2 de um carro com base no tamanho do motor,
# mas com a regressão múltipla podemos lançar mais variáveis, como o peso do carro, 
# para tornar a previsão mais precisa.
# Como funciona?
# Em Python temos módulos que farão o trabalho para nós. Comece importando o módulo Pandas. 
# import pandas
# Conheça o módulo Pandas em#: https://www.w3schools.com/python/pandas/default.asp
# Use o comando no cmd(windows) para instalá-lo: 
# pip install pandas. 
# O módulo Pandas nos permite ler arquivos csv e retornar um objeto DataFrame. 
# O arquivo é feito apenas para fins de teste, você pode baixá-lo aqui: carros.csv:
# https://www.w3schools.com/python/cars.csv
# df = pandas.read_csv("cars.csv")
# Em seguida, faça uma lista dos valores independentes e chame essa variável . X 
# Coloque os valores dependentes em uma variável chamada .y

# X = df[['Weight', 'Volume']]
# y = df['CO2']

# Dica: É comum nomear a lista de valores independentes com uma maiúsdia X, 
# e a lista de valores dependentes com um caso inferior y.

# Usaremos alguns métodos do módulo sklearn, então teremos que importar esse módulo também:
# from sklearn import linear_model
# A partir do módulo sklearn usaremos o método para criar um objeto
# de regressão linear.LinearRegression()
# Este objeto tem um método chamado que toma os valores independentes 
# e dependentes como parâmetros e preenche o objeto de regressão com 
# dados que descrevem a relação:fit()

# regr = linear_model.LinearRegression()
# regr.fit(X, y)

# Agora temos um objeto de regressão que está pronto para prever 
# valores de CO2 com base no peso e volume de um carro:

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
# predictedCO2 = regr.predict([[2300, 1300]])
# Exemplo
# Veja o exemplo completo em ação:
# Execute o código abaixo para ver o resultado.

import csv
import pandas 
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
# O resultado do código acima será 107.2087328
# Prevemos que um carro com motor de 1,3 litro, e um peso de 2300 kg, 
# liberará aproximadamente 107 gramas de CO2 para cada quilômetro que dirige.