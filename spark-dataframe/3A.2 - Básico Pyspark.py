# Databricks notebook source
from datetime import datetime, date
from pyspark.sql import Row

# COMMAND ----------

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=3, b=6., c='texto3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0)),
    Row(a=5, b=8., c='string4', d=date(2000, 4, 1), e=datetime(2000, 1, 4, 12, 0)),
    Row(a=4, b=5., c='text5', d=date(2000, 5, 1), e=datetime(2000, 1, 5, 12, 0))
])

# COMMAND ----------

# DBTITLE 1,Exiba as primeiras 5 linhas do dataframe df.
df.show(5)

# COMMAND ----------

# DBTITLE 1,Exiba a estrutura do dataframe df.
df.printSchema()

# COMMAND ----------

# DBTITLE 1,Exiba somente a coluna 'a' do dataframe df.
df.select('a').show()

# COMMAND ----------

# DBTITLE 1,Exiba somente as colunas 'b' e 'c' do dataframe df.
df.select('b', 'c').show()

# COMMAND ----------

# DBTITLE 1,Crie um novo dataframe chamado df2 que contenha as colunas 'a' e 'b' do dataframe df.
df2 = df.select('a', 'b')
df2.show()

# COMMAND ----------

# DBTITLE 1,Calcule a média da coluna 'b' do dataframe df.
from pyspark.sql.functions import mean

df.select(mean('b')).show()

# COMMAND ----------

# DBTITLE 1,Adicione uma nova coluna 'f' ao dataframe df, que contém os valores da coluna 'a' multiplicados por 2.
from pyspark.sql.functions import col

df.withColumn('f', col('a')*2).show()

# COMMAND ----------

# DBTITLE 1,Adicione uma nova coluna 'g' ao dataframe df, que contém a concatenação da coluna 'c' com a string '_nova'.
from pyspark.sql.functions import concat, lit

df.withColumn('g', concat(col('c'), lit('_nova'))).show()

# COMMAND ----------

# DBTITLE 1,Exiba somente as linhas do dataframe df onde o valor da coluna 'a' é maior que 2.
df.filter(col('a') > 2).show()

# COMMAND ----------

# DBTITLE 1,Exiba somente as linhas do dataframe df onde o valor da coluna 'c' contém a substring 'string'.
df.filter(col('c').contains('string')).show()

# COMMAND ----------

# DBTITLE 1,Ordene o dataframe df pela coluna 'b' em ordem decrescente.
df.orderBy(col('b').desc()).show()

# COMMAND ----------

# DBTITLE 1,Agrupe o dataframe df pela coluna 'a' e exiba a soma da coluna 'b' para cada valor único da coluna 'a'.
df.groupBy('a').sum('b').show()

# COMMAND ----------

# DBTITLE 1,Renomeie a coluna 'a' do dataframe df para 'id' e exiba o resultado.
df.withColumnRenamed('a', 'id').show()

# COMMAND ----------

# DBTITLE 1,Calcule a soma da coluna 'b' do dataframe df e armazene o resultado em uma variável chamada soma. Exiba o resultado.
from pyspark.sql.functions import sum

soma = df.select(sum('b')).show()

# COMMAND ----------

# DBTITLE 1,Exiba somente as linhas do dataframe df onde o valor da coluna 'd' é anterior a '2000-02-01'.
df.filter(col('d') < '2000-02-01').show()

# COMMAND ----------

# DBTITLE 1,Adicione uma nova coluna 'h' ao dataframe df, que contém os valores da coluna 'e' convertidos para a hora do dia.
from pyspark.sql.functions import hour

df.withColumn('h', hour(col('e'))).show()

# COMMAND ----------

# DBTITLE 1,Exiba a quantidade de linhas do dataframe df.
df.count()

# COMMAND ----------

# DBTITLE 1,Utilizando a função join, junte os dataframes df e df2 pela coluna 'key'.
df_join = df1.join(df2, 'key')

# COMMAND ----------

# DBTITLE 1,Testes Unitários
def test_df_detalhado():
    expected = [("Devedor A", "Credor 1", "01/2021", 100.0),
                ("Devedor B", "Credor 1", "01/2021", 50.0),
                ("Devedor C", "Credor 2", "02/2021", 75.0),
                ("Devedor D", "Credor 2", "02/2021", 125.0),
                ("Devedor A", "Credor 1", "03/2021", 200.0),
                ("Devedor B", "Credor 1", "03/2021", 150.0),
                ("Devedor C", "Credor 2", "04/2021", 100.0),
                ("Devedor D", "Credor 2", "04/2021", 50.0)]
    result = [(row.Devedor, row.Credor, row.Mes, row.Divida) for row in df_detalhado.collect()]
    assert result == expected

# COMMAND ----------

#noqa
