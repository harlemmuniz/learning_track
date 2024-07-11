# Databricks notebook source
# MAGIC %md #Funções
# MAGIC - São estruturas em bloco.
# MAGIC - São executadas quando fazemos "chamadas" às funções.
# MAGIC - São definidas pela palavra reservada def

# COMMAND ----------

#Função de soma
#Somar dois números
def soma(a,b):
  print("O resultado da soma é:", a, " + ", b, " = ", a+b)


#É importante ressaltar que as variáveis(parâmetros) a e b são variáveis(parâmetros) locais. O que quer dizer que elas existem apenas dentro do escopo da **função**.
#Se você tentar utilizar essas variáveis(parâmetros) não será possível. Acusará um erro de variáveis não definidas.
#E caso você declare, fora da função, outras variáveis a e b elas são diferentes das variáveis(parâmetros) da função.

# COMMAND ----------

#Invocando a função soma - certifique-se de executar o comando anterior antes deste.
soma(1,2)

# COMMAND ----------

# MAGIC %md ###Return

# COMMAND ----------

#Para pode utilizar o resultado da função em uma variável, por exemplo, é preciso utilizar o comando return.
#Observe:
def soma(a,b):
  print(a+b)

soma(5,8) #resultado: 13

# COMMAND ----------

#Se tentarmos somar a esse resulta +3, verifique...

# x = soma(5,8) + 3 

#Dá erro. Verifique. Descomente a linha anterior e execute o comando.

# COMMAND ----------

def soma(a,b):
  return a+b

"""Invocando a função soma e armazenando o retorno na variável result_soma"""
result_soma = soma(5,8) + 5 #Adicionando + 5 ao resultado da função soma.

print(result_soma)

#Observe que agora a função retorna um resultado e esse resultado pode ser utilizado da maneira que for necessário.

# COMMAND ----------

# Exemplo
#Resolva a equação 2x2 + 6/3 + 37 + 9x3 - 2^4

#Criando funções
def multiplicacao_equacao(a, b):
  return a*b

def divisao_equacao(a, b):
  return a/b

def exponeciacao_equacao(a,b):
  return 2**4

resultado = multiplicacao_equacao(2,2) + divisao_equacao(6,3) + 37 + multiplicacao_equacao(9,3) - exponeciacao_equacao(2,4)

print(resultado)  #54

# COMMAND ----------

# MAGIC %md #Listas
# MAGIC - É um conjunto de dados que aceita mais de um tipo de dado.

# COMMAND ----------

nomes = ["João", "Pedro", "Maria", "Rita"]
idades = [21, 34, 19, 64, 78]
varios = [True, False, "Antônio", "Isabel", 12, 45, 6.78, 9.99]

#"Caminhando" dentro da lista

print("Terceiro elemento da lista. Índice 2 da lista. -->", nomes[2])
print("Quarto elemento da lista. Índice 3 da lista. -->", nomes[3])
print("Primeiro elemento da lista. Índice 0 da lista. -->", idades[0])
print("Sexto elemento da lista. Índice 5 da lista. -->", varios[5])
print("O último elemento da lista. N - 1. -->", varios[-1])

# COMMAND ----------

#As mesma funções utilizadas em strings podem ser utilizadas em listas.
#Tamanho da lista

tamanho_nomes = len(nomes)
tamanho_idades = len(idades)
tamanho_varios = len(varios)

print(tamanho_nomes)
print(tamanho_idades)
print(tamanho_varios)


# COMMAND ----------

print("Lista nomes dos comandos anterios:", nomes)
#Adicionando itens ao final da lista
nomes.append("Mateus") #Altere o nome e adicione mais à lista.
print("Adicionando Mateus ao final da lista.", nomes)

#Adicionando em uma posição desejada
nomes.insert(0, "Alberto")
print("Adicionando o nome Alberto à primeira posição(0)", nomes)

# COMMAND ----------

# Removendo um item de uma lista
lista_remover = ["Abacaxi", "Amora", "Abacate", "Uva", "Banana", "Caqui"]
print(lista_remover)

lista_remover.pop(3)
print(lista_remover) #Com o nome uva removido na posição de índice 3.

lista_remover.remove("Amora")
print(lista_remover) #Removendo o elemento desejado.

#Se o item não existir vai dar erro e preciso tratar esse erro. Exemplo:
try:
  lista_remover.remove("José")
except ValueError:
  print("Esse elemento não existe")


#Outra maneira de deletar

del lista_remover[1:] #Removendo do elemento de índice 1 até o final.
print(lista_remover)
# Se quiser um intervalo é só definir [1:4] -> Do índice 1 ao 4.
# Se quiser remover a lista toda é só utilizar [:]



# COMMAND ----------

#Verificando se um elemento desejado está na lista
existe_nome = "Pedro"
existe = existe_nome in nomes
print("É", existe, "que existe o nome", existe_nome, "na lista pesquisada.") #Se existir retornará True. Se não existir retornará False.


