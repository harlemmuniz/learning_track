# Databricks notebook source
# MAGIC %md # DataFrame
# MAGIC
# MAGIC DataFrames são uma estrutura de dados fundamental no campo da manipulação e análise de dados, comumente usada em linguagens de programação como Python com bibliotecas como o Pandas ou em R. 
# MAGIC É uma estrutura de dados tabular comum a muitas bibliotecas de processamento de dados.
# MAGIC
# MAGIC Um DataFrame pode ser pensado como uma estrutura de dados bidimensional rotulada com colunas de tipos potencialmente diferentes, semelhante a uma planilha ou uma tabela SQL. Isso permite a manipulação, limpeza e análise de dados estruturados de maneira fácil. 

# COMMAND ----------

# MAGIC %md
# MAGIC Os **DataFrames** são objetos bidimensionais, de tamanho variável. **O seu formato é de uma tabela, onde os dados são organizados em linhas e colunas**. Além disso, enquanto podemos pensar a Series como uma única coluna, o DataFrame seria uma união de várias Series sob um mesmo index.
# MAGIC
# MAGIC Elementos-chave de um DataFrame:
# MAGIC
# MAGIC 1. Linhas: Cada linha representa uma única observação ou ponto de dados.
# MAGIC
# MAGIC 2. Colunas: Cada coluna representa uma variável ou característica associada aos dados.
# MAGIC
# MAGIC 3. Rótulos: Tanto as linhas quanto as colunas podem ter rótulos, que podem ser usados para acessar pontos de dados específicos ou realizar operações.
# MAGIC
# MAGIC Os DataFrames fornecem uma maneira versátil de organizar, limpar e analisar dados. Eles suportam várias operações, como indexação, filtragem, agregação, mesclagem e análise estatística. Além disso, os DataFrames podem lidar com valores ausentes e podem ser facilmente exportados para diferentes formatos de arquivo, como CSV, Excel ou banco de dados.

# COMMAND ----------

# DBTITLE 1,Exemplo
# Exemplo simples de um DataFrame em Python usando a biblioteca Pandas:
import pandas as pd

