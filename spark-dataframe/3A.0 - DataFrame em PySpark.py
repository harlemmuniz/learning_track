# Databricks notebook source
# MAGIC %md ###DataFrame em PySpark
# MAGIC
# MAGIC Com PySpark, o conceito de DataFrame é muito semelhante ao que foi abordado anteriormente com o Pandas, mas em vez de usar a biblioteca Pandas para manipulação de dados em Python, se utiliza o PySpark, que é uma interface Python para o framework de processamento distribuído Apache Spark.
# MAGIC
# MAGIC Um DataFrame em PySpark é uma estrutura de dados distribuída e imutável que organiza os dados em colunas nomeadas. Ele é construído sobre o conceito de RDDs (Resilient Distributed Datasets) e oferece uma interface mais amigável e eficiente para a manipulação de grandes conjuntos de dados distribuídos em um cluster Spark.
# MAGIC

# COMMAND ----------

# MAGIC %md ###Elementos-chave de um DataFrame em PySpark
# MAGIC
# MAGIC 1. Linhas: Assim como em outras estruturas de DataFrame, as linhas representam observações individuais ou pontos de dados.
# MAGIC
# MAGIC 2. Colunas: As colunas representam variáveis ou características associadas aos dados. Cada coluna tem um nome único e um tipo de dados associado.
# MAGIC
# MAGIC 3. Imutabilidade: Os DataFrames em PySpark são imutáveis, o que significa que, após criados, eles não podem ser modificados. No entanto, pode-se aplicar tranformações para criar novos DataFrames.
# MAGIC
# MAGIC 4. Distribuição: Os DataFrames em PySpark são distribuídos, o que significa que eles podem lidar com grandes volumes de dados, dividindo-os em partições que são processadas em paralelo em um cluster Spark.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md ###Criação e manipulação de DataFrames com PySpark
# MAGIC
# MAGIC A abordagem de criação e manipulação de DataFrames com PySpark pode ser apresentada com as seguintes etapas:
# MAGIC
# MAGIC 1. Importar o módulo PySpark;
# MAGIC 2. Criar DataFrame a partir de fonte de dados;
# MAGIC 3. Manipulação de DataFrame;
# MAGIC 4. Executar ação para obter resultados.
# MAGIC
# MAGIC Essa é uma visão geral básica de como se pode trabalhar com DataFrames usando PySpark.
# MAGIC
# MAGIC Abaixo alguns exemplos.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md ###Importar o módulo PySpark
# MAGIC Primeiro, é preciso importar o módulo PySpark e inicializar uma sessão Spark.

# COMMAND ----------

# DBTITLE 1,Exemplo: Importar o módulo PySpark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Exemplo DataFrame") \
    .getOrCreate()

# COMMAND ----------

# MAGIC %md ###Criar DataFrame a partir de fontes de dados
# MAGIC Pode-se criar um DataFrame em PySpark a partir de diferentes fontes de dados, como arquivos CSV, bancos de dados, RDDs, etc.

# COMMAND ----------

# DBTITLE 1,Exemplo: Criar DataFrame a partir de fontes de dados
# Lendo um arquivo CSV e criando um DataFrame
df = spark.read.csv("caminho/do/arquivo.csv", header=True, inferSchema=True)

# COMMAND ----------

# MAGIC %md ###Manipulação de DataFrame
# MAGIC Depois de criar um DataFrame, você pode aplicar várias operações de manipulação de dados, como seleção, filtragem, agregação, junção, etc.
# MAGIC

# COMMAND ----------

# DBTITLE 1,Exemplo: Manipulação de DataFrame
# Selecionando algumas colunas
df.select("coluna1", "coluna2")

# Filtrando linhas com base em uma condição
df.filter(df["idade"] > 30)

# Realizando uma junção com outro DataFrame
df1.join(df2, df1["coluna_comum"] == df2["coluna_comum"], "inner")


# COMMAND ----------

# MAGIC %md ###Executar ação para obter resultados
# MAGIC Finalmente, após aplicar todas as transformações necessárias, você pode executar uma ação para obter os resultados desejados.

# COMMAND ----------

# DBTITLE 1,Exemplo: Executar ação para obter resultados
# Mostrando os primeiros registros do DataFrame
df.show()

# Salvando o DataFrame em um formato específico
df.write.format("parquet").save("caminho/do/arquivo_parquet")

# COMMAND ----------

# MAGIC %md ###Otimização de Processamento
# MAGIC Uma nota de obervação é de que as operações em DataFrames PySpark são "preguiçosas", o que significa que elas não são executadas imediatamente, mas sim quando uma ação é acionada, permitindo otimizações de processamento.
# MAGIC
# MAGIC No contexto do PySpark, a "preguiça" se refere a um conceito de avaliação tardia (lazy evaluation). Isso significa que as operações em um DataFrame não são executadas imediatamente quando são chamadas, mas são adiadas até que uma ação seja acionada.
# MAGIC
# MAGIC Quando se chama uma transformação em um DataFrame em PySpark, como seleção, filtragem, ou qualquer outra operação, o PySpark simplesmente constrói um plano de execução (execution plan) para essa operação, mas não a executa imediatamente. Isso permite que o PySpark otimize a execução do plano de execução, combinando e reorganizando operações para obter melhor desempenho.
# MAGIC
# MAGIC A execução real das operações ocorre somente quando se chama uma ação em um DataFrame. As ações incluem operações que retornam resultados concretos, como show(), collect(), count(), write(), entre outras. É nesse momento que o PySpark executa o plano de execução que foi construído pelas transformações.
# MAGIC
# MAGIC A abordagem de avaliação tardia é fundamental para a eficiência do processamento distribuído em PySpark, pois permite que ele evite processar dados desnecessários e otimize a execução das operações. Isso torna PySpark adequado para lidar com grandes volumes de dados de forma eficiente em ambientes distribuídos.
