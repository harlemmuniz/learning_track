-- Databricks notebook source
-- MAGIC %md ### SQL - Structured Query Language
-- MAGIC Conceitos básicos
-- MAGIC
-- MAGIC É uma linguagem de programação projetada para gerenciar e manipular dados armazenados em sistemas de gerenciamento de banco de dados relacionais.
-- MAGIC
-- MAGIC BANCO DE DADOS (DATABASE): Um banco de dados é um conjunto organizado de dados armazenados eletronicamente. Pode conter uma ou mais tabelas, índices e outros objetos relacionados.
-- MAGIC
-- MAGIC COLUNA (COLUMN): Cada coluna em uma tabela tem um nome único e representa um atributo específico. Por exemplo, em uma tabela de funcionários, pode haver colunas como "ID", "Nome", "Cargo" etc.
-- MAGIC
-- MAGIC REGISTRO (ROW): Um registro é uma entrada única em uma tabela. Cada registro contém dados relacionados a uma entidade específica na tabela.
-- MAGIC
-- MAGIC CHAVE PRIMÁRIA (PRIMARY KEY): Uma chave primária é uma coluna ou conjunto de colunas em uma tabela que identifica de forma exclusiva cada registro na tabela. Ela é usada para garantir a integridade dos dados e facilitar a busca rápida.
-- MAGIC
-- MAGIC CHAVE ESTRANGEIRA (FOREIN KEY): Uma chave estrangeira é uma coluna em uma tabela que se relaciona com a chave primária de outra tabela. Isso estabelece uma ligação entre as duas tabelas.
-- MAGIC
-- MAGIC CONSULTA (QUERY): Uma consulta é um comando SQL usado para extrair dados específicos de uma ou mais tabelas. As consultas são usadas para recuperar, inserir, atualizar ou excluir dados no banco de dados.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md ### Instruções SQL Básico:
-- MAGIC SELECT: Usado para recuperar dados de uma ou mais tabelas.
-- MAGIC
-- MAGIC         Ex.: SELECT coluna1, coluna2 FROM tabela WHERE condição;
-- MAGIC
-- MAGIC INSERT: Usado para inserir novos registros em uma tabela.
-- MAGIC
-- MAGIC         Ex.: INSERT INTO tabela (coluna1, coluna2) VALUES (valor1, valor2);
-- MAGIC
-- MAGIC UPDATE: Usado para atualizar dados existentes em uma tabela.
-- MAGIC
-- MAGIC         Ex.: UPDATE tabela SET coluna1 = novo_valor WHERE condição;
-- MAGIC
-- MAGIC DELETE: Usado para excluir registros de uma tabela.
-- MAGIC
-- MAGIC         Ex.: DELETE FROM tabela WHERE condição;
-- MAGIC
-- MAGIC WHERE: Utilizado para filtrar resultados com base em uma condição específica.
-- MAGIC
-- MAGIC         Ex.: SELECT coluna1, coluna2 FROM tabela WHERE coluna1 = 'valor';

-- COMMAND ----------

-- No SQL, ao iniciar um trecho de código utilizando -- (dois traços), esse trecho não será interpretado pelo compilador, ou seja, essa é uma forma de comentar, descrevendo algo, ou simplesmente, um forma de ignorar algum trecho de código.

-- COMMAND ----------

-- Selecionando todos os dados da tabela "selic"
SELECT * FROM selic;

-- COMMAND ----------

-- MAGIC %md ### Cláusulas: 
-- MAGIC
-- MAGIC Partes opcionais de uma instrução SQL que fornecem condições, restrições ou ordens específicas. 
-- MAGIC
-- MAGIC         Exemplos incluem WHERE, ORDER BY, GROUP BY.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### WHERE:
-- MAGIC
-- MAGIC A cláusula WHERE é usada para filtrar os resultados de uma consulta, permitindo que você especifique uma condição para restringir as linhas retornadas. 
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

SELECT * FROM selic 
  WHERE data > '2020-01-01'

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### ORDER BY:
-- MAGIC
-- MAGIC A cláusula ORDER BY é usada para classificar os resultados de uma consulta com base em uma ou mais colunas, em ordem ascendente (ASC) ou descendente (DESC).
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

SELECT * FROM selic 
  ORDER BY data ASC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### GROUP BY:
-- MAGIC
-- MAGIC A cláusula GROUP BY é usada para agrupar linhas que têm os mesmos valores em determinadas colunas, geralmente para serem usadas com funções de agregação, como COUNT, SUM, AVG.
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

SELECT data, COUNT(*)
FROM selic 
GROUP BY data

-- COMMAND ----------

-- MAGIC %md ###DESCRIBE ou DESC
-- MAGIC
-- MAGIC Utilizado em SQL para obter informações sobre a estrutura de uma tabela, incluindo os nomes das colunas, tipos de dados e outras propriedades.
-- MAGIC
-- MAGIC Esses comandos são úteis para obter uma visão rápida da estrutura de uma tabela, especialmente quando você está explorando um novo banco de dados ou trabalhando com tabelas desconhecidas. Eles retornam informações sobre as colunas, tipos de dados, chaves primárias, e outras propriedades da tabela. Vale notar que a disponibilidade desses comandos pode variar entre os diferentes sistemas de gerenciamento de banco de dados.
-- MAGIC

-- COMMAND ----------

DESCRIBE selic

-- COMMAND ----------

DESC selic
