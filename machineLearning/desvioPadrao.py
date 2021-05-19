# Machine Learning - Standard Deviation 
# O que é desvio padrão?
# O desvio padrão é um número que descreve como os valores são espalhados. 
# Um desvio padrão baixo significa que a maioria dos números estão próximos do valor médio (médio). 
# Um desvio de alto padrão significa que os valores estão espalhados por uma faixa mais ampla. 
# Exemplo: Desta vez registramos a velocidade de 7 carros: 
# speed = [86,87,88,86,87,85,86] 
# O desvio padrão é: 0.9 
# O que significa que a maioria dos valores estão dentro da faixa de 0,9 do valor médio, que é de 86,4. 
# Façamos o mesmo com uma seleção de números com uma gama maior: 
# speed = [32,111,138,28,59,77,97] 
# O desvio padrão é: 37.85 
# O que significa que a maioria dos valores está dentro da faixa de 37,85 do valor médio, que é de 77,4. 
# Como você pode ver, um desvio padrão mais alto indica que os valores estão espalhados por uma faixa mais ampla. 
# O módulo NumPy tem um método para calcular o desvio padrão: 
# Exemplo 
# Use o método NumPy para encontrar o desvio padrão:std()

import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

#exemplo

import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

# O Desvio Padrão é frequentemente representado pelo símbolo Sigma: σ
# desvio padrão 
# Como aprendemos, a fórmula para encontrar o desvio padrão é a raiz quadrada da variância: 
# Use o método NumPy para encontrar a variância:var() 
#   import numpy 
#   speed = [32,111,138,28,59,77,97] 
#   x = numpy.var(speed) 
#   print(x)
# √1432.25 = 37.85
# O Desvio Padrão e Variância são termos que muitas vezes são usados no Machine Learning, 
# por isso é importante entender como obtê-los, e o conceito por trás deles.