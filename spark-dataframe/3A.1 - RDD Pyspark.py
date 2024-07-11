# Databricks notebook source
# MAGIC %md #RDD
# MAGIC
# MAGIC Em um alto nível, toda aplicação Spark consiste em um programa direcionador que executa, no cluster, as funções principais do usuário e, em paralelo, várias outras operações. A abstração principal fornecida pelo Spark é um _Resilient Distributed Dataset_ (RDD), que é uma coleção de elementos, tolerantes à falhas, distribuidos através dos nós de um cluster que podem ser executadas em paralelo.
# MAGIC
# MAGIC A primeira coisa que um programa Spark deve fazer é criar um objeto _SparkContext_, que informa ao Spark como acessar um cluster. Para criar um SparkContext, primeiro você precisa criar um objeto SparkConf que contenha informações sobre seu aplicativo. Aqui no databricks não é preciso fazer isso, pois já está setado como default.

# COMMAND ----------

#Criando um RDD através do método sc (SparkContext) e da função parallelize().
numeros = sc.parallelize([1,2,3,4,5,6,7,8,9,10])
# A partir desse momento, o RDD numeros pode ser utilizado para executar ações em paralelo.

# COMMAND ----------

#Executação uma ação através do método take()
numeros.take(5) #5 primeiros

# COMMAND ----------

# MAGIC %md #Operações com RDDs
# MAGIC
# MAGIC RDDs suportam dois tipos de operações:
# MAGIC - **Transformations**, as quais criam um novo Dataset de um já existente.
# MAGIC - **Actions**, as quais retornam um valor ao programa executor depois de executar operação(ções) no Dataset, e esse retorno pode ser armazenado.
# MAGIC
# MAGIC
# MAGIC Todas as transformações no Spark são lentas, pois não computam seus resultados imediatamente. Em vez disso, eles apenas armazenam em memória as transformações aplicadas a algum conjunto de dados básico. As transformações são computadas apenas quando uma _Action_ requer que um resultado seja retornado ao programa executor. Esse design permite que **o Spark seja executado com mais eficiência**.
# MAGIC Por padrão, cada RDD transformado pode ser recalculado toda vez que você executar uma _action_ nele. No entanto, você também pode persistir um RDD na memória usando o método persist (ou cache), caso em que o Spark manterá os elementos no cluster para um acesso muito mais rápido na próxima vez que você o consultar. 

# COMMAND ----------

# MAGIC %md ##_Transformations_ mais comuns
# MAGIC
# MAGIC - map(func)	Return a new distributed dataset formed by passing each element of the source through a function func.
# MAGIC - filter(func)	Return a new dataset formed by selecting those elements of the source on which func returns true.
# MAGIC - sample(withReplacement, fraction, seed)	Sample a fraction fraction of the data, with or without replacement, using a given random number generator seed.
# MAGIC - union(otherDataset)	Return a new dataset that contains the union of the elements in the source dataset and the argument.
# MAGIC - intersection(otherDataset)	Return a new RDD that contains the intersection of elements in the source dataset and the argument.  
# MAGIC - distinct([numPartitions]))	Return a new dataset that contains the distinct elements of the source dataset.
# MAGIC - groupByKey([numPartitions])	When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable<V>) pairs.
# MAGIC - aggregateByKey(zeroValue)(seqOp, combOp, [numPartitions])	When called on a dataset of (K, V) pairs, returns a dataset of (K, U) pairs where the values for each key are aggregated using the given combine functions and a neutral "zero" value. 
# MAGIC - sortByKey([ascending], [numPartitions])	When called on a dataset of (K, V) pairs where K implements Ordered, returns a dataset of (K, V) pairs sorted by keys in ascending or descending order, as specified in the boolean ascending argument.
# MAGIC - join(otherDataset, [numPartitions])	When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin.
# MAGIC - cartesian(otherDataset)	When called on datasets of types T and U, returns a dataset of (T, U) pairs (all pairs of elements).
# MAGIC - coalesce(numPartitions)	Decrease the number of partitions in the RDD to numPartitions. Useful for running operations more efficiently after filtering down a large dataset.
# MAGIC - repartition(numPartitions)	Reshuffle the data in the RDD randomly to create either more or fewer partitions and balance it across them. This always shuffles all data over the network.

# COMMAND ----------

# MAGIC %md ##_Actions_ mais comuns
# MAGIC
# MAGIC - 

# COMMAND ----------

numeros.top(5) #Os 5 maiores

# COMMAND ----------

numeros.collect() #O Dataset inteiro.

# COMMAND ----------

numeros.count() #Conta a quantidade de elementos no Dataset.

# COMMAND ----------

numeros.mean() #Calcula a média dos elementos numéricos

# COMMAND ----------

numeros.sum() #A soma de todos os elementos

# COMMAND ----------

numeros.max() #O elemento de maior valor numérico

# COMMAND ----------

numeros.min() # O elemento de menor valor numérico

# COMMAND ----------

numeros.stdev() #O desvio padrão de todo o Dataset.

# COMMAND ----------

filtros = numeros.filter(lambda filtros: filtros >2)

# COMMAND ----------

filtros.collect()

# COMMAND ----------

amostra = numeros.sample(True, 0.5, 1)

# COMMAND ----------

amostra.collect()

# COMMAND ----------

mapa = numeros.map(lambda mapa: mapa * 2)

# COMMAND ----------

mapa.collect()

# COMMAND ----------

numeros2 = sc.parallelize([6,7,8,9,10])

# COMMAND ----------

uniao = numeros.union(numeros2)

# COMMAND ----------

uniao.collect()

# COMMAND ----------

#Elementos em comun
interseccao = numeros.intersection(numeros2)

# COMMAND ----------

interseccao.collect()

# COMMAND ----------

#Diferença entre os rdds
subtrai = numeros.subtract(numeros2)
subtrai.collect()

# COMMAND ----------

cartesiano = numeros.cartesian(numeros2)
cartesiano.collect()

# COMMAND ----------

cartesiano.countByValue()

# COMMAND ----------

compras = sc.parallelize([(1, 200), (2, 300), (3, 120), (4, 250), (5, 78)])

# COMMAND ----------

chaves = compras.keys()
chaves.collect()

# COMMAND ----------

valores = compras.values()
valores.collect()

# COMMAND ----------

compras.countByKey()

# COMMAND ----------

soma = compras.mapValues(lambda soma: soma + 1)
soma.collect()

# COMMAND ----------

debitos = sc.parallelize([(1, 20), (2, 300), (3, 120), (4, 250), (5, 78)])

# COMMAND ----------

# MAGIC %md #RDD
# MAGIC Uma **segunda abstração** no Spark são as _Shared Variables_ (variáveis compartilhadas) que podem ser usadas em operações paralelas. Por padrão, quando o Spark executa uma função em paralelo como, por exemplo, um conjunto de tarefas em nós diferentes, o Spark envia uma cópia de cada variável usada na função para cada tarefa. Às vezes, uma variável precisa ser compartilhada por várias tarefas, ou entre tarefas, e o programa executor. O Spark oferece suporte a dois tipos de variáveis compartilhadas: variáveis de _broadcast_ (transmissão), que podem ser usadas para armazenar em cache um valor na memória em todos os nós, e variáveis _accumulators_ (acumuladoras), que são variáveis que são apenas “adicionadas”, como contadores e somas.

# COMMAND ----------

#noqa
