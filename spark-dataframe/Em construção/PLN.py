# Databricks notebook source
# MAGIC %md
# MAGIC #Processamento de Linguagem Natural - PLN
# MAGIC
# MAGIC O PLN é uma área da inteligência artificial que se preocupa com interações entre máquinas e o ser humano. Em particular, em como programar a máquina para processar e analisar uma grande quantidade de dados em linguagem natural, com o intuito de extrair sentido. 
# MAGIC
# MAGIC Para modelar a língua e possibilitar que a máquina a entenda são necessários *pré-processamentos* que abstraiam e estruturem a língua, deixando apenas o que é informação relevante. Esse *pré-processamento* reduz o vocabulário e torna os dados menos esparsos, característica conveniente para o processamento computacional.
# MAGIC
# MAGIC Uma ferramenta bastante útil nesse processo é o NLTK (*Natural Language Toolkit*), que fornece classes básicas para representar dados relevantes para o processamento da linguagem natural.

# COMMAND ----------

# MAGIC %md
# MAGIC Exemplo criado no webinar de janeiro de 2022.

# COMMAND ----------

# MAGIC %pip install nltk
# MAGIC %pip install beautifulsoup4

# COMMAND ----------

import nltk

# COMMAND ----------

#baixa dependencias
nltk.download('punkt')
nltk.download("stopwords")

# COMMAND ----------

#importacoes
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

# COMMAND ----------

#exemplo de tokenizacao de palavras (machado de assis)
print(word_tokenize("Está morto: podemos elogiá-lo à vontade."))

# COMMAND ----------

#exemplo de tokenizacao de sentencas (machado de assis)
print(sent_tokenize("Tempo é um tecido invisível em que se pode bordar tudo, uma flor, um pássaro, uma dama, um castelo, um túmulo. Também se pode bordar nada. Nada em cima de invisível é a mais sutil obra deste mundo, e acaso do outro."))

# COMMAND ----------

#palavras-vazias
print(set(stopwords.words("portuguese")))

# COMMAND ----------

#pontuacoes
print(list(punctuation))

# COMMAND ----------

# MAGIC %md
# MAGIC # Sumarização
# MAGIC
# MAGIC Objetivo: Ler uma notícia da internet e criar um resumo dinamicamente.

# COMMAND ----------

#define url da noticia escolhida
url = 'https://g1.globo.com/pr/norte-noroeste/noticia/2022/02/03/galo-que-foi-preso-apos-cantar-de-madrugada-vira-garoto-propaganda-e-ex-dono-ganha-casa-nova-com-moveis.ghtml'

# COMMAND ----------

#importa urlopen
from urllib.request import urlopen

# COMMAND ----------

#leitura da url
page_html = urlopen(url).read()

# COMMAND ----------

page_html

# COMMAND ----------

#a função abaixo foi postada no chat com o intuito de substituir o processo recursivo mais abaixo (precisa de adequações para implementação)
def remove_tags(html):
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")
  for data in soup(['style', 'script']):
    data.decompose() 
  return ' '.join(soup.stripped_strings)

# COMMAND ----------

def dst_io_get_text_from_notice(html):
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")
  soup.prettify()
  contents_container = soup.findAll("p",{"class":"content-text__container"})
  content_notice = []
  for content_conteiner in contents_container:
    content_notice.append(content_conteiner.text)
  return ' '.join(content_notice)

# COMMAND ----------

texto = dst_io_get_text_from_notice(page_html)

# COMMAND ----------

texto

# COMMAND ----------

def dst_trs_summary_text(text,n):
  
  from nltk.tokenize import word_tokenize
  from nltk.tokenize import sent_tokenize
  from nltk.corpus import stopwords
  from nltk.probability import FreqDist
  from string import punctuation
  from collections import defaultdict
  from heapq import nlargest
  
  #stopwords
  stop_words = set(stopwords.words("portuguese") + list(punctuation))
  #sentencas
  sentencas = sent_tokenize(text)
  #palavras
  palavras = word_tokenize(text.lower())
  #retira stopwords
  palavras_sem_stop_words = [palavra for palavra in palavras if palavra not in stop_words]
  #define dict de sentencas importantes
  sentencas_importantes = defaultdict(int)
  
  #calcula frequencia das palavras sem stopwords
  frequencia = FreqDist(palavras_sem_stop_words)
  
  #define variável resumo
  summary = str()
  
  for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
      if palavra in frequencia:
        sentencas_importantes[i] += frequencia[palavra]
  
  for i in sorted(nlargest(n,sentencas_importantes, sentencas_importantes.get)):
    summary = summary + sentencas[i]
  
  return summary

# COMMAND ----------

resumo = dst_trs_summary_text(texto,4)

# COMMAND ----------

resumo

# COMMAND ----------

#noqa
