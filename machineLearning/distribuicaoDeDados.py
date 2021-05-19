# Machine Learning - Data Distribution 
# Distribuição de dados 
# No início deste tutorial trabalhamos com quantidades muito pequenas de dados em nossos exemplos, 
# apenas para entender os diferentes conceitos. 
# No mundo real, os conjuntos de dados são muito maiores, 
# mas pode ser difícil coletar dados do mundo real, pelo menos em um estágio inicial de um projeto.
# Como podemos obter conjuntos de big data?
# Para criar conjuntos de big data para testes, usamos o módulo Python NumPy,
# que vem com uma série de métodos para criar conjuntos de dados aleatórios, de qualquer tamanho.
# Exemplo
# Crie uma matriz contendo 250 carros alegóricos aleatórios entre 0 e 5:

import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

