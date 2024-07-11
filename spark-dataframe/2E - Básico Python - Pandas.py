# Databricks notebook source
# MAGIC %md *Pandas* é uma biblioteca de software para manipulação e análise de dados

# COMMAND ----------

# MAGIC %md Leitura

# COMMAND ----------

import pandas as pd

# COMMAND ----------

df = pd.read_json("https://data.smcgov.org/resource/mb6a-xn89.json")

# COMMAND ----------

df.head(5)

# COMMAND ----------

df.tail(3)

# COMMAND ----------

# MAGIC %md Análise Básica do Conjunto de Dados
# MAGIC
# MAGIC O pandas possui vários métodos que permitem que você analise rapidamente um conjunto de dados e tenha uma ideia do tipo e quantidade de dados com os quais você está lidando, juntamente com algumas estatísticas importantes.
# MAGIC
# MAGIC > .shape - retorna a contagem de linhas e colunas de um conjunto de dados
# MAGIC <br>
# MAGIC > .describe() - retorna estatísticas sobre as colunas numéricas em um conjunto de dados
# MAGIC <br>
# MAGIC > .dtypes retorna o tipo de dados de cada coluna

# COMMAND ----------

df.shape

# COMMAND ----------

df.describe()

# COMMAND ----------

df.dtypes

# COMMAND ----------

# MAGIC %md Alguns métodos que podem fornecer estatísticas de um DataFrame ou de uma coluna específica em um DataFrame.
# MAGIC
# MAGIC > .mean (eixo = 0 [fornecerá o valor calculado por coluna]) - retorna a média estatística
# MAGIC <br>
# MAGIC > .median (eixo = 0 [fornecerá o valor calculado por coluna]) - retorna a mediana estatística
# MAGIC <br>
# MAGIC > .mode (axis = 0 [fornecerá o valor calculado por coluna]) - retorna o modo estatístico
# MAGIC <br>
# MAGIC > .count () - dá o número de valores totais na coluna
# MAGIC <br>
# MAGIC > .unique () - retorna a matriz de todos os valores únicos nessa coluna
# MAGIC <br>
# MAGIC > .value_counts () - retorna o objeto contendo contagens de valores únicos

# COMMAND ----------

df.bachelor_s_degree_or_higher.mean()

# COMMAND ----------

df.geography.count()

# COMMAND ----------

df.geography_type.unique()

# COMMAND ----------

df.less_than_high_school_graduate.value_counts()

# COMMAND ----------

# MAGIC %md Funções de mapeamento para transformar dados

# COMMAND ----------

def mapGeography(x):
    if x == "Town":
        return 1
    else:
        return 0

# COMMAND ----------

df['geography_mapped_value'] = df.geography_type.apply(mapGeography)

df.geography_mapped_value.value_counts()

# COMMAND ----------

# MAGIC %md Usando *Lambda*

# COMMAND ----------

df['geography_mapped_value_lambda'] = df.geography_type.apply(lambda y: 1 if y == "Town" else 0)

df.geography_mapped_value_lambda.value_counts()

# COMMAND ----------

# MAGIC %md Criação de Objetos

# COMMAND ----------

# MAGIC %md Criar uma série passando uma lista de valores, permitindo que o Pandas crie um índice inteiro padrão:

# COMMAND ----------

s = pd.Series([1, 3, 5, 0, 6, 8])

# COMMAND ----------

pdf = pd.DataFrame(
    {
        "nu_exemplos": s,
    }
)

# COMMAND ----------

pdf

# COMMAND ----------

pdf.sort_values(by=['nu_exemplos'], ascending=False)

# COMMAND ----------

pdf[:-2]

# COMMAND ----------

#noqa
