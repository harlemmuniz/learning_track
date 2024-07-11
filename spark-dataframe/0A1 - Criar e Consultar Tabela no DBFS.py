# Databricks notebook source
# MAGIC %md
# MAGIC ### Criar e Consultar Tabela no DBFS
# MAGIC **Visão geral**
# MAGIC
# MAGIC DBFS significa "Distributed File System" ou Sistema de Arquivos Distribuído, em português. 
# MAGIC
# MAGIC [DBFS](https://docs.databricks.com/user-guide/dbfs-databricks-file-system.html) é um sistema de arquivos Databricks que permite armazenar dados para consulta dentro do Databricks. Este notebook pressupõe que você já tenha um arquivo dentro do DBFS do qual gostaria de ler.
# MAGIC
# MAGIC Será mostrado como criar e consultar uma tabela ou DataFrame que você carregou no DBFS.
# MAGIC
# MAGIC Este notebook é escrito em **Python** para que o tipo de célula padrão seja Python. No entanto, você pode usar idiomas diferentes usando a sintaxe %LANGUAGE. Python, Scala, SQL e R são todos suportados.

# COMMAND ----------

# MAGIC %md
# MAGIC **Exemplo: Criar e Consultar Tabela no DBFS**

# COMMAND ----------

# Local e tipo de arquivo
file_location = "/FileStore/tables/data.csv"
file_type = "csv"

# Opções do CSV
infer_schema = "true" # identifica o tipo de variáveis das colunas
first_row_is_header = "true" # identifica a primeira linha como cabeçalho
delimiter = ";" # define o delimitador
# As opções aplicadas são para arquivos CSV. Para outros tipos de arquivo, eles serão ignorados.

# Procedimento para a leitura de um arquivo.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)

# COMMAND ----------

# Create a view or table (Criar um modo de exibição ou tabela)

temp_table_name = "data_csv"

df.createOrReplaceTempView(temp_table_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Consultar a tabela temporária criada em uma célula SQL */
# MAGIC
# MAGIC select * from `data_csv`

# COMMAND ----------

# Com isso registrado como uma visualização temporária, ele só estará disponível para este notebook específico. Se você quiser que outros usuários possam consultar essa tabela, também poderá criar uma tabela a partir do DataFrame.
# Depois de salva, essa tabela persistirá nas reinicializações do cluster, além de permitir que vários usuários em diferentes notebooks consultem esses dados.
# Para fazer isso, escolha o nome da tabela e remova o comentário da linha de fundo.

permanent_table_name = "data_csv"

# df.write.format("parquet").saveAsTable(permanent_table_name)

# COMMAND ----------

#noqa
