# https://www.w3schools.com/python/python_ml_scale.asp
# Machine Learning - Scale - Escala
# Recursos de escala 
# Quando seus dados têm valores diferentes e até mesmo unidades de medição diferentes,
# pode ser difícil compará-los. O que é quilograma comparado com metros? 
# Ou altitude em comparação com o tempo? 
# A resposta para este problema é o escalonamento. 
# Podemos dimensionar dados em novos valores que são mais fáceis de comparar.
# Dê uma olhada na tabela abaixo, 
# é o mesmo conjunto de dados que usamos no capítulo de regressão múltipla,
# mas desta vez a coluna de volume contém valores em litros 
# em vez de centímetro3 (1,0 em vez de 1000).
# carro	 -  modelo	 volume - peso - CO2	
# Toyota	Aygo   - 1.0 	- 790  - 99

# Pode ser difícil comparar o volume 1.0 com o peso 790, 
# mas se dimensioná-los ambos em valores comparáveis, 
# podemos facilmente ver quanto um valor é comparado ao outro.
# Existem diferentes métodos para dimensionamento de dados,
# neste tutorial usaremos um método chamado padronização.
# O método de padronização usa esta fórmula: z = (x - u) / s
# Onde está o novo valor, é o valor original, é a média e é o desvio padrão.zxus 
# Se você pegar a coluna de peso do conjunto de dados acima,
# o primeiro valor é 790, e o valor escalonado será:
# (790 - 1292.23) / 238.74 = -2.1
# O Valor 1292.23 foi obtido através do código:
# import pandas
# import numpy

# df = pandas.read_csv("cars2.csv")

# v = df['Weight']

# Finding the mean value:
# mean = numpy.mean(v)

# print(mean)

# O valor 238.74 foi obtido através do código:
# import pandas
# import numpy

# df = pandas.read_csv("cars2.csv")

# v = df['Weight']

#Finding the standard deviation:
# std = numpy.std(v)

# print(std)

# Se você pegar a coluna de volume do conjunto de dados acima, 
# o primeiro valor é 1.0, e o valor escalonado será: 
# (1.0 - 1.61) / 0.38 = -1.59

# Agora você pode comparar -2.1 com -1,59 em vez de comparar 790 com 1.0.
# Você não precisa fazer isso manualmente, o módulo python sklearn tem um 
# método chamado que retorna um objeto Scaler com métodos para transformar 
# conjuntos de dados.StandardScaler()

# Exemplo
# Dimensione todos os valores nas colunas Peso e Volume:

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)
# Resultado: execute o código acima para ver o resultado.
# Note que os dois primeiros valores são -2.1 e -1,59, o que corresponde aos nossos cálculos.
