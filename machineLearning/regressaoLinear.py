# Machine Learning - Linear Regression
# Regressão
# O termo regressão é usado quando você tenta encontrar a relação entre variáveis. 
# No Machine Learning, e na modelagem estatística, essa relação é usada para prever
# o resultado de eventos futuros.

# Regressão Linear
# A regressão linear usa a relação entre os pontos de dados para desenhar uma linha 
# reta através de todos eles. 
# Esta linha pode ser usada para prever valores futuros.

# No Machine Learning, prever o futuro é muito importante.

# Como funciona?
# Python tem métodos para encontrar uma relação entre pontos de dados e desenhar 
# uma linha de regressão linear. 
# Vamos mostrar como usar esses métodos em vez de passar pela fórmula matemática.

# No exemplo abaixo, o eixo x representa a idade, e o eixo y representa velocidade. 
# Registramos a idade e a velocidade de 13 carros enquanto passavam por um pedágio.
# Vejamos se os dados coletados podem ser usados em uma regressão linear:

#Exemplo
# Comece desenhando um gráfico de dispersão:
# Execute o código para ver o resultado.

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# Exemplo
# Agora, importe e desenhe a linha de Regressão Linear:scipy

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Exemplo Explicado
# Importe os módulos que você precisa.
# Você pode aprender sobre o módulo Matplotlib em: https://www.w3schools.com/python/matplotlib_intro.asp
# Você pode aprender sobre o módulo SciPy em: https://www.w3schools.com/python/scipy/scipy_intro.php

# import matplotlib.pyplot as plt
# from scipy import stats

# Crie as matrizes que representam os valores do eixo x e y:

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute um método que retorne alguns valores-chave importantes da Regressão Linear:

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# Crie uma função que use os valores e para retornar um novo valor. 
# Este novo valor representa onde no eixo y o valor x correspondente será colocado:slopeintercept

# def myfunc(x):
#  return slope * x + intercept

# Execute cada valor da matriz x através da função. 
# Isso resultará em uma nova matriz com novos valores para o eixo y:

# mymodel = list(map(myfunc, x))

# Desenhe o gráfico de dispersão original:

# plt.scatter(x, y)

# Desenhe a linha de regressão linear:

# plt.plot(x, mymodel)

# Exibir o diagrama:

# plt.show()

# R for Relationship - R para Relacionamento 
# É importante saber como a relação entre os valores do eixo x e os valores do eixo y é, 
# se não há relação a regressão linear não pode ser usada para prever nada.

# Essa relação - o coeficiente da correlação - é chamada .r 
# O valor varia de -1 a 1, onde 0 significa sem relação, e 1 (e -1) significa 100% relacionado.r
# Python e o módulo Scipy calcularão esse valor para você, tudo o que você precisa fazer
# é alimentá-lo com os valores x e y.

# Exemplo
# Quão bem meus dados se encaixam em uma regressão linear?

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

# Nota: O resultado -0,76 mostra que há uma relação, não perfeita, 
# mas indica que poderíamos usar a regressão linear em previsões futuras.

# Prever valores futuros
# Agora podemos usar as informações que reunimos para prever valores futuros.

#Exemplo: Vamos tentar prever a velocidade de um carro de 10 anos.

# Para isso, precisamos da mesma função do exemplo acima:myfunc()

# def myfunc(x):
#   return slope * x + intercept

# Exemplo
# Prever a velocidade de um carro de 10 anos:

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)

# O exemplo previu uma velocidade de 85,6, que também podemos ler a partir do diagrama.





