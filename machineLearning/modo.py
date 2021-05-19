from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

# Modo
# O valor do modo é o valor que aparece mais vezes:

# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

# O módulo SciPy tem um método para isso. Conheça o módulo SciPy em:
# https://www.w3schools.com/python/scipy/scipy_intro.php

# Exemplo
# Use o método SciPy para encontrar o número que aparece mais:mode()
# A Média, Mediana e Modo são técnicas que muitas vezes são usadas no Machine Learning, 
# por isso é importante entender o conceito por trás deles.