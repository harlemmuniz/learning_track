-- Databricks notebook source
-- MAGIC %md ### SQL - Structured Query Language
-- MAGIC Conceitos intermediários
-- MAGIC
-- MAGIC No nível intermediário do SQL, os conceitos e comandos se expandem para permitir uma manipulação mais sofisticada e eficiente dos dados.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md ### Instruções SQL Intermediário:
-- MAGIC
-- MAGIC Os conceitos intermediários permitem que se faça consultas mais complexas, agregue dados de diferentes fontes e organize os resultados de maneira mais sofisticada. Isso é fundamental para lidar com conjuntos de dados mais extensos e realizar análises mais avançadas em um banco de dados relacional.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Funções Agregadas: 
-- MAGIC
-- MAGIC Funções como COUNT, SUM, AVG, MAX, MIN, que são usadas para realizar operações em conjuntos de dados.

-- COMMAND ----------

-- MAGIC %md ###COUNT
-- MAGIC
-- MAGIC A função COUNT é usada para contar o número de linhas em um conjunto de resultados. Pode ser aplicada a uma coluna específica ou a todo o conjunto de resultados.
-- MAGIC
-- MAGIC Exemplo:

-- COMMAND ----------

SELECT COUNT(*) FROM selic;

-- COMMAND ----------

-- MAGIC %md ###SUM
-- MAGIC
-- MAGIC A função SUM é utilizada para calcular a soma dos valores em uma coluna numérica.
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

SELECT SUM(valor) FROM tabela;

-- COMMAND ----------

-- MAGIC %md ###AVG
-- MAGIC
-- MAGIC A função AVG calcula a média dos valores em uma coluna numérica.
-- MAGIC
-- MAGIC Exemplo:

-- COMMAND ----------

SELECT AVG(nota) FROM alunos;

-- COMMAND ----------

-- MAGIC %md ###MAX
-- MAGIC
-- MAGIC A função MAX retorna o valor máximo em uma coluna.
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

SELECT MAX(salario) FROM funcionarios;

-- COMMAND ----------

-- MAGIC %md ###MIN
-- MAGIC
-- MAGIC A função MIN retorna o valor mínimo em uma coluna.
-- MAGIC
-- MAGIC Exemplo:

-- COMMAND ----------

SELECT MIN(estoque) FROM produtos;

-- COMMAND ----------

select min(data) as inicio, max(data) as fim from selic

-- COMMAND ----------

desc selic

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Fazer script SQL para obter o menor e maior valor por ano