# Criando um DataFrame a partir de um dicionário
dados = {'Nome': ['Alice', 'Bruno', 'Carlos', 'Davi'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['Brasília', 'São Paulo', 'Nova York', 'Chicago']}

df = pd.DataFrame(dados)
print(df)

# No exemplo acima, cada linha corresponde a uma pessoa, e as colunas representam seu nome, idade e cidade. Este DataFrame pode ser facilmente manipulado e analisado usando vários métodos e funções do Pandas.

# COMMAND ----------

# MAGIC %md
# MAGIC ### DataFrame x Manipulação e Análise de dados
# MAGIC
# MAGIC Um DataFrame oferece diversas possibilidades de uso para manipulação e análise de dados.
# MAGIC
# MAGIC Algumas das *ações* que podem ser realizadas incluem:
# MAGIC
# MAGIC **Junção de Tabelas**: É possível unir dois ou mais DataFrames com base em colunas comuns para criar um novo conjunto de dados combinando informações de diferentes fontes.
# MAGIC
# MAGIC **Filtragem e Seleção**: Os DataFrames permitem filtrar dados com base em condições específicas, como valores em colunas, datas, etc. Além disso, você pode selecionar apenas as colunas necessárias para a análise.
# MAGIC
# MAGIC **Agregações e Sumarizações**: É possível realizar operações de agregação, como soma, média, máximo, mínimo, contagem, entre outras, para resumir e analisar grandes conjuntos de dados.
# MAGIC
# MAGIC **Transformações e Limpezas**: Os DataFrames oferecem métodos para transformar dados, como renomear colunas, alterar tipos de dados, lidar com valores nulos e realizar outras operações de limpeza e preparação dos dados para análise.
# MAGIC
# MAGIC **Visualização de Dados**: Com o uso de bibliotecas de visualização, como Matplotlib, Plotly ou Databricks Visualization, é possível criar gráficos e visualizações interativas a partir dos dados do DataFrame. É possível também utilizar os dados obtidos nas manipulações para alimentar painéis em outra plataforma, como o PowerBI. Isso permite integrar a análise e preparação de dados realizada no Databricks com a criação de dashboards e relatórios mais elaborados em ferramentas especializadas em visualização de dados. Essa integração é bastante útil para criar insights e comunicar informações de forma eficaz para diferentes públicos dentro de uma organização.
# MAGIC
# MAGIC **Análise Exploratória de Dados (EDA)**: Os DataFrames são úteis para realizar análises exploratórias de dados, como identificação de padrões, tendências, outliers e insights preliminares sobre os dados.
# MAGIC
# MAGIC **Integração com Outras Ferramentas**: Os DataFrames podem ser integrados com outras ferramentas e serviços no ecossistema Databricks, como MLflow para gerenciamento de fluxos de trabalho de aprendizado de máquina e Delta Lake para armazenamento e versionamento de dados.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exemplos
# MAGIC
# MAGIC Exemplos em Python utilizando a biblioteca Pandas para demonstrar algumas das possibilidades de ações que mencionamos anteriormente.

# COMMAND ----------

# DBTITLE 1,Exemplo de Junção de Tabelas
# Exemplo de Junção de Tabelas

import pandas as pd

# Criar dois DataFrames de exemplo
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Idade': [25, 30, 35]})

# Realizar a junção dos DataFrames com base na coluna 'ID'
df_merged = pd.merge(df1, df2, on='ID')

print(df_merged)

# COMMAND ----------

# DBTITLE 1,Exemplo de Filtragem e Seleção
# Exemplo de Filtragem e Seleção

# Filtrar registros com idade maior que 25
df_filtered = df_merged[df_merged['Idade'] > 25]

print(df_filtered)

# COMMAND ----------

# DBTITLE 1,Exemplo de Agregações e Sumarizações
# Exemplo de Agregações e Sumarizações

# Calcular a média de idade
media_idade = df_filtered['Idade'].mean()

print("Média de idade:", media_idade)

# COMMAND ----------

# DBTITLE 1,Exemplo de Transformações e Limpezas
# Exemplo de Transformações e Limpezas

# Renomear coluna 'Nome' para 'Nome Completo'
df_filtered.rename(columns={'Nome': 'Nome Completo'}, inplace=True)

print(df_filtered)

# COMMAND ----------

# Exemplo de Transformações e Limpezas

# Renomear coluna 'Nome Completo' para 'Nome'
df_filtered.rename(columns={'Nome Completo': 'Nome'}, inplace=True)

print(df_filtered)

# COMMAND ----------

# DBTITLE 1,Exemplo de Visualização de Dados
# Exemplo de Visualização de Dados

import matplotlib.pyplot as plt

# Criar um gráfico de barras com a contagem de registros por idade
df_filtered['Idade'].value_counts().plot(kind='bar')
plt.xlabel('Idade')
plt.ylabel('Quantidade')
plt.title('Contagem de Registros por Idade')
plt.show()

# COMMAND ----------

# DBTITLE 1,Exemplo de Integração com Outras Ferramentas
# Exemplo de Integração com Outras Ferramentas

# Exportar DataFrame filtrado para um arquivo CSV
df_filtered.to_csv('dados_filtrados.csv', index=False)

# Neste exemplo o arquivo 'dados_filtrados.csv' é disponibilizado no diretório de trabalho atual, ou seja, o arquivo será salvo no diretório onde o notebook está localizado, a menos que você especifique um caminho absoluto para o arquivo. Você pode verificar isso navegando para o diretório onde você abriu o notebook no sistema de arquivos.

# COMMAND ----------

# MAGIC %md
# MAGIC Nesses exemplos, cada ação é demonstrada de forma isolada para facilitar a compreensão. No contexto real de um projeto de análise de dados, essas ações podem ser combinadas e aplicadas em sequência para realizar análises mais complexas e obter insights valiosos. Os comentários no código ajudam a explicar cada etapa e seu propósito.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Função .merge()
# MAGIC
# MAGIC A função pd.merge() é utilizada para combinar DataFrames com base em colunas comuns. Ela realiza operações de junção semelhantes às operações de join em bancos de dados relacionais.
# MAGIC
# MAGIC Ao usar pd.merge(), você especifica as colunas pelas quais deseja unir os DataFrames e o tipo de junção (por exemplo, inner join, left join, right join, outer join).
# MAGIC
# MAGIC O resultado é um novo DataFrame que contém as colunas dos DataFrames originais combinados com base nas colunas especificadas na junção.

# COMMAND ----------

# DBTITLE 1,Exemplo de junção de tabelas com função pd.merge()
# Exemplo de junção de tabelas usando a função pd.merge()
 
import pandas as pd

# Criar os DataFrames de exemplo
df_clientes = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Charlie'], 'Saldo': [1000, 2000, 1500]})
df_transacoes = pd.DataFrame({'ID': [1, 2, 3, 1], 'Valor': [500, 1000, 700, 200]})

# Realizar a junção das tabelas com base na coluna 'ID'
df_joined = pd.merge(df_clientes, df_transacoes.groupby('ID')['Valor'].sum().reset_index(), on='ID')

# Renomear a coluna resultante da soma
df_joined.rename(columns={'Valor': 'Total_Transacoes'}, inplace=True)

print(df_joined)

# Neste exemplo, temos duas tabelas: df_clientes com informações dos clientes, incluindo o saldo, e df_transacoes com as transações dos clientes. Após a junção das tabelas, utilizamos a função groupby e sum para calcular a soma das transações agrupadas por ID e, em seguida, renomeamos a coluna resultante para Total_Transacoes no DataFrame final df_joined.

# A saída será um novo DataFrame contendo as informações dos clientes e a coluna adicional Total_Transacoes que mostra a soma das transações para cada cliente.

# COMMAND ----------

# MAGIC %md
# MAGIC O exemplo que fornecido acima é um exemplo de **junção de tabelas**, que é comumente conhecido como **"join"** em bancos de dados e em manipulação de dados em geral. No exemplo, utilizamos a **função pd.merge() do Pandas** para realizar a junção dos DataFrames df_clientes e df_transacoes com base na coluna 'ID'.
# MAGIC
# MAGIC Especificamente, *utilizamos um tipo de junção chamado de* **"inner join"**, que é o padrão utilizado pelo Pandas quando você não especifica explicitamente o tipo de join. Nesse tipo de join, apenas os registros que possuem valores correspondentes nas duas tabelas são incluídos no DataFrame resultante.
# MAGIC
# MAGIC O resultado é um novo DataFrame df_joined que contém as informações dos clientes e a coluna adicional Total_Transacoes, que representa a soma das transações para cada cliente. 
# MAGIC
# MAGIC **Essa junção é útil para combinar dados de diferentes fontes e realizar análises mais abrangentes sobre os dados relacionados.**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Método .groupby()
# MAGIC
# MAGIC O método .groupby() é utilizado para agrupar dados com base em valores específicos de uma ou mais colunas. Ele permite realizar operações de agregação em grupos de dados.
# MAGIC
# MAGIC Ao usar .groupby(), você especifica a(s) coluna(s) pelas quais deseja agrupar os dados. Em seguida, você pode aplicar funções de agregação, como soma, média, contagem, máximo, mínimo, entre outras, aos grupos de dados resultantes.
# MAGIC
# MAGIC O resultado é um objeto GroupBy que pode ser combinado com funções de agregação para gerar um novo DataFrame com os resultados agregados.

# COMMAND ----------

# DBTITLE 1,Exemplo de junção de tabelas com método .groupBy()
# Exemplo de junção de tabelas usando o método .groupBy()

import pandas as pd

# Criar o DataFrame de exemplo
df_transacoes = pd.DataFrame({'Cliente': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
                              'Valor': [500, 1000, 700, 300, 800]})

# Agrupar as transações por cliente e calcular a soma dos valores
df_agrupado = df_transacoes.groupby('Cliente')['Valor'].sum().reset_index()

print(df_agrupado)

# COMMAND ----------

# MAGIC %md
# MAGIC No exemplo que foi fornecido acima temos um DataFrame df_transacoes com informações de transações de diferentes clientes. Ao usar *'.groupby('Cliente')['Valor'].sum().reset_index()'*, estamos realizando as seguintes operações:
# MAGIC
# MAGIC Agrupando as transações por cliente usando a coluna 'Cliente'.
# MAGIC
# MAGIC Calculando a soma dos valores das transações para cada cliente.
# MAGIC
# MAGIC Usando reset_index() para redefinir o índice do DataFrame resultante para que ele tenha um índice padrão.
# MAGIC
# MAGIC O resultado será um novo DataFrame df_agrupado que contém as somas das transações por cliente.
# MAGIC
# MAGIC Isso demonstra como o **.groupby()** pode ser usado de forma independente para agrupar e realizar operações de agregação em dados sem a necessidade de usar o **.merge()**.

# COMMAND ----------

# MAGIC %md
# MAGIC De forma geral, **pd.merge()** é usado para combinar DataFrames com base em colunas comuns, enquanto **.groupby()** é usado para agrupar dados e realizar operações de agregação dentro desses grupos.
# MAGIC
# MAGIC Ambos são fundamentais na manipulação e análise de dados em Python, mas têm finalidades distintas.
