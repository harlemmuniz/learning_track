# Databricks notebook source
# MAGIC %md #### Numpy
# MAGIC
# MAGIC Numpy é uma abreviação de `Numerical Python` e é usado para realizar uma ampla variedade de operações matemáticas.
# MAGIC
# MAGIC Começaremos importando a biblioteca:

# COMMAND ----------

import numpy as np

# COMMAND ----------

# MAGIC %md Os arrays NumPy são mais rápidos e compactos do que as listas Python. Um array consome menos memória e é conveniente de usar. 
# MAGIC
# MAGIC O NumPy usa muito menos memória para armazenar dados e fornece um mecanismo de especificação dos tipos de dados.
# MAGIC
# MAGIC As dimensões de um ndarray são chamadas de eixos (*axis*). 

# COMMAND ----------

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# COMMAND ----------

c = np.concatenate((a, b))

c

# COMMAND ----------

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

# COMMAND ----------

z = np.concatenate((x, y), axis=0)

z

# COMMAND ----------

# MAGIC %md Usar arr.reshape () dará uma nova forma a um array sem alterar os dados.

# COMMAND ----------

r = np.arange(6)

r

# COMMAND ----------

s = r.reshape(3, 2)

s

# COMMAND ----------

# MAGIC %md Você pode usar index e slice em arrays NumPy da mesma forma que se usa em listas do Python.

# COMMAND ----------

c[0]

# COMMAND ----------

c[1:3]

# COMMAND ----------

c[-2:]

# COMMAND ----------

c[::-1]

# COMMAND ----------

# MAGIC %md Operações Básicas

# COMMAND ----------

data = np.array([1, 2, 3])
ones = np.ones(3, dtype=int)

# COMMAND ----------

data + ones

# COMMAND ----------

data * data

# COMMAND ----------

data.sum()

# COMMAND ----------

s.sum(axis=0)

# COMMAND ----------

s.sum(axis=1)

# COMMAND ----------

# MAGIC %md Mean Square Error
# MAGIC
# MAGIC Esta é a fórmula do erro médio quadrado (usada em modelos de aprendizado de máquina supervisionado que lidam com regressão):
# MAGIC
# MAGIC \\(mse = \frac{1}{n} * \sum  (Y_{pred} - Y)^{2}\\)

# COMMAND ----------

predictions = np.array([1,1,1])
labels = np.array([1,2,3])

# COMMAND ----------

mse = (1/3) * np.sum(np.square(predictions - labels))

mse

# COMMAND ----------

# MAGIC %md ##### Matplotlib

# COMMAND ----------

import matplotlib.pyplot as plt

# COMMAND ----------

# MAGIC %matplotlib inline

# COMMAND ----------

a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22, 15])

# COMMAND ----------

plt.plot(a,'green')

# COMMAND ----------

x = np.linspace(0, 15, 20)
y = np.linspace(0, 15, 20)
plt.plot(x, y, 'o')
plt.plot(x, y, 'red')

# COMMAND ----------

plt.plot(x, y, 'o')
plt.plot(a,'green')

# COMMAND ----------

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

# COMMAND ----------

# MAGIC %md *Saiba mais:* https://cs231n.github.io/python-numpy-tutorial/

# COMMAND ----------

X=[ ] 
for i in range(10,1,-1): 
  X.append(i) 
print(X)

# COMMAND ----------

for i in range(0,10,1):
  print(i)

# COMMAND ----------

#noqa
