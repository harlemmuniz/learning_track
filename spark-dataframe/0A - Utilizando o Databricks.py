# Databricks notebook source
# MAGIC %md
# MAGIC #Utilizando o Databricks

# COMMAND ----------

# MAGIC %md
# MAGIC ### Preparação e execução de código
# MAGIC
# MAGIC Para preparar e executar código em DataFrames e Notebooks no Databricks, o usuário geralmente precisa seguir os seguintes passos:
# MAGIC
# MAGIC **Acesso ao Ambiente Databricks**: O usuário precisa ter acesso ao ambiente Databricks. Isso geralmente envolve ter uma conta configurada e permissões adequadas para acessar os recursos do Databricks.
# MAGIC
# MAGIC **Criar um Cluster**: Antes de executar o código, o usuário precisa criar ou selecionar um cluster no Databricks. Um cluster é uma coleção de máquinas virtuais que serão usadas para executar o código. O tamanho e a configuração do cluster podem ser ajustados conforme necessário, dependendo dos requisitos de processamento do código.
# MAGIC
# MAGIC **Importar Bibliotecas e Pacotes**: Se o código requer bibliotecas ou pacotes específicos que não estão disponíveis por padrão no ambiente Databricks, o usuário precisa importá-los. Isso pode ser feito usando comandos como pip install ou conda install, dependendo do gerenciador de pacotes usado.
# MAGIC
# MAGIC **Carregar e Preparar os Dados**: Se o código envolve a manipulação de dados, o usuário precisa carregar os dados no ambiente Databricks. Isso pode ser feito carregando arquivos diretamente de armazenamentos como Azure Blob Storage, AWS S3, Google Cloud Storage, ou lendo de bancos de dados como SQL Server, PostgreSQL, etc. Após o carregamento dos dados, eles podem precisar ser limpos, transformados ou preparados de acordo com as necessidades do código.
# MAGIC
# MAGIC **Criar ou Importar Notebooks**: O usuário pode criar um novo notebook no Databricks ou importar um existente. *Notebooks* são ambientes interativos onde o código pode ser escrito e executado de forma iterativa. Eles geralmente contêm uma combinação de código, texto explicativo e visualizações.
# MAGIC
# MAGIC **Escrever e Executar o Código**: Com o ambiente configurado e os dados carregados, o usuário pode escrever o código no notebook. Isso pode envolver o uso de linguagens como Python, Scala, SQL ou R, dependendo das preferências e das necessidades do projeto. O código pode incluir operações de transformação de dados, análises estatísticas, machine learning, etc.
# MAGIC
# MAGIC **Monitorar e Depurar**: Durante a execução do código, o usuário pode monitorar o progresso e verificar se há erros ou problemas. O Databricks fornece ferramentas para monitoramento e depuração, como logs de execução e visualizações de desempenho do cluster.
# MAGIC
# MAGIC **Salvar Resultados**: Após a conclusão do código, o usuário pode salvar os resultados, seja em arquivos de saída, bancos de dados, ou integrando com outros serviços e ferramentas para análise posterior ou compartilhamento com colegas.
# MAGIC
# MAGIC **Gerenciar Recursos**: Após a conclusão do trabalho, o usuário pode gerenciar seus recursos, como encerrar o cluster se não estiver mais em uso para evitar custos desnecessários.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Diferença entre Notebook e Dataframe
# MAGIC
# MAGIC Notebook e DataFrame são conceitos distintos, embora frequentemente sejam usados juntos em ambientes de análise de dados como o Databricks.
# MAGIC
# MAGIC **Notebook**: Um notebook é um ambiente interativo onde o código pode ser escrito e executado. Ele consiste em células que podem conter código, texto explicativo ou visualizações. Os notebooks permitem aos usuários escrever e executar código em linguagens como Python, Scala, SQL ou R, facilitando a análise de dados, desenvolvimento de modelos de machine learning, colaboração e documentação.
# MAGIC
# MAGIC **DataFrame**: Um DataFrame é uma estrutura de dados tabular bidimensional, semelhante a uma tabela de banco de dados ou uma planilha do Excel. Ele organiza os dados em linhas e colunas, onde cada coluna representa uma variável e cada linha representa uma observação. DataFrames são comumente usados para manipular e analisar dados em ambientes como o Apache Spark, onde podem lidar com grandes volumes de dados distribuídos de forma eficiente.
# MAGIC
# MAGIC Embora os notebooks e DataFrames sejam frequentemente utilizados juntos para análise de dados, eles representam diferentes aspectos do processo de análise. Os notebooks fornecem o ambiente de execução e interação, enquanto os DataFrames representam os dados que estão sendo analisados e manipulados dentro desse ambiente.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criando tabela no notebook
# MAGIC
# MAGIC Abaixo será apresentado um modelo de como criar uma tabela no Databricks de forma automatizada. É mostrado como ler o arquivo utilizando o Spark e como salvar o dataframe como uma tabela no formato parquet.
# MAGIC É importante configurar corretamente as variáveis *infer_schema*, *first_row_is_header* e *delimiter*.
# MAGIC
# MAGIC Um passo a passo detalhado  para criar a tabela de forma automatizada pode ser consultado no item *0A1*.

