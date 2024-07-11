-- Databricks notebook source
-- MAGIC %md ### SQL - Structured Query Language
-- MAGIC Conceitos avançados
-- MAGIC
-- MAGIC No nível avançado do SQL, os conceitos e comandos se tornam mais sofisticados, permitindo uma manipulação mais fina e um melhor desempenho em ambientes complexos.
-- MAGIC
-- MAGIC Eles proporcionam maior controle sobre o banco de dados, melhor desempenho e modularidade em ambientes complexos de gerenciamento de dados. A aplicação desses conceitos exige um entendimento profundo dos requisitos do sistema e das características específicas do banco de dados utilizado.
-- MAGIC
-- MAGIC

-- COMMAND ----------

-- MAGIC %md ### Instruções SQL Avançado:
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Chave Estrangeira:
-- MAGIC
-- MAGIC Uma chave estrangeira é uma coluna em uma tabela que se refere à chave primária de outra tabela, estabelecendo um relacionamento entre elas.
-- MAGIC
-- MAGIC Exemplo:

-- COMMAND ----------

CREATE TABLE pedidos (
  id INT PRIMARY KEY,
  cliente_id INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- COMMAND ----------

-- MAGIC %md ### Transações:
-- MAGIC
-- MAGIC Transações garantem que um conjunto de operações no banco de dados seja realizado de maneira completa e consistente, ou então desfeito se ocorrer um erro.
-- MAGIC
-- MAGIC Exemplo:

-- COMMAND ----------

BEGIN TRANSACTION;
UPDATE conta SET saldo = saldo - 100 WHERE cliente_id = 1;
UPDATE conta SET saldo = saldo + 100 WHERE cliente_id = 2;
COMMIT;

-- COMMAND ----------

-- MAGIC %md ### Índices e Otimização:
-- MAGIC
-- MAGIC O uso de índices melhora o desempenho das consultas, tornando a busca de dados mais eficiente.
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

CREATE INDEX idx_nome ON clientes (nome);

-- COMMAND ----------

-- MAGIC %md ### Views:
-- MAGIC
-- MAGIC Views são consultas SQL armazenadas que podem ser referenciadas como tabelas, facilitando consultas complexas e fornecendo uma camada de abstração sobre os dados reais.
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

CREATE VIEW visao_clientes AS
SELECT id, nome FROM clientes WHERE status = 'ativo';

-- COMMAND ----------

-- MAGIC %md ### Stored Procedures e Funções:
-- MAGIC
-- MAGIC Stored Procedures e Funções são blocos de código SQL armazenados no banco de dados, que podem ser chamados e reutilizados.
-- MAGIC
-- MAGIC Exemplo:
-- MAGIC

-- COMMAND ----------

CREATE PROCEDURE sp_atualizar_saldo (IN cliente_id INT, IN valor INT)
BEGIN
  UPDATE conta SET saldo = saldo + valor WHERE cliente_id = cliente_id;
END;
