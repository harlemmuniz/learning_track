# Databricks notebook source
# MAGIC %md
# MAGIC # Usando SQL no Databricks

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criando uma tabela

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Lista todos os bancos de dados disponíveis
# MAGIC SHOW DATABASES

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criando um database

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS teste

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criando uma tabela

# COMMAND ----------

# MAGIC %sql
# MAGIC USE teste

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE trilha_panda.usuarios_teste(
# MAGIC   idade int,
# MAGIC   estado string,
# MAGIC   salario float
# MAGIC )
# MAGIC   -- ROW FORMAT DELIMITED 
# MAGIC   --   FIELDS TERMINATED BY ','
# MAGIC   --   LINES TERMINATED BY '\n'
# MAGIC   -- STORED AS textfile
# MAGIC   -- LOCATION '/FileStore/tables/trilha_panda/usuarios/'

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC   FROM trilha_panda.usuarios_teste

# COMMAND ----------

# MAGIC %md
# MAGIC ### Inserindo registros em uma tabela

# COMMAND ----------

# DBTITLE 1,Inserir dados na tabela
# MAGIC %sql
# MAGIC INSERT INTO trilha_panda.usuarios_teste VALUES (25, 'SP', 5000)

# COMMAND ----------

# DBTITLE 1,Consulta tabela
# MAGIC %sql
# MAGIC SELECT *
# MAGIC   FROM usuarios_teste

# COMMAND ----------

# DBTITLE 1,Excluir linha de registros da tabela
# MAGIC %sql
# MAGIC DELETE FROM trilha_panda.usuarios_teste
# MAGIC WHERE idade = 25
# MAGIC   --AND cidade = 'SP'
# MAGIC   --AND salario = 5000;

# COMMAND ----------

# DBTITLE 1,Remover tabela
# MAGIC %sql
# MAGIC DROP TABLE usuarios;

# COMMAND ----------

# MAGIC %md
# MAGIC **DROP TABLE**
# MAGIC
# MAGIC O comando DROP TABLE é usado para excluir permanentemente uma tabela do banco de dados.
# MAGIC Quando se executa **DROP TABLE usuarios;**, a tabela chamada 'usuarios' e todos os seus dados são removidos do banco de dados de forma irreversível.
# MAGIC Este comando não apenas remove os dados da tabela, mas também remove a própria estrutura da tabela, ou seja, todas as colunas, índices, restrições e outros elementos relacionados à tabela são excluídos.
# MAGIC É importante ter cuidado ao usar DROP TABLE, pois não há como desfazer essa operação e todos os dados da tabela serão perdidos permanentemente.

# COMMAND ----------

# MAGIC %sql
# MAGIC TRUNCATE TABLE usuarios;

# COMMAND ----------

# MAGIC %md
# MAGIC **TRUNCATE TABLE**
# MAGIC
# MAGIC O comando TRUNCATE TABLE é usado para remover todos os registros de uma tabela, mas mantém a estrutura da tabela intacta.
# MAGIC Ao executar **TRUNCATE TABLE usuarios;**, todos os dados na tabela 'usuarios' são apagados, mas a definição da tabela, incluindo colunas, índices e restrições, permanece.
# MAGIC O TRUNCATE TABLE é mais rápido do que **DELETE FROM tabela;**, pois não gera logs de transação para cada linha removida, o que pode ser útil em situações em que você precisa remover todos os dados de uma tabela de forma eficiente.
# MAGIC No entanto, ao contrário do DROP TABLE, o TRUNCATE TABLE não pode ser usado para excluir a estrutura da tabela; ele só pode ser usado para remover os dados dentro dela.