# COMMAND ----------

dbutils.fs.rm('/user/hive/warehouse/data_csv', recurse=True)

# Para este procedimento funcionar o arquivo data.csv deve estar carregado no DBFS no endereço especificado na variável `file_location`
file_location = '/FileStore/tables/data.csv'
file_type = 'csv'
infer_schema = 'true'
first_row_is_header = 'true'
delimiter = ';'

df = spark\
    .read\
    .format(file_type)\
    .option('inferSchema', infer_schema)\
    .option('header', first_row_is_header)\
    .option('sep', delimiter)\
    .load(file_location)

table_name = 'data_csv'

df.write.format('parquet').saveAsTable(table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC # Databricks Utilities
# MAGIC
# MAGIC As Databricks Utilities são um conjunto de ferramentas e utilitários fornecidos pelo Databricks para simplificar e aprimorar o desenvolvimento, implantação e monitoramento de aplicativos e análises de dados em sua plataforma. Aqui estão alguns dos principais componentes das Databricks Utilities:
# MAGIC
# MAGIC **dbutils**: O dbutils é uma biblioteca de utilitários integrada ao ambiente Databricks que fornece métodos para acessar e manipular recursos do ambiente de maneira eficiente. Ele oferece funcionalidades para ler e gravar arquivos em sistemas de armazenamento como Azure Blob Storage, AWS S3 e Google Cloud Storage, executar comandos shell, gerenciar configurações e segredos, entre outros. Usado para manipulação de dados do DBFS a partir do notebook.
# MAGIC
# MAGIC **Databricks File System (DBFS)**: O DBFS é um sistema de arquivos distribuído e seguro fornecido pelo Databricks. Ele permite armazenar e acessar arquivos de forma distribuída e escalável dentro do ambiente Databricks. Os utilitários do DBFS podem ser usados por meio do dbutils para ler e gravar arquivos, bem como para gerenciar diretórios e permissões.
# MAGIC
# MAGIC **Widgets**: Os widgets são componentes interativos que podem ser adicionados aos notebooks Databricks para permitir a interação do usuário com o código. Eles podem ser usados para criar controles de entrada, como menus suspensos, caixas de seleção e campos de entrada de texto, que podem ser usados para parametrizar consultas, ajustar hiperparâmetros de modelos de machine learning, entre outras finalidades.
# MAGIC
# MAGIC **Databricks CLI**: O Databricks Command-Line Interface (CLI) é uma ferramenta de linha de comando que permite aos usuários interagir com o ambiente Databricks a partir da linha de comando. Ele fornece comandos para gerenciar clusters, notebooks, jobs, bibliotecas e outros recursos do Databricks. O CLI pode ser usado para automatizar tarefas, integrar com pipelines de CI/CD e realizar operações em massa.
# MAGIC
# MAGIC **Jobs e Agendamento**: Os Jobs são tarefas agendadas que podem ser executadas de forma recorrente no ambiente Databricks. Eles podem ser configurados para executar notebooks, scripts Python ou Spark, permitindo a automação de fluxos de trabalho de análise de dados e processamento de big data. Os utilitários relacionados a jobs permitem criar, agendar, monitorar e gerenciar essas tarefas de forma eficiente.
# MAGIC
# MAGIC No geral, as Databricks Utilities oferecem uma variedade de ferramentas e utilitários que simplificam e automatizam tarefas comuns de desenvolvimento, implantação e monitoramento em ambientes de análise de dados baseados no Databricks. Essas ferramentas ajudam a melhorar a produtividade dos desenvolvedores, otimizar o desempenho dos aplicativos e garantir a segurança e a confiabilidade das operações.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Comandos Databricks Utilities - `dbutils`

# COMMAND ----------

# MAGIC %md
# MAGIC Para executar apenas um comando (Cmd), pressione <'Ctrl'> + <'Enter'>

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %md
# MAGIC Para compreender melhor e ver alguns novos exemplos da utilização do dbutils acesse o [Databricks Utilities](https://docs.databricks.com/pt/dev-tools/databricks-utils.html).
# MAGIC
# MAGIC Nesta página do Databricks Utilities, você terá acesso a informações para aprender a:
# MAGIC - Listar utilitários disponíveis.
# MAGIC - Listar comandos disponíveis para um utilitário.
# MAGIC - Exibir ajuda para um comando.
# MAGIC - Utilizar cada utilitário disponível.
# MAGIC - Acelerar o desenvolvimento de aplicativos com o uso da biblioteca da API Databricks Utilities.
# MAGIC - Lidar com algumas limitações.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Manipulando arquivos

# COMMAND ----------

# MAGIC %md
# MAGIC ### Listar todos os arquivos dentro de uma pasta

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

for item in dbutils.fs.ls('/'):
    print(item.path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Acessando os arquivos carregados no DBFS

# COMMAND ----------

dbutils.fs.ls('/FileStore/')

# COMMAND ----------

dbutils.fs.ls('/FileStore/tables/')

# COMMAND ----------

display(dbutils.fs.ls('/FileStore/tables/'))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Listando as primeiras linhas de um arquivo

# COMMAND ----------

dbutils.fs.head('/FileStore/tables/data.csv')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Removendo arquivos

# COMMAND ----------

dbutils.fs.rm('/FileStore/tables/data.csv')

# COMMAND ----------

dbutils.fs.ls('/FileStore/tables')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Databricks Datasets
# MAGIC ##### [Wine Quality Data Set](http://archive.ics.uci.edu/ml/datasets/wine+quality)
# MAGIC
# MAGIC Abaixo alguns exemplos de uso do Databricks para carregar dados externos e criar tabelas. É apresentado como visualizar os datasets disponíveis, utilizando um código que lista os arquivos na pasta "databricks-datasets". Em seguida, selecionar o dataset de qualidade de vinhos, chamado "wine-quality", e mostrar os arquivos disponíveis nesse dataset. Também é mostrado como visualizar o conteúdo desses arquivos utilizando o comando "dbutils.fs.head()". 
# MAGIC
# MAGIC Nota: Para realizar alterações nos datasets do Databricks é necessário mover os arquivos para uma pasta antes de trabalhar com eles.

# COMMAND ----------

# DBTITLE 1,Listando Arquivos e Diretórios no DBFS
for item in dbutils.fs.ls('/'): print(item.path)

# COMMAND ----------

# DBTITLE 1,Exibindo Conteúdo do Diretório de Datasets no DBFS
display(dbutils.fs.ls('/databricks-datasets'))

# COMMAND ----------

# DBTITLE 1,Exibindo Conteúdo Específico do Diretório de Datasets no DBFS
display(dbutils.fs.ls('/databricks-datasets/wine-quality'))

# COMMAND ----------

# DBTITLE 1,Visualizando o Conteúdo de um Arquivo no DBFS
dbutils.fs.head("/databricks-datasets/wine-quality/README.md")

# COMMAND ----------

# DBTITLE 1,Visualizando o Conteúdo de um Arquivo CSV no DBFS
dbutils.fs.head("/databricks-datasets/wine-quality/winequality-red.csv")

# COMMAND ----------

# DBTITLE 1,Visualizando o Conteúdo de um Arquivo CSV no DBFS
dbutils.fs.head("/databricks-datasets/wine-quality/winequality-white.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Diretórios e arquivos
# MAGIC
# MAGIC Exemplos usando a biblioteca dbutils para lidar com diretórios e arquivos no ambiente Databricks:

# COMMAND ----------

# DBTITLE 1,Listar arquivos em um diretório no DBFS
# dbutils.fs.ls("/path/to/directory")
# dbutils.fs.ls("/data")
dbutils.fs.ls('/FileStore/tables')

# COMMAND ----------

# DBTITLE 1,Criar um diretório no DBFS
# dbutils.fs.mkdirs("/path/to/new_directory")
dbutils.fs.mkdirs('/FileStore/tables/aula-databricks/vinhos')

# COMMAND ----------

# DBTITLE 1,Exibindo Conteúdo do Diretório de Datasets 'aula-databricks'
display(dbutils.fs.ls('/FileStore/tables/aula-databricks'))

# COMMAND ----------

# DBTITLE 1,Remover um arquivo ou diretório do DBFS
# dbutils.fs.rm("/path/to/file_or_directory", recurse=True)
dbutils.fs.rm("/FileStore/tables/aula-databricks/vinhos", recurse=True)

# COMMAND ----------

# DBTITLE 1,Copiar um arquivo do local para o DBFS
dbutils.fs.cp("file:/local/path/to/file", "/dbfs/path/to/destination")

# COMMAND ----------

# DBTITLE 1,Mover um arquivo ou diretório dentro do DBFS
dbutils.fs.mv("/dbfs/path/to/source", "/dbfs/path/to/destination")

# COMMAND ----------

# DBTITLE 1,Ler o conteúdo de um arquivo no DBFS
file_path = "/dbfs/path/to/file"
text_data = dbutils.fs.head(file_path)

# COMMAND ----------

# DBTITLE 1,Escrever dados em um arquivo no DBFS
file_path = "/dbfs/path/to/new_file"
data_to_write = "Hello, Databricks!"
dbutils.fs.put(file_path, data_to_write, overwrite=True)

# COMMAND ----------

# MAGIC %md
# MAGIC Esses são apenas alguns exemplos de operações comuns de manipulação de arquivos e diretórios que podem ser realizadas usando a biblioteca dbutils no ambiente Databricks. Essas funcionalidades são úteis para lidar com dados e arquivos dentro do Databricks, seja para carregar dados, salvar resultados, ou realizar outras operações de manipulação de dados.

# COMMAND ----------

#noqa
