# Mediana
# O valor médio é o valor no meio, depois de classificar todos os valores: 
# No exemplo abaixo é o 87.
# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

# É importante que os números sejam classificados antes que você possa encontrar a mediana.
# O módulo NumPy tem um método para isso:
# Exemplo
# Use o método NumPy para encontrar o valor médio:median()

import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

#Se houver dois números no meio, divida a soma desses números por dois.

# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103

# (86 + 87) / 2 = 86.5

# Exemplo
# Usando o módulo NumPy:

import numpy
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)
