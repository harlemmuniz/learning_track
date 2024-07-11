# Databricks notebook source
# MAGIC %md
# MAGIC ## Widgets
# MAGIC Os "widgets" são componentes interativos utilizados em notebooks de desenvolvimento, como o Azure Databricks. 
# MAGIC
# MAGIC Eles permitem criar interfaces gráficas simples para interagir com o código de forma dinâmica.
# MAGIC
# MAGIC Os widgets nos notebooks do Databricks servem para:
# MAGIC
# MAGIC - Permitir interatividade e visualização dinâmica de resultados.
# MAGIC - Ajustar parâmetros de algoritmos e consultas.
# MAGIC - Criar gráficos interativos e personalizados.
# MAGIC - Personalizar a experiência do usuário.
# MAGIC - Facilitar a comunicação e colaboração entre equipes.
# MAGIC - Agilizar o desenvolvimento e análise de dados.
# MAGIC
# MAGIC Basicamente, utilizamos os Widgets para realizar entrada de parâmetros que serão utilizados no código do notebook.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Tipos de widgets
# MAGIC
# MAGIC Alguns dos widgets comuns que podem ser usados são:
# MAGIC
# MAGIC **Text Box** (Caixa de Texto): Permite aos usuários inserir texto ou números.
# MAGIC
# MAGIC **Dropdown** (Menu Suspenso): Oferece opções selecionáveis em uma lista suspensa.
# MAGIC
# MAGIC **Checkbox** (Caixa de Seleção): Permite selecionar uma ou várias opções em uma lista.
# MAGIC
# MAGIC **Radio Button** (Botão de Seleção): Oferece opções mutuamente exclusivas em forma de botões.
# MAGIC
# MAGIC **Date Picker** (Selecionador de Data): Facilita a seleção de datas em um calendário interativo.
# MAGIC
# MAGIC **Slider** (Controle Deslizante): Permite selecionar um valor em um intervalo especificado.
# MAGIC
# MAGIC **Button** (Botão): Aciona a execução de uma função ou ação específica quando clicado.
# MAGIC
# MAGIC Esses widgets podem ser utilizados para criar interfaces interativas dentro dos notebooks do Azure Databricks, permitindo que os usuários ajustem parâmetros, filtros ou visualizem dados de forma dinâmica durante a análise ou desenvolvimento de código.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exemplos de uso de widgets

# COMMAND ----------

import ipywidgets as widgets

# Criar uma caixa de texto
text_box = widgets.Text(value='Insira seu texto aqui')
text_box

# COMMAND ----------

# Lista de opções para o dropdown
opcoes = ['Opção 1', 'Opção 2', 'Opção 3']

# Criar o dropdown
dropdown = widgets.Dropdown(options=opcoes, value='Opção 1', description='Escolha:')
dropdown

# COMMAND ----------

# Criar caixas de seleção
checkboxes = widgets.Checkbox(value=False, description='Marcar')

# Exibir as caixas de seleção
checkboxes

# COMMAND ----------

# Lista de opções para os botões de seleção
opcoes_radio = ['Opção A', 'Opção B', 'Opção C']

# Criar os botões de seleção
radio_buttons = widgets.RadioButtons(options=opcoes_radio, description='Escolha:')
radio_buttons

# COMMAND ----------

# Criar o selecionador de data
date_picker = widgets.DatePicker(description='Selecione uma data:')
date_picker

# COMMAND ----------

# Criar o controle deslizante
slider = widgets.IntSlider(value=5, min=0, max=10, step=1, description='Valor:')
slider

# COMMAND ----------

# Criar um botão
button = widgets.Button(description='Clique Aqui!')

# Exibir o botão
button

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criar caixa de texto usando widgets
# MAGIC No Azure Databricks, para criar uma caixa de texto usando widgets, você pode usar o módulo **dbutils.widgets**.
# MAGIC
# MAGIC Ao criar as caixas de texto usando widgets, é apresentado no topo do notebook os nome dos campos informados disponíveis para receber dados do usuário. Assim, é possível informar os parâmetros para serem importados no notebook.

# COMMAND ----------

# Criar widgets
dbutils.widgets.text('key', '', '')
dbutils.widgets.text('owner', '', '')
dbutils.widgets.text('table_name', '', '')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Importar widgets

# COMMAND ----------

# MAGIC %md
# MAGIC Após criar os widgets, é possível informar os parâmetros para serem importados.
# MAGIC
# MAGIC Digite os valores desejados e execute o código abaixo para importação. Assim, os dados informados serão atribuídos aos nomes dos atributos, que poderão ser utilizados como partâmetros no código do notebook.

# COMMAND ----------

#import widgets
key = dbutils.widgets.get('key')
owner = dbutils.widgets.get('owner')
table_name = dbutils.widgets.get('table_name')

# COMMAND ----------

# MAGIC %md
# MAGIC Exemplo de comandos para **excluir widgets**.

# COMMAND ----------

# Excluir widgets
dbutils.widgets.remove("key")
dbutils.widgets.remove("owner")
dbutils.widgets.remove("table_name")
