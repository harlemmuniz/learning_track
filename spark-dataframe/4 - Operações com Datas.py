# Databricks notebook source
# MAGIC %md ### Operações com Datas

# COMMAND ----------

# MAGIC %md
# MAGIC UTC significa Tempo Universal Coordenado, o tempo em vigor em zero graus de longitude, que é usado como horário padrão global para regular o horário e fusos horários. Estamos no UTC-3 (Brasília Time em UTC-03:00).
# MAGIC
# MAGIC Um unixtimestamp representa um instante único, um ponto específico na linha do tempo, e seu valor corresponde a uma determinada quantidade de tempo decorrida a partir de um instante inicial. Esse instante inicial é chamado de *Unix Epoch*, cujo valor é 1970-01-01 00:00:00 (UTC). 
# MAGIC
# MAGIC A representação é feita por meio de uma codificação de 32 bits, podendo ser um número positivo (para instantes que ocorrem depois do Unix Epoch) ou negativo (para instantes anteriores ao Unix Epoch).
# MAGIC
# MAGIC Um detalhe importante é que o mesmo valor de unixtimestamp corresponde a uma data e hora diferente dependendo do fuso horário utilizado.
# MAGIC
# MAGIC > O unixtimestamp 1556322834, por exemplo, representa um instante ocorrido 1.556.322.834 segundos depois do *Unix Epoch* e corresponde às seguintes datas e horários:
# MAGIC
# MAGIC > 26/04/2019, às 20:53:54	em São Paulo
# MAGIC
# MAGIC > 26/04/2019, às 16:53:54	em Los Angeles
# MAGIC
# MAGIC > 27/04/2019, às 08:53:54	em Tóquio
# MAGIC
# MAGIC Este é um conceito importantíssimo: o timestamp 1556322834 corresponde a todas as datas e horas acima. O instante é o mesmo (1.556.322.834 segundos depois do Unix Epoch), o que muda é apenas a data e hora local, de acordo com o fuso-horário que você usa como referência.
# MAGIC
# MAGIC Por isso, só faz sentido converter um timestamp para uma data e hora (e vice-versa) se você estiver usando um fuso-horário específico.
# MAGIC
# MAGIC Usamos a seguinte nomenclatura/formato:
# MAGIC <br>
# MAGIC > Periodo: *YYYY-MM*
# MAGIC <br>
# MAGIC > Data: *YYYY-MM-DD*
# MAGIC <br>
# MAGIC > Timestamp: *YYYY-MM-DD HH:MM:SS*
# MAGIC <br>
# MAGIC > Unixtimestamp: *MMMMMMMMMM*

# COMMAND ----------

# MAGIC %md Em Python você pode usar o módulo **datetime**, que possui vários métodos para se trabalhar com data. 
# MAGIC
# MAGIC <br>
# MAGIC Além disso, você pode usar o módulo **pytz** para configurar o fuso-horário.

# COMMAND ----------

from datetime import datetime
import pytz

# COMMAND ----------

hoje = datetime.now()

hoje = hoje.strftime("%Y-%m-%d")

print("Data /n de hoje:",hoje)

# COMMAND ----------

agora_utc = datetime.now()

agora_utc = agora_utc.strftime("%H:%M:%S")

print("Hora atual:",agora_utc,"(perceba a diferença de fuso)")

# COMMAND ----------

agora = datetime.now(pytz.timezone("Brazil/East"))

agora = agora.strftime("%H:%M:%S")

print("Hora atual em Brasília:",agora)

# COMMAND ----------

# MAGIC %md Vejamos um exemplo de unixtimestamp.

# COMMAND ----------

ano_novo = datetime.fromtimestamp(1641006001, pytz.timezone("Brazil/East"))

print("Ano novo:", ano_novo, "(perceba o carimbo '-03:00')")

# COMMAND ----------

# MAGIC %md Agora veremos como trabalhar com datas em dataframes com PySpark.
# MAGIC
# MAGIC Importaremos vários métodos do módulo pyspark.sql.functions.

# COMMAND ----------

from pyspark.sql.functions import unix_timestamp, from_unixtime, expr, date_format, current_timestamp, to_date, to_timestamp, current_date, lit, hour, col

# COMMAND ----------

# Criamos um dataframe vazio

df = spark.createDataFrame([()], [])

# COMMAND ----------

df = df.withColumn("dt_hoje",current_date()) \
       .withColumn("ts_agora",current_timestamp())

# COMMAND ----------

df.show(truncate=False)

# COMMAND ----------

df = df.withColumn('ts_agora_mais_hora',df.ts_agora + expr('interval 1 hour')) \
       .withColumn('ts_agora_menos_minuto',df.ts_agora + expr('interval -1 minute')) \
       .withColumn('ts_agora_mais_segundo',df.ts_agora + expr('interval 1 second'))

# COMMAND ----------

df.show(truncate=False)

# COMMAND ----------

df = df.withColumn("ts_ano_novo",to_timestamp(lit("2022-01-01 00:00:00")))

# COMMAND ----------

df = df.withColumn("nu_utc_ano_novo",unix_timestamp('ts_ano_novo')) \
       .withColumn("nu_utc_agora",unix_timestamp('ts_agora'))

# COMMAND ----------

df = df.withColumn("nu_segundos_ano_novo",df.nu_utc_agora - df.nu_utc_ano_novo)

# COMMAND ----------

df.select('nu_utc_agora','nu_utc_ano_novo','nu_segundos_ano_novo').show(truncate=False)

# COMMAND ----------

# Em vez de criar variáveis dividindo a quantidade de segundos, podemos usar o método from_unixtime para expressar o tempo decorrido

df = df.withColumn("nu_tempo_ano_novo",from_unixtime('nu_segundos_ano_novo',"HH:mm:ss"))

# COMMAND ----------

df.select('nu_segundos_ano_novo','nu_tempo_ano_novo').show(truncate=False)

# COMMAND ----------

# MAGIC %md 
# MAGIC **Curiosidade:**
# MAGIC
# MAGIC <br>
# MAGIC O que acontecerá em 19 de Janeiro de 2038?
# MAGIC
# MAGIC Nesta data, o unixtimestamp deixará de funcionar devido ao estouro dos 32 bits. Isso porque o intervalo de valores que podem ser armazenados em de 32 bits é de 0 até 4294967295, ou de −2147483648 até 2147483647.
# MAGIC
# MAGIC Antes desse momento, milhões de aplicativos precisarão adotar uma nova convenção para carimbos de data/hora ou migrar para sistemas de 64 bits.
# MAGIC
# MAGIC *Saiba mais*: https://en.wikipedia.org/wiki/Year_2038_problem

# COMMAND ----------

#noqa
