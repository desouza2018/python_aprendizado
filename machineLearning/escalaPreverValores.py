# https://www.w3schools.com/python/python_ml_scale.asp
# Predict CO2 Values - Prever valores de CO2
# A tarefa no capítulo De Regressão Múltipla era prever 
# a emissão de CO2 de um carro quando você só sabia seu peso e volume.
# Quando o conjunto de dados for dimensionado, você terá que usar a escala quando prever valores:
# Exemplo
# Prever a emissão de CO2 de um carro de 1,3 litros que pesa 2300 kg:

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
# Execute o código acima para ver o resultado.
# Resultado: [107.2087328]
# No meu código o resultado foi: [107.6579943]
# pois utilizei todos os numeros depois da virgula, 
# ao invés de usar apenas dois. 