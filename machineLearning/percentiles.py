# Machine Learning - Percentiles 
# Percentis são usados em estatísticas para lhe dar um número que descreve 
# o valor que um determinado percentual dos valores são menores do que. 
# Exemplo: Digamos que temos uma série de idades de todas as pessoas que vivem em uma rua.

# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# O que é o 75. percentil? A resposta é 43, o que significa que 75% das pessoas têm 43 anos ou menos. 
# O módulo NumPy tem um método para encontrar o percentil especificado:

# Exemplo
# Use o método NumPy para encontrar os percentis:percentile()

import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)# O Resultado será 43.

# Exemplo 
# Qual é a idade em que 90% das pessoas são mais jovens do que?

import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)# O Resultado será 61.
