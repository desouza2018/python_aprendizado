# Variance 
# Variação 
# Variância é outro número que indica como os valores estão espalhados. 
# Na verdade, se você pegar a raiz quadrada da variância, você terá o desvio padrão! 
# Ou o contrário, se você multiplicar o desvio padrão por si só, você tem a variância! 
# Para calcular a variância você tem que fazer o seguinte: 

# 1. Encontre a média: 
# (32+111+138+28+59+77+97) / 7 = 77.4 

# 2. Para cada valor: encontre a diferença da média: 
# 32 - 77.4 = -45.4
# 111 - 77.4 =  33.6
# 138 - 77.4 =  60.6
# 28 - 77.4 = -49.4 
# 59 - 77.4 = -18.4 
# 77 - 77.4 = - 0.4 
# 97 - 77.4 =  19.6

# 3. Para cada diferença: encontre o valor quadrado: 
# (-45.4)2 = 2061.16 
# (33.6)2 = 1128.96 
# (60.6)2 = 3672.36 
# (-49.4)2 = 2440.36 
# (-18.4)2 =  338.56 
# (- 0.4)2 =    0.16 
# (19.6)2 =  384.16

#4. A variância é o número médio dessas diferenças quadradas:

# (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
#Felizmente, o NumPy tem um método para calcular a variância:
#Exemplo 
# Use o método NumPy para encontrar a variância:var()
# A variância é frequentemente representada pelo símbolo Sigma Square: σ2

import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

# O Desvio Padrão e Variância são termos que muitas vezes são usados no Machine Learning, 
# por isso é importante entender como obtê-los, e o conceito por trás deles.
