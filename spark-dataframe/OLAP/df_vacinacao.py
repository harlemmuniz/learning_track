# Databricks notebook source
# MAGIC %md ### Geração de entidades para a *Trilha*
# MAGIC
# MAGIC Este notebook servirá como embrião de dados para a trilha da plataforma analítica de dados.
# MAGIC
# MAGIC O objetivo é gerar dados para consumo e aplicação no **PowerBI** e **Metabase**

# COMMAND ----------

df0 = spark.read\
           .option("header", True)\
           .option("delimiter", ';')\
           .csv("/mnt/landed/analytics/trilha_plataforma/power_bi/df_vacinacao/part-00000-47658484-25a7-4665-8b60-d4326886209e.c000.csv")

# COMMAND ----------

df1 = spark.read\
           .option("header", True)\
           .option("delimiter", ';')\
           .csv("/mnt/landed/analytics/trilha_plataforma/power_bi/df_vacinacao/part-00001-47658484-25a7-4665-8b60-d4326886209e.c000.csv")

# COMMAND ----------

df2 = spark.read\
           .option("header", True)\
           .option("delimiter", ';')\
           .csv("/mnt/landed/analytics/trilha_plataforma/power_bi/df_vacinacao/part-00002-47658484-25a7-4665-8b60-d4326886209e.c000.csv")

# COMMAND ----------

df_union = df0.union(df1).union(df2)

# COMMAND ----------

# string de conexão
jdbcUrl = dbutils.secrets.get(scope = 'bbts', key = 'synapse-jdbc-connection-string')

# COMMAND ----------

df_union.write.mode("overwrite").option("truncate",True).jdbc(jdbcUrl, 'analytics'+"."+'trilha_plataforma_df_vacinacao')

# COMMAND ----------

union_synapse = spark.read.jdbc(url=jdbcUrl, table= 'analytics.trilha_plataforma_df_vacinacao')

# COMMAND ----------

union_synapse.count()

# COMMAND ----------

#noqa
