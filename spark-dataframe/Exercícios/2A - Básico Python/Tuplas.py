# Databricks notebook source
# MAGIC %md #Básico

# COMMAND ----------

# Enunciado: Crie uma tupla com três números inteiros e retorne a tupla.
# Passo 1: Defina uma tupla com três números inteiros.
tupla = (3, 7, 10)
# Passo 2: Retorne a tupla.
print(tupla)


# COMMAND ----------

# Enunciado: Dada uma tupla de nomes, retorne o primeiro nome da tupla.
# Passo 1: Defina uma tupla com nomes.
nomes = ("Alice", "Bob", "Charlie", "David")
# Passo 2: Acesse o primeiro elemento da tupla (índice 0).
primeiro_nome = nomes[0]
# Passo 3: Retorne o primeiro nome.
print(primeiro_nome)


# COMMAND ----------

# Enunciado: Dada uma tupla de números, retorne o segundo número.
# Passo 1: Defina uma tupla de números.
numeros = (15, 27, 42, 59)
# Passo 2: Acesse o segundo elemento da tupla (índice 1).
segundo_numero = numeros[1]
# Passo 3: Retorne o segundo número.
print(segundo_numero)


# COMMAND ----------

# Enunciado: Crie uma função que receba duas palavras como entrada e retorne uma tupla com essas palavras.
# Passo 1: Defina uma função que recebe duas palavras como argumentos.
def criar_tupla(palavra1, palavra2):
    # Passo 2: Crie uma tupla com as duas palavras.
    tupla = (palavra1, palavra2)
    # Passo 3: Retorne a tupla.
    return tupla

# Exemplo de uso da função:
resultado = criar_tupla("gato", "cachorro")
print(resultado)


# COMMAND ----------

# Enunciado: Crie uma função que receba uma tupla de números e retorne a soma de todos os elementos.
# Passo 1: Defina uma função que recebe uma tupla de números como argumento.
def soma_tupla(tupla):
    # Passo 2: Use a função `sum` para calcular a soma dos elementos da tupla.
    soma = sum(tupla)
    # Passo 3: Retorne a soma.
    return soma

# Exemplo de uso da função:
tupla = (1, 2, 3, 4, 5)
resultado = soma_tupla(tupla)
print(resultado)


# COMMAND ----------

# Enunciado: Crie uma função que receba uma tupla de números inteiros e retorne o maior número.
# Passo 1: Defina uma função que recebe uma tupla de números inteiros como argumento.
def maior_numero(tupla):
    # Passo 2: Use a função `max` para encontrar o maior número na tupla.
    maior = max(tupla)
    # Passo 3: Retorne o maior número.
    return maior

# Exemplo de uso da função:
tupla = (18, 7, 32, 45, 12)
resultado = maior_numero(tupla)
print(resultado)


# COMMAND ----------

# Enunciado: Crie uma função que receba uma tupla de strings e retorne a string mais longa.
# Passo 1: Defina uma função que recebe uma tupla de strings como argumento.
def string_mais_longa(tupla):
    # Passo 2: Use a função `max` com a chave `len` para encontrar a string mais longa.
    mais_longa = max(tupla, key=len)
    # Passo 3: Retorne a string mais longa.
    return mais_longa

# Exemplo de uso da função:
tupla = ("maçã", "banana", "laranja", "morango")
resultado = string_mais_longa(tupla)
print(resultado)


# COMMAND ----------

# Enunciado: Crie uma função que receba duas tuplas de números e retorne uma única tupla que contenha todos os elementos das duas tuplas.
# Passo 1: Defina uma função que recebe duas tuplas como argumentos.
def unir_tuplas(tupla1, tupla2):
    # Passo 2: Use o operador de concatenação de tuplas para unir as duas tuplas.
    tupla_unida = tupla1 + tupla2
    # Passo 3: Retorne a tupla unida.
    return tupla_unida

# Exemplo de uso da função:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
resultado = unir_tuplas(tupla1, tupla2)
print(resultado)


# COMMAND ----------

# Enunciado: Crie uma função que receba uma tupla de números e um valor alvo, e retorne quantas vezes o valor alvo aparece na tupla.
# Passo 1: Defina uma função que recebe uma tupla de números e um valor alvo como argumentos.
def contar_valor(tupla, valor_alvo):
    # Passo 2: Use o método `count` para contar quantas vezes o valor alvo aparece na tupla.
    ocorrencias = tupla.count(valor_alvo)
    # Passo 3: Retorne o número de ocorrencias.
    return ocorrencias

# Exemplo de uso da função:
tupla = (1, 2, 3, 2, 4, 2, 5)
valor_alvo = 2
resultado = contar_valor(tupla, valor_alvo)
print(resultado)


# COMMAND ----------

# Enunciado: Crie uma função que receba uma tupla de números e retorne uma nova tupla sem o último elemento.
# Passo 1: Defina uma função que recebe uma tupla de números como argumento.
def remover_ultimo_elemento(tupla):
    # Passo 2: Utilize a técnica de slicing para criar uma nova tupla sem o último elemento.
    nova_tupla = tupla[:-1]
    # Passo 3: Retorne a nova tupla.
    return nova_tupla

# Exemplo de uso da função:
tupla = (10, 20, 30, 40, 50)
resultado = remover_ultimo_elemento(tupla)
print(resultado)


# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md #Intermediário

# COMMAND ----------

# MAGIC %md #Avançado

# COMMAND ----------

#noqa
