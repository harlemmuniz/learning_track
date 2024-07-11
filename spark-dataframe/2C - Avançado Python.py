# Databricks notebook source
# MAGIC %md #Trilha Python Avançado

# COMMAND ----------

# MAGIC %md ##List Comprehension
# MAGIC - 

# COMMAND ----------

lista = [1,2,3,4,5,6,7,8,9]
#Imaginem que queremos criar uma nova lista com o cálculo automático
#Podemos fazer isso de duas formas:

# COMMAND ----------

#Forma 1

lista_a_ser_preenchida = [] #Lista vazia
for valor in lista:
  lista_a_ser_preenchida.append(valor**2)

print(lista)
print(lista_a_ser_preenchida) # Observe que todos os número foram elevados ao quadrado(^2)

# COMMAND ----------

#Forma 2
#Vamos usar a estrutura abaixo
# list_comprehension = [valor_a_adicionar laço condição]

lista = [1,2,3,4,5,6,7,8,9]

list_comprehension = [elemento**2 for elemento in lista] #Está sem a condição
print(list_comprehension)

# COMMAND ----------

#Exibir os valores ímpares utilizando list comprehension
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
valores_impares = [valor for valor in lista if valor%2 == 1] #Se o resto(%) da visisão valor/2 for 1 então o valor é ímpar.

print(valores_impares)

# COMMAND ----------

# MAGIC %md ##Função Enumerate

# COMMAND ----------

#Para obter o índice do elemento na lista
lista_enumerate = ['laranja', 'pêra', 'amora', 'mamão', 'framboesa', 'banana', 'uva']

for indice, lista_item in enumerate(lista_enumerate):
  print(indice, lista_item)
#Utilidade está em descobrir o índice do elemento para poder navegar e realizar demais ações.

# COMMAND ----------

# MAGIC %md ##Função Map

# COMMAND ----------

#Sem a função map, multiplicar os valores de uma lista por 2 (lista*2) já sabemos que apenas replica os valores da lista.
#Para multiplicar, ou executar uma determinada ação, cada um dos itens da lista é preciso utilizar a função map. Observe.

lista_map = [1,2,3,4,5,6,7,8,9]

def dobro(num):
  return num*2

print("Valores replicados, observe: --> ", dobro(lista_map)) #Observe que apenas REPLICOU + uma vez a lista. E não é isso que queremos. Queremos utilizar a função dobro item por item.

#Utilizando a função map
#A função MAP recebe dois argumentos como parâmetros map(função, lista). A função map retorna um objeto, e uma maneira de visualizarmos esse objeto é atribuir o valor à uma variável e utilizar um laço for para verificar o resultado. Ou convertendo em uma lista. Observe.

#Variável valor_funcao_dobro no laço for
valor_funcao_dobro = map(dobro, lista_map)
for item in valor_funcao_dobro:
  print(item) #Um por linha, pois é exibido a variável toda vez que entra no laço.

#Convertendo em uma lista
valor_fun_dobro = map(dobro, lista_map)
valor_dobrado = list(valor_fun_dobro)
print(valor_dobrado)


# COMMAND ----------

# MAGIC %md ##Função Reduce
# MAGIC - Reduz uma lista a um único resultado

# COMMAND ----------

#Somar os itens de uma lista
lista_somar = [2,5,9,12,45,32,65,74,13,7,21,4,89,52]

def soma(a, b):
  return a+b

#É preciso importar a função reduce utilizando o comando abaixo
from functools import reduce

#Para utilizar a função reduce é preciso dois argumentos reduce(função, lista)
resultado_soma = reduce(soma, lista_somar)

print(resultado_soma) #Resultado = 430


# COMMAND ----------

# MAGIC %md ##Função Zip
# MAGIC - Tem o objetivo de concatenar duas ou mais listas indíce por índice
# MAGIC - Exemplo: lista_A e lista_B
# MAGIC   - item_1_lista_A | item_1_lista_B
# MAGIC   - item_2_lista_A | item_2_lista_B
# MAGIC   - item_3_lista_A | item_3_lista_B
# MAGIC   - item_4_lista_A | item_4_lista_B

# COMMAND ----------

lista_numeros = [1,2,3,4,5]
lista_nomes = ['João', 'Pedro', 'Maria', 'Lucia', 'Carlos']

#2 listas
for indice_numero, indice_nome in zip (lista_numeros, lista_nomes):
  print(indice_numero, indice_nome)

lista_telefone = [987654321, 987654322, 987654313, 987654324, 987654326]

#3 listas
print("Abaixo veja o exemplo de 3 listas:\n")
for indice_numero, indice_nome, indice_telefone in zip (lista_numeros, lista_nomes, lista_telefone):
  print(indice_numero, indice_nome, indice_telefone)

# COMMAND ----------

#noqa
