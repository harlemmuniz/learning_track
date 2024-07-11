# Databricks notebook source
# MAGIC %md Dados para BI
# MAGIC
# MAGIC O objetivo deste notebook é gerar dados para serem consumidos via powerbi ou metabase para exercitar conhecimentos básicos de visualização de dados.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS trilha_panda.bi_pessoas OPTIONS (PATH 'dbfs:/databricks-datasets/learning-spark-v2/people/people-10m.delta')

# COMMAND ----------

df = spark.read.table('trilha_panda.bi_pessoas')

# COMMAND ----------

# corrige nomes e adiciona termos natureza
df = df.withColumnRenamed()

# COMMAND ----------

# escreve no synapse, schema 'trilha_panda'

# COMMAND ----------

#noqa
