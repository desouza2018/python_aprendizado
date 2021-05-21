# Machine Learn 
# Regressão Linear- continuação

# Mau Ajuste?
# Criemos um exemplo onde a regressão linear não seria o melhor método para prever valores futuros.

# Exemplo
# Esses valores para o eixo x e y devem resultar em um ajuste muito ruim para a regressão linear:
# Lembre-se:
# O valor varia de -1 a 1, onde 0 significa sem relação, e 1 (e -1) significa 100% relacionado.r

import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# E o para o relacionamento?r
# Exemplo
# Você deve obter um valor muito baixo.r

import numpy
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
# O resultado: 0,013 indica uma relação muito ruim, e nos diz que esse conjunto de dados
# não é adequado para regressão linear.
