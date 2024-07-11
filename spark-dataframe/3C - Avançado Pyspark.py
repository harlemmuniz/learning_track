# Databricks notebook source
# MAGIC %md ### Resilient Distributed Dataset 
# MAGIC
# MAGIC O RDD é um bloco de construção fundamental do PySpark, que é uma coleção de objetos imutáveis e tolerantes a falhas. 
# MAGIC
# MAGIC Imutável quer dizer que, uma vez que você cria um RDD, você não pode alterá-lo. 
# MAGIC
# MAGIC Cada registro no RDD é dividido em partições lógicas, que podem ser calculadas em diferentes nós do cluster.
# MAGIC
# MAGIC RDDs são uma coleção de objetos semelhantes à lista em Python, com a diferença de que RDD é calculado em vários processos espalhados por vários servidores físicos também chamados de nós em um cluster, enquanto uma coleção Python vive e processa em apenas um.
# MAGIC
# MAGIC Além disso, os RDDs fornecem abstração de dados de particionamento e distribuição dos dados projetados para executar cálculos em paralelo em vários nós, enquanto fazemos transformações em RDD, não precisamos nos preocupar com o paralelismo que o PySpark fornece por padrão.

# COMMAND ----------

# MAGIC %md ### Benefícios do PySpark RDD
# MAGIC O PySpark é amplamente adaptado na comunidade de aprendizado de máquina e ciência de dados devido às suas vantagens em comparação com a programação python tradicional.
# MAGIC
# MAGIC #### Processamento In-Memory
# MAGIC O PySpark carrega os dados do disco e do processo na memória e mantém os dados na memória, esta é a principal diferença entre o PySpark e o Mapreduce. Entre as transformações, também podemos armazenar em cache/persistir o RDD na memória para reutilizar os cálculos anteriores.
# MAGIC
# MAGIC #### Imutabilidade
# MAGIC Os RDDs do PySpark são imutáveis por natureza, uma vez que os RDDs são criados, você não pode modificá-los. Quando aplicamos transformações no RDD, o PySpark cria um novo RDD e mantém a linhagem RDD.
# MAGIC
# MAGIC #### Tolerância ao erro
# MAGIC O PySpark opera em armazenamentos de dados tolerantes a falhas, portanto, qualquer operação RDD falha, ele recarrega automaticamente os dados de outras partições. Além disso, quando as tasks são executados em um cluster, as falhas das tarefas do PySpark são recuperadas automaticamente por um determinado número de vezes (de acordo com a configuração) e concluem o aplicativo perfeitamente.
# MAGIC
# MAGIC #### Lazy
# MAGIC O PySpark não avalia as transformações RDD conforme aparecem pelo Driver, em vez disso, mantém todas as transformações à medida que encontra e avalia todas as transformações quando vê a primeira ação RDD.
# MAGIC
# MAGIC #### Particionamento
# MAGIC Quando você cria um RDD a partir de dados, ele, por padrão, particiona os elementos em um RDD. Por padrão, ele particiona de acordo com o número de núcleos disponíveis.

# COMMAND ----------

# MAGIC %md #### Persistência do  RDD
# MAGIC
# MAGIC Cache e Persist são técnicas de otimização para melhorar o desempenho das tarefas RDD que são iterativas e interativas.
# MAGIC
# MAGIC Embora o PySpark forneça computação 100 x vezes mais rápida do que os trabalhos tradicionais de Map Reduce, se você não tiver projetado os trabalhos para reutilizar os cálculos repetidos, verá uma degradação no desempenho quando estiver lidando com bilhões ou trilhões de dados. Portanto, precisamos olhar para os cálculos e usar técnicas de otimização como uma das maneiras de melhorar o desempenho.
# MAGIC
# MAGIC Usando os métodos cache() e persist(), o PySpark fornece um mecanismo de otimização para armazenar a computação intermediária de um RDD para que possam ser reutilizados em ações subsequentes.
# MAGIC
# MAGIC Quando você persiste ou armazena em cache um RDD, cada nó de trabalho armazena seus dados particionados na memória ou disco e os reutiliza em outras ações nesse RDD. E os dados persistentes do Spark nos nós são tolerantes a falhas, o que significa que se alguma partição for perdida, ela será automaticamente recalculada usando as transformações originais que a criaram.
# MAGIC
# MAGIC #### Vantagens de persistir
# MAGIC * Custo eficiente - os cálculos do PySpark são muito caros, portanto, a reutilização dos cálculos é usada para economizar custos.
# MAGIC * Eficiente em termos de tempo - reutilizar os cálculos repetidos economiza muito tempo.
# MAGIC * Tempo de execução - economiza tempo de execução do trabalho, o que nos permite realizar mais trabalhos no mesmo cluster.

# COMMAND ----------

# MAGIC %md #### Broadcast
# MAGIC Variáveis de broadcast são variáveis somente de leitura que são armazenadas em cache e disponíveis em todos os nós em um cluster para acessar ou usar pelas tarefas. Em vez de enviar esses dados junto com todas as tarefas, o PySpark distribui variáveis de transmissão para a máquina usando algoritmos de transmissão eficientes para reduzir os custos de comunicação.
# MAGIC
# MAGIC Um dos melhores casos de uso do PySpark RDD Broadcast é usar com dados de pesquisa, por exemplo, código postal, estado, pesquisas de país e.t.c
# MAGIC
# MAGIC Quando você executa um trabalho RDD do PySpark que tem as variáveis de transmissão definidas e usadas, o Spark faz o seguinte:
# MAGIC
# MAGIC * O PySpark divide o trabalho em estágios que possuem embaralhamento distribuído e as ações são executadas no estágio.
# MAGIC * As fases posteriores também são divididas em tarefas
# MAGIC * O PySpark transmite os dados comuns (reutilizáveis) necessários para as tarefas em cada estágio.
# MAGIC * Os dados transmitidos são armazenados em cache no formato serializado e desserializados antes de executar cada tarefa.

# COMMAND ----------

# MAGIC %md #### Map reduce

# COMMAND ----------

#noqa