#Verificando se um elemento desejado está na lista com o if
nome_verificação = "Rita"

if nome_verificação in nomes:
  print(nome_verificação, "está na lista.")



# COMMAND ----------

#É possível criar listas com listas

lista_lista = ["João", 25, ["61999876761", "6133456734"], "SQS 314 Bloco G ap. 201", ["instagram/joao", "linkedin/joao", "face/joao"]]
print(lista_lista)

# COMMAND ----------

#Criando uma lista a partir da método list()
ate_9 = list(range(0,10))

print(ate_9)

#E é possível transformar um string em uma lista utilizando o mesmo método.

string_lista = "BB Tecnologia e Serviços"

lista_string = list(string_lista)
print(lista_string)


# COMMAND ----------

#É replicar o conteúdo de uma lista multiplicando por um número.
lista_a_ser_multiplicada = [1,2,3,4]

lista_multiplicada = lista_a_ser_multiplicada * 3

print(lista_multiplicada)


# COMMAND ----------

#É possível juntar "somando" uma ou mais listas.
ate_4 = [1,2,3,4]
ate_9 = [5,6,7,8,9]
ate_18 = [10,11,12,13,14,15,16,17,18]

result_ate = ate_4 + ate_18 + ate_9

print(result_ate)

# COMMAND ----------

#Se a lista for número é possível saber os máximos, mínimos e soma.
#***Execute o comando anterior
print("Mínimo é", min(result_ate))
print("Máximo é", max(result_ate))
print("Soma é", sum(result_ate))

#É possível ordenar a lista sendo ela numérica ou alfabética.
result_ate.sort(reverse=True) #True é para ordem Decrescente.
#Altere para False e verifique.

print(result_ate)

result_ate.reverse() # Ou esse método para inverter o sentido da lista. Não é em ordem crescente ou decrescente.
print(result_ate)

#O método sort é aplicado à lista, porém, caso precise que isso seja retornado em uma variável para uso, faça o seguinte:
lista_numerica = [34,12,19,9,3,39,45,7,28,8,97,2,4,1,6,5,43,57,89,72,22,63,69,31]
lista_numerica_ordenada = sorted(lista_numerica)
print(lista_numerica_ordenada)


# COMMAND ----------

#Contando a quantidade de elementos desejados de uma lista.
lista_contar = [1,4,1,5,6,1,8,8,1,6,5,4,9,6,7,3,4,2,9,8,4,0,4,2,6,8,4,2,1,6,4,3,2,8,6,9,1,0]
total_num = lista_contar.count(1) #Altere o número e verifique.
print("A quantidade de números 1 é:",total_num)

lista_nomes_contar = ["João"
                      , "Pedro"
                      , "Maria"
                      , "Pedro"
                      , "Lucia"
                      , "Antonio"
                      , "Lucia"
                      , "Pedro"
                      , "Marcos"
                      , "Mateus"
                      , "João"
                      , "Lucia"
                      , "Marcia"
                      , "Sebastião"]

total_nome = lista_nomes_contar.count("João")
print("A quantidade de nomes João é:", total_nome)

# COMMAND ----------

# MAGIC %md #Dicionários
# MAGIC - É um array associativo o que quer dizer que cada chave terá um valor correspondente associado.
# MAGIC - dicionário = {'CHAVE':'valor'}
# MAGIC - Declarado entre chaves{ } e utiliza-se colchetes[ ] para buscar os valores.

# COMMAND ----------

#Dicionário
UF = {"DF":"Distrito Federal"
       , "SP":"São Paulo"
       , "MG":"Minas Gerais"
       , "RJ":"Rio de Janeiro"
       , "BA":"Bahia"
       , "CE":"Ceará"
       , "GO":"Goiás"
       , "MS":"Mato Grosso do Sul"
       , "TO":"Tocantins"
       , "PA":"Pará"}
#Dicionários não possuem índices, portanto se usarmos UFs[0] dará erro.
#Para exibir um elemento é necessário conhecer e utilizar a chave para conhecer o valor.

print(UF["DF"])

print("\n\nDicionário UF:", UF)

for elemento in UF:
  print("Observe que exibirá apenas as chaves:", elemento)


for elemento in UF:
  print("Observe que exibirá apenas os valores das chaves:",UF[elemento])


#Para exibir chave:valor

for elemento in UF:
  print(elemento + " -> " + UF[elemento])

# COMMAND ----------

#método itens
for elemento in UF.items():
  print(elemento) 
#Observe como os conjunto chave:valor é exibido.
#Não é exibido mais como um dicionário e sim como uma tupla. Essas tuplas são imutáveis.

# COMMAND ----------

#método values
for elemento in UF.values():
  print(elemento)
#Dessa maneira só exibe os valores(values).

# COMMAND ----------

#método keys
for elemento in UF.keys():
  print(elemento)
#Dessa maneira só exibe as chaves(keys).

# COMMAND ----------

#noqa
