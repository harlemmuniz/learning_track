# Databricks notebook source
# Ao iniciar um trecho de código utilizando o #(cerquilha/jogo da velha/hashtag), esse trecho não será interpretado pelo compilador, ou seja, essa é uma forma de comentar, descrevendo algo, ou simplesmente, um forma de ignorar algum trecho de código. Outra maneira é utilizar as aspas triplas """ """ que é indicado quando há um texto sendo utilizado como comentário ou código, como exemplo abaixo.

"""Antes de executar qualquer Caixa de Comando, ou Célula de Comando( Cmd 1, Cmd 2, Cmd 3...) é preciso que o cluster esteja ligado. Portanto, na parte superior deste notebook, antes dos comandos File, Edit, View..., Run All, Clear... existe um combobox com o clusters, representado por um ícone de hierarquia. Selecione o indicado e inicie-o. O Cluster desligará automaticamente caso fique mais de 30 minutos sem utilização. Caso deseje executar algum comando, inicie-o novamente. """

#As linhas do parágrafo anterior são um comentário e não é interpretado pelo compilador.

#Para executar qualquer caixa de comando( Cmd 1, Cmd 2, Cmd 3...) pressionar simultâneamente no teclado Ctrl + Enter, ou, no canto superior de cada caixa de comando clique na seta >, e depois em Run Cell.

#Ao utilizar o comando print(), ele exibe o que está entre os parentêses ().

#exemplo:

##Exemplo 1 -> Texto
print("Exemplo 1")
print("---> Texto está sendo exibido como resultado esperado. ;) \n\n\n Conseguiu observar?\n\n\n") # Observe que tudo que está entre as "" está sendo exibido. O comando \n representa uma quebra de linha. Ou seja, tudo que está após o \n será exibido na linha de baixo.

##Exemplo 2 -> Número inteiro e número decimal. A vírgula é utilizada para que o comando print exiba mais de um "parâmetro".
print("Exemplo 2")
print("Número inteiro:", 5, ", Número decimal:", 3.4)

#Exemplo 3 -> Váriável
variavel_texto_numero_inteiro = "Número:"
variavel_numero_inteiro = 89 

print("\n\n Exemplo 3")
print(variavel_texto_numero_inteiro, variavel_numero_inteiro)

#IMPORTANTE
# = é um operador de atribuição e não de igualdade.
#Quando escrevemos x = 3, lemos: x recebe o valor 3. Ou, o valor 3 foi atribuído à variável x.
#Quando escrevemos x = "Temos aqui um resultado esperado.", lemos: x recebe o texto Temos aqui um resultado esperado.
#Ou, Temos aqui um resultado esperado. foi atribuído à variável x.

#noqa

# COMMAND ----------

# MAGIC %md ###Variáveis e Tipos de Dados
# MAGIC Em python tudo é objeto, ou seja, toda variável é um referência. Em python, as variáveis armazenam endereços de memória, e não os valores. E essas variáveis não têm um tipo fixo, e sim apenas o tipo de conteúdo.

# COMMAND ----------

#Uma variável não pode ter caracter especial, nem espaço e é case sensitive, ou seja, se houver uma letra maiúscula já é outra variável.
#Exemplos:

variavel = "Tudo minúsculo.\n"

Variavel = "Inicial maiúscula.\n"

print("Conteúdo de variavel:", variavel)
print("Conteúdo de Variável:", Variavel)

#Observe que não declaramos o tipo da variável, apenas o seu conteúdo. Sendo assim, após x receber um vetor, e y receber a referência de x, ao adicionarmos (append()) a letra a, y continua sendo vetor.
x = [1,2,3]
y = x
x.append("a")
print(y)

#Uma variável exibirá o resultado do último valor atribuído a ela. Exemplo:
valor_atribuido =  1
valor_atribuido =  False
valor_atribuido =  "***Último valor atribuído.***"

print("\nExibindo o valor da variável valor_atribuido: ", valor_atribuido)

#Dê um novo valor à variável valor_atribuido e veja o resultado.

#noqa

# COMMAND ----------

# MAGIC %md Dados númericos

# COMMAND ----------

#Em python não é preciso declarar o tipo da variável. É identificado automáticamente.
numero_inteiro = 5
numero_decimal = 3.6
texto = "Texto"
booleano = True

print("Variável com resultado do tipo número inteiro:", numero_inteiro)
print("Variável com resultado do tipo número decimal:", numero_decimal)
print("Variável com resultado do tipo texto/string:", texto)
print("Variável com resultado do tipo booleano:", booleano)

#noqa

# COMMAND ----------

A = float(22/5) # Resultado é decimal/flutuante: 4,4
B = int(4.5) #Pega só a parte inteira(antes da vírgula) do número, no caso, número 4.
C = int(3.9) #Pega só a parte inteira(antes da vírgula) do número, no caso, número 3.
D = int(0xff563) #Número hexadecimal, pois inicia com 0x ou 0X
E = float(int(3.9)) #Exige um número decimal a partir da extração do número inteiro: 3,0
F = int(float(3.9)) 
G = int(float(3))
H = round(3.9) #A função round arredonda o número, no caso, 3,9, que vira 4.
I = round(3)
J = int(round(3.9))

#Substitua as variáveis de A a J na função print() abaixo e veja o resultado. 
print(A)

#noqa

# COMMAND ----------

# MAGIC %md Dados texto

# COMMAND ----------

a = 'Isso é uma String com aspas Simples'
b = "Isso é uma String com aspas Duplas"
c = """Isso é Uma String com aspas Triplas"""
print(a + "\n" + b + "\n" + c)

#noqa

# COMMAND ----------

# MAGIC %md Dados booleanos

# COMMAND ----------

true = True
false = False

print("O valor da variável true é: ", true)
print("O valor da variável false é: ", false)

#noqa

# COMMAND ----------

#Para saber o type (tipo) da variável utilize a função type.
var1 = False
var2 = 'Isso é uma String com aspas Simples'
var3 = "4.5"
var4 = 3.8
var5 = -68

type(var5)

#Substitua a variavél na função type() e verifique a tipologia das mesmas.

#noqa

# COMMAND ----------

#Outra opção para exibir variáveis é utilizar {} dentro dos comandos:

nome = 'Sebastião Antunes Figueira'
idade = 78
endereco = 'Rua Floriano Peixoto, 10'
num_telefone = 11987654321
cpf = '123.123.123-00'
sexo = 'Masculino'
profissao = 'Físico'

print("Outra maneira de exibir texto + variáveis.")
print("Olá! Meu nome é {}, tenho {} anos e moro no endereço {}.".format(nome, idade, endereco))

print("\nOutra maneira de exibir texto + variáveis. Esse é mais moderno.")
print(f"Olá! Sou o {nome}, tenho {idade} anos.\nMeu número de telefone é {num_telefone}, sou do sexo {sexo} e sou {profissao}.")

#Utilizando a função .format(), todos os argumentos que você passar para a função substituirá as {}.

#noqa

# COMMAND ----------

# MAGIC %md #Operadores

# COMMAND ----------

# MAGIC %md Operadores Aritméticos
# MAGIC - soma (+)
# MAGIC - subtração (-)
# MAGIC - multiplicação (*)
# MAGIC - divisão(/)
# MAGIC - divisão inteira (//)
# MAGIC - módulo/resto da divisão (%)
# MAGIC - exponenciação (**)

# COMMAND ----------

#Soma
print("Resultado da soma de 2 + 3 é:", 2 + 3)

#Subtração
print("\n Resultado da subtração de 2 - 3 é:", 2 - 3)

#Multiplicação
print("\n Resultado da multiplicação de 2 x 3 é:", 2 * 3)

#Divisão
print("\n Resultado da divisão de 2 / 3 é:", 2 / 3)

#Divisão inteira (Desconsidera a parte decimal)
print("\n Resultado da divisão inteira de 2 / 3 é:", 2 // 3)

#Resto da Divisão
print("\n O resto da divisão de 2 / 3 é:", 2 % 3)

#Exponeciação
print("\n Resultado da exponenciação de 2 elevado a (2^3) é:", 2 ** 3)

#Atente-se à ordem de procedência:
# parênteses ()
# exponênciação **
# multiplicação, divisão e módulo *, / e %
# soma e subtração + e -

#noqa

# COMMAND ----------

# MAGIC %md Operadores Relacionais
# MAGIC - igual e diferente(não igual) (== e !=)
# MAGIC - maior e menor (> e <)
# MAGIC - maior igual e menor igual (>= e <=)

# COMMAND ----------

# Um exemplo simples é verificar se duas variáveis são iguais.
var1 = 2
var2 = "2"
var3 = int("2") #Convertendo string em int

print("2 e '2' são iguais? ", var1 == var2) #Saída: False
print("2 e int('2') são iguais? ", var1 == var3) #Saída: True

#Vamos verificar se o tipo das variáveis são iguais e garantir a vericidade da informação anterior.
print("Os tipos das variáveis var1 e var2 são iguais? ", type(var1) == type(var2)) #Saída: False
print("Os tipos das variáveis var1 e var3 são iguais? ", type(var1) == type(var3)) #Saída: True

#noqa

# COMMAND ----------

#Vamos utilizar os dados booleanos para verificar a veracidade os operadores relacionais. True, para verdadeiro e False, para falso.
#Considere as variáveis a seguir:
numero_1 = 20
numero_2 = 5
numero_3 = 20

#noqa

# COMMAND ----------

#Operador de igualdade
verificacao_operador_1 = numero_1 == numero_2
verificacao_operador_2 = numero_1 == numero_3

print("Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador ==, a variável numero_1 é \033[1m igual \033[0m à variável numero_2?\
\n O resultado é: ", verificacao_operador_1, ". \033[1m Falso \033[0m, pois 20 é diferente de 5, e não igual.")

print("\n Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador ==, a variável numero_1 é \033[1m igual \033[0m à variável numero_3?\
\n O resultado é: ", verificacao_operador_2, ". \033[1m Verdadeiro \033[0m, pois 20 =20.")

#noqa

# COMMAND ----------

#Operador de diferente
verificacao_operador_3 = numero_1 != numero_2
verificacao_operador_4 = numero_1 != numero_3
print("\n Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador !=, a variável numero_1 é \033[1m diferente \033[0m da variável numero_2?\
\n O resultado é: ", verificacao_operador_3, ". \033[1m Verdadeiro \033[0m, pois 20 é diferente de 5.")

print("\n Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador !=, a variável numero_1 é \033[1m diferente \033[0m da variável numero_3?\
\n O resultado é: ", verificacao_operador_4, ". \033[1m Falso \033[0m, pois 20 = 20, e não diferente.")

#noqa

# COMMAND ----------

#Operdadores de Maior e Menor. Operadores maior ou igual, menos ou igual.
verificacao_operador_5 = numero_1 > numero_2
verificacao_operador_6 = numero_1 < numero_3
verificacao_operador_7 = numero_2 >= numero_3

print("\n Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador !=, a variável numero_1 é \033[1m maior \033[0m do que a variável numero_2?\
\n O resultado é: ", verificacao_operador_5, ". \033[1m Verdadeiro \033[0m, pois 20 > 5.")

print("\n Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador !=, a variável numero_1 é \033[1m menor \033[0m do que a variável numero_3?\
\n O resultado é: ", verificacao_operador_6, ". \033[1m Falso \033[0m, pois 20 é a 20, e não menor.")

print("\n Se as variáveis tem os seguintes valores:\
\n numero_1 = 20\
\n numero_2 = 5\
\n numero_3 = 20\
\n Utilizando o comparador !=, a variável numero_2 é \033[1m maior ou igual \033[0m à variável numero_3?\
\n O resultado é: ", verificacao_operador_6, ". \033[1m Falso \033[0m, pois 20 é a 20, e não menor.")

#noqa

# COMMAND ----------

# MAGIC %md Operadores Lógicos
# MAGIC - AND
# MAGIC - OR
# MAGIC - NOT

# COMMAND ----------

#Considere as variáveis abaixo:
logica_1 = 3
logica_2 = 3
logica_3 = 3
logica_4 = 6
logica_5 = 12

print("As variáveis logica_1, logica_2 e logica_3 são iguais?", logica_1 == logica_2 and logica_1 == logica_3)

print("Algumas das variáveis logica_1, logica_3 e logica_5 é igual a 12?", logica_1 ==12 or logica_3 == 12 or logica_5 == 12)

#NOT é uma negação, ou seja, ao adicionar o not estou negando a proposição a seguir.
#Logo, se 
#logica_1 = 3 é True.
#not logica_1 é False.
#Observe o resultado.
print("not logica_1 nos dará o resultado False, pois estamos negando que logica_1 = 3. Portanto, o resultado é:", not logica_1 == 3)

#noqa

# COMMAND ----------

# MAGIC %md #Estruturas Condicionais

# COMMAND ----------

# MAGIC %md ##IF
# MAGIC Comando SE avalia se uma condição é verdadeira ou falsa.

# COMMAND ----------

var_1 = 5
var_2 = 8

if var_1 > var_2:
  print("A variável var_1 é maior")
else:
  print("A variável var_2 é maior")
  
#Altere o valor da variável var_1 e verifique o resultado.

#noqa

# COMMAND ----------

#Se você alterar o valor de var_1 para ser o mesmo de var_2 você verá que o resultado não será o esperado.

var_3 = 5
var_4 = 8

if var_3 > var_4:
  print("A variável var_3 é maior")
elif var_3 == var_4:
  print("As variáveis possuem os mesmos valores.")
else:
  print("A variável var_4 é maior")
  
#Altere o valor da variável var_3 e verifique o resultado.
#A indentação se faz obrigatória. Se você não colocar o else na mesma posição do if acusará erro de indentação. O mesmo serve para o elif. Teste e verifique.

#noqa

# COMMAND ----------

#A ordem de execução também importa, pois essa estrutura para de ser executada ao encontrar a primeira verdadeira. Observe.
var_5 = 9
var_6 = 8

if var_5 == var_6:
  print("As variáveis são iguais.")
elif var_5 > var_6:
  print("A variável var_5 é maior.")
else:
  print("As variáveis não são iguais.")
  

#Observe que se var_5 for maior que var_6, elas são também diferentes, e o else então não será executado. Pois a primeira condição verdadeira já foi satisfeita.

#noqa

# COMMAND ----------

#Exercício 1
#Considerando 2 variáveis e utilizando a estrutura condicional IF.
#Informar qual é o maior número e se o número é positivo ou negativo.

# COMMAND ----------

# MAGIC %md #Estruturas de Repetição ou Iteradoras.
# MAGIC - Repetem uma ação enquanto uma condição for verdadeira.
# MAGIC - Iterar = repetir

# COMMAND ----------

# MAGIC %md ##While
# MAGIC Comando WHILE(enquanto) repete uma ação enquanto uma ou mais condições forem verdadeiras.

# COMMAND ----------

coman_while = 1
while coman_while < 10:
  print("A variável coman_while recebeu o valor: ", coman_while)
  coman_while = coman_while + 1          #ou coman_while += 1

  #noqa

# COMMAND ----------

#Outra exemplo utilizando dupla validação do while.
com_while = 100
com_whi = 20

while com_whi < 200 and com_while > 25:
  print("A soma é realizada da seguinte forma:", com_while, "+", com_whi, "=", com_while + com_whi)
  com_while -=1
  com_whi +=2

#Enquanto o com_whi for menor que 200 e ao mesmo tempo o com_while maior que 25, subtrai -1 do com_while e adicionar +2 ao com_whi a cada execução.

#noqa

# COMMAND ----------

# MAGIC %md ##FOR
# MAGIC Comando FOR(para) executada determinada ação para os parâmetros declarados.

# COMMAND ----------

#O FOR com apenas um parâmetro no range define o limite máximo de execuções do comando for.
for unidade in range(10):
  print(unidade)

#Observe que definimos um range de 10. Esse range diz a quantidade de execuções, e não o número de parada.
#Ou seja, a função print(unidade) será executada 10 vezes.
#Em python a contagem começa no 0. Portanto, a função print(unidade) exibirá 10 resultados: do 0 ao 9.

#noqa

# COMMAND ----------

#É possível definir um número limitado de execuções. Para isso adicionamos mais um parâmetro no comando range.

for unidade_dezena in range(0,100):
  print(unidade_dezena)

#Observe que ao colocarmos os parâmetros 1, 99 estamos definindo o limite mínimo e máximo de execuções.
#Iniciou no 0 e finalizou no 100. Ou seja, o limite máximo nunca é executado. É sempre o limite máximo - 1.

#Se você trocar o 100 por 99, o último número exibido será o 98. Teste.

#noqa

# COMMAND ----------

#É possível também definir de quanto em quanto o limite máximo tem que ser incrementado ou decrementado.
for dezenas in range(10, 100, 10):
  print(dezenas)

#Observe que apenas as dezenas exatas foram exibidas.
#O laço for funcionou iniciando no 10 e finalizando no 100-1, e sendo incrementado de 10 em 10.
#Ou seja, contamos de 10 em 10, do 10 ao 90.

#noqa

# COMMAND ----------

#For decrementado
for dezenas_desc in range(100, 0, -10):
  print(dezenas_desc)
#Contagem de 10 em 10, decrescente, de 100 a 0.

#noqa

# COMMAND ----------

# MAGIC %md ##FOR em listas.

# COMMAND ----------

#Podemos criar/obter listas e "caminhar" por essa lista utilizando o for.

nomes = ["João", "Pedro", "Maria", "Rita"]
idades = [21, 34, 19, 64]
varios = [True, False, "Antônio", "Isabel", 12, 45, 6.78, 9.99]

for lista in varios:
  print(lista)

#noqa

# COMMAND ----------

# MAGIC %md #Objetos
# MAGIC ##Em Python, tudo é objeto!
# MAGIC Python é uma linguagem orientada a objetos. Objetos são instâncias de classes. Por exemplo, quando você cria uma variável com uma string, você está criando um objeto do tipo  string.
# MAGIC
# MAGIC
# MAGIC
# MAGIC Objetos possuem atributos (características) e métodos (ações que podem ser aplicadas).

# COMMAND ----------

# MAGIC %md #Strings
# MAGIC - São declaradas utilizando aspas ou apóstrofos: "string" ou 'string'
# MAGIC
# MAGIC ###Observação
# MAGIC A principal diferença entre "string" ou 'string' é que as aspas duplas permitem que variáveis sejam incorporadas diretamente na string e permitem a interpretação de caracteres de escape, enquanto as aspas simples tratam o conteúdo estritamente como texto e não expandem variáveis nem interpretam caracteres de escape. Em termos de escolha entre as duas, muitas vezes é uma questão de preferência pessoal, mas a capacidade de usar variáveis e caracteres de escape em strings delimitadas por aspas duplas é frequentemente mais versátil em muitos cenários.
# MAGIC

# COMMAND ----------

#Concatenação

primeiro_nome = "Marcos"
sobrenome = "Pereira Albuquerque"

nome_completo = primeiro_nome + sobrenome

print(nome_completo, " - Sem espaço.")

#Observe que as palavras Marcos e Pereira estão juntas: MarcosPereira.
nome_completo_espaco = primeiro_nome + " " + sobrenome

print(nome_completo_espaco, "- Com espaço.")

#noqa

# COMMAND ----------

#Lenght - Tamanho da string

tamanho = len(nome_completo_espaco)
print(tamanho) #Contabiliza todos os caracteres da string. 

#noqa

# COMMAND ----------

#Localização e posição de caracteres
print(nome_completo_espaco[0])
print(nome_completo_espaco[1])
print(nome_completo_espaco[2])
print(nome_completo_espaco[3])
print(nome_completo_espaco[4])
print(nome_completo_espaco[5])
#.
#.
#.
print(nome_completo_espaco[25])

#São 26 posições a string da variável nome_completo_espaco. Do 0 ao 25.
#Se você quiser ler o 26, que não existe, vai dar erro: string index out of range. Teste.

#noqa

# COMMAND ----------

#Extraindo um trecho de caracteres da string. Da posição 1 à posição 5 resultando na sequência arco.
print(nome_completo_espaco[1:5])

#Se desejar da posição 5 até o final da string, deixe a segunda posição vazia.
print(nome_completo_espaco[5:])

#noqa

# COMMAND ----------

#Strings são objetos, e sendo o python uma linguagem orientada a objetos, podemos então utilizar métodos(.metodo()).
nome_completo_metodo = "Juliano Fonseca Marques da Silva"
print("Como escrito na variável: ", nome_completo_metodo)
#Método de colocar letra maiúscula .upper() e letra minúscula .lower().
nome_completo_metodo = nome_completo_metodo.upper()
print("Tudo em letra maiúscula: ", nome_completo_metodo)
nome_completo_metodo = nome_completo_metodo.lower()
print("Tudo em letra minúscula: ", nome_completo_metodo)

#noqa

# COMMAND ----------

#strip - remove espaços após o último caracter
nome_espacos = "Pedro Paulo                      "
nome_espacos.strip()

#noqa

# COMMAND ----------

#split - divide a string de acordo com os espaços em branco, ou de acordo com o padrão passado.
bbts = "BB Tecnologia e Serviços"
bbts_split = bbts.split() # Observe que o método retira os espaços e cria uma lista com os strings restantes.
print(bbts_split)

trava_lingua = "O rato roeu a rica roupa do rei de Roma! A rainha raivosa rasgou o resto e depois resolveu remendar!"
trava_lingua_split = trava_lingua.split()
print(trava_lingua_split)

trava_lingua_split_r = trava_lingua.split("r")
print(trava_lingua_split_r) #Observe que o método .split() retira a letra r (minúscula) e das palavras restantes cria uma lista. 
#Trabalhar com string é case sensitive. Ou sera r minúsculo é diferente de R maiúsculo. Observer que o R maiúsculo continua na string trava_lingua_split_r.

#noqa

# COMMAND ----------

#Buscar dentro da string retornando a posição do primeiro caracter.

busca_trava_lingua = "A vida é uma sucessiva sucessão de sucessões que se sucedem sucessivamente, sem suceder o sucesso."
busca_trava_lingua.find("sucessiva") #Inicia no caracter de posição 13.

#noqa

# COMMAND ----------

#Lembra que podemos fazer uma busca definindo um limite mínimo e máximo?
trava_lingua_busca = "Disseram que na minha rua tem paralelepípedo feito de paralelogramos. Seis paralelogramos têm um paralelepípedo. Mil paralelepípedos têm uma paralelepipedovia. Uma paralelepipedovia tem mil paralelogramos. Então uma paralelepipedovia é uma paralelogramolândia?"

trava_busca_minima = trava_lingua_busca.find("minha") #a busca iniciará na palavra minha
trava_busca_maxima = trava_lingua_busca.find("Então") #e finalizará na palavra Então - 1.

trava_minima_maxima = trava_lingua_busca[trava_busca_minima:trava_busca_maxima]

print(trava_minima_maxima)

#noqa

# COMMAND ----------

#Replace - substitui uma palavra pela outra
trava_pedro = "Se o Pedro é preto, o peito do Pedro é preto e o peito do pé do Pedro também é preto."

trava_pedro_replace = trava_pedro.replace("Pedro", "João")

print(trava_pedro_replace)

#noqa

# COMMAND ----------

# MAGIC %md #TypeCasting
# MAGIC Em Python, existem várias maneiras de converter tipos de variáveis para atender às necessidades específicas do seu programa. Vamos conceituar, diferenciar e fornecer cinco exemplos de cada tipo de conversão. Vamos começar:

# COMMAND ----------

# DBTITLE 1,Conversão Implícita
#Conceito: A conversão implícita ocorre ***automaticamente** quando uma variável é usada em uma operação que espera um tipo diferente. Isso é feito pelo Python para garantir que as operações sejam realizadas de maneira compatível.
#Diferenciação: A conversão é realizada sem intervenção direta do programador. Por exemplo, quando você soma um número inteiro e um número de ponto flutuante, o Python converte implicitamente o inteiro em um ponto flutuante para realizar a operação.

#Exemplos:
# Exemplo 1: Conversão implícita de int para float
x = 5
y = 2.0
resultado = x + y
print_resultado = f"Exemplo 1 -> {resultado}"
print(print_resultado)  # Saída: 7.0 (float)

# Exemplo 2: Conversão implícita de int para str
numero = 42
mensagem = "Exemplo 2 -> O número é: " + str(numero)
print(mensagem)  # Saída: "O número é: 42" (str)

# Exemplo 3: Conversão implícita de int para bool
valor_inteiro = 0
comparacao = valor_inteiro == 0
print_exemplo_3 = f"Exemplo 3 -> {comparacao}"
print(print_exemplo_3)  # Saída: True (bool)

# Exemplo 4: Conversão implícita de bool para int
verdadeiro = True
falso = int(verdadeiro == False) # a verificação é falsa, pois verdadeiro não é igual a False
print_exemplo_4 = f"Exemplo 4 -> {falso}"
print(print_exemplo_4)  # Saída: 0 (int) 

# Exemplo 5: Conversão implícita de int para complex
inteiro = 2
complexo = 1 + 2j + inteiro
print_exemplo_5 = f"Exemplo 5 -> {complexo}"
print(print_exemplo_5)  # Saída: (3+2j) (complex)

#noqa

# COMMAND ----------

# DBTITLE 1,Conversão Explícita (Casting)
#Conceito: A conversão explícita é o processo de alterar manualmente o tipo de uma variável de acordo com a necessidade do programa.
#Diferenciação: O programador utiliza funções de conversão específicas para realizar a conversão de um tipo para outro.

#Exemplos:

# Exemplo 1: Conversão explícita de float para int
valor_float = 3.8
valor_int = int(valor_float)
print(f"Exemplo 1 -> {valor_int}")  # Saída: 3 (int)

# Exemplo 2: Conversão explícita de str para int
numero_str = "42"
numero_int = int(numero_str)
print(f"Exemplo 2 -> {numero_int}")  # Saída: 42 (int)

# Exemplo 3: Conversão explícita de int para str
inteiro = 123
texto = str(inteiro)
print(f"Exemplo 3 -> {texto}")  # Saída: "123" (str)

# Exemplo 4: Conversão explícita de float para str
numero_float = 3.14
texto = str(numero_float)
print(f"Exemplo 4 -> {texto}")  # Saída: "3.14" (str)

# Exemplo 5: Conversão explícita de str para float
valor_str = "7.5"
valor_float = float(valor_str)
print(f"Exemplo 5 -> {valor_float}")  # Saída: 7.5 (float)

#noqa

# COMMAND ----------

# DBTITLE 1,Conversão de String para Outros Tipos
#Conceito: Converte uma string em outro tipo, o que é útil para processar dados de entrada do usuário.
#Diferenciação: Use funções de conversão, como int(), float(), e bool(), para converter strings em tipos numéricos ou booleanos.

#Exemplos:

# Exemplo 1: Conversão de str para int
numero_str = "42"
numero_int = int(numero_str)
print(f"Exemplo 1 -> {numero_int}")  # Saída: 42 (int)

# Exemplo 2: Conversão de str para float
valor_str = "3.14"
valor_float = float(valor_str)
print(f"Exemplo 2 -> {valor_float}")  # Saída: 3.14 (float)

# Exemplo 3: Conversão de str para bool
texto = "True"
booleano = bool(texto)
print(f"Exemplo 3 -> {booleano}")  # Saída: True (bool)

# Exemplo 4: Conversão de str para lista de caracteres
texto = "Python"
lista_de_caracteres = list(texto)
print(f"Exemplo 4 -> {lista_de_caracteres}")  # Saída: ['P', 'y', 't', 'h', 'o', 'n'] (lista)

# Exemplo 5: Conversão de str para lista de palavras
frase = "Python é incrível"
lista_de_palavras = frase.split()
print(f"Exemplo 5 -> {lista_de_palavras}")  # Saída: ['Python', 'é', 'incrível'] (lista)

#noqa

# COMMAND ----------

# DBTITLE 1,Conversão de Tipos Numéricos
#Conceito: Realiza conversões entre tipos numéricos, como inteiros e números de ponto flutuante.
#Diferenciação: A conversão de um número de ponto flutuante para um número inteiro por meio de int() resulta em truncagem, removendo a parte decimal.

#Exemplos:

# Exemplo 1: Conversão de int para float
valor_int = 7
valor_float = float(valor_int)
print(f"Exemplo 1 -> {valor_float}")  # Saída: 7.0 (float)

# Exemplo 2: Conversão de float para int
valor_float = 9.8
valor_int = int(valor_float)
print(f"Exemplo 2 -> {valor_int}")  # Saída: 9 (int)

# Exemplo 3: Conversão de float para complex
numero_float = 3.14
numero_complexo = complex(numero_float, 2)
print(f"Exemplo 3 -> {numero_complexo}")  # Saída: (3.14+2j) (complex)

# Exemplo 4: Conversão de complex para int
numero_complexo = 2 + 5j
numero_int = int(numero_complexo.real)
print(f"Exemplo 4 -> {numero_int}")  # Saída: 2 (int)

# Exemplo 5: Conversão de int para hexadecimal
inteiro = 255
hexadecimal = hex(inteiro)
print(f"Exemplo 5 -> {hexadecimal}")  # Saída: '0xff' (str)

#Exemplo 6: número inteiro para binário
numero_inteiro = 42
binario = bin(numero_inteiro)
binario_str = binario[2:]  #Só binário retornaria o valor 0b101010, porém com o [2:] remove o prefixo '0b' e apresenta apenas o número 101010
print(f'Exemplo 6 -> O número {numero_inteiro} em binário é: {binario_str}') #Saída: O número 42 em binário é: 101010

#Exemplo 7: hexadecimal pars binário
hexadecimal = "1A"
decimal = int(hexadecimal, 16) #O segundo argumento 16 especifica que o valor em hexadecimal deve ser interpretado como um número na base 16 (hexadecimal).
binario = bin(decimal)
binario_str = binario[2:]  # Remova o prefixo '0b'
print(f'Exemplo 7 -> O valor hexadecimal {hexadecimal} em binário é: {binario_str}') #Saída: O valor hexadecimal 1A em binário é: 11010

#noqa

# COMMAND ----------

# DBTITLE 1,Conversão de Sequências
#Conceito: Converte entre sequências, como listas, tuplas e strings.
#Diferenciação: Use as funções list(), tuple(), e str() para realizar as conversões. As sequências são mantidas na mesma ordem.

#Exemplos:

# Exemplo 1: Conversão de lista para tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(f"Exemplo 1 -> {tupla}")  # Saída: (1, 2, 3) (tupla)

# Exemplo 2: Conversão de tupla para lista
tupla = (4, 5, 6)
lista = list(tupla)
print(f"Exemplo 2 -> {lista}")  # Saída: [4, 5, 6] (lista)

# Exemplo 3: Conversão de string para lista de caracteres
texto = "Python"
lista_de_caracteres = list(texto)
print(f"Exemplo 3 -> {lista_de_caracteres}")  # Saída: ['P', 'y', 't', 'h', 'o', 'n'] (lista)

# Exemplo 4: Conversão de lista para string
lista_de_palavras = ["Python", "é", "incrível"]
frase = " ".join(lista_de_palavras)
print(f"Exemplo 4 -> {frase}")  # Saída: "Python é incrível" (str)

# Exemplo 5: Conversão de string para tupla de palavras
frase = "Python é ótimo"
tupla_de_palavras = tuple(frase.split())
print(f"Exemplo 5 -> {tupla_de_palavras}")  # Saída:

#noqa

# COMMAND ----------

# MAGIC %md #Estruturas de Dados
# MAGIC ##O Python oferece várias estruturas de dados para armazenar, organizar e manipular informações.
# MAGIC Cada uma dessas estruturas tem características e usos específicos. Vamos conceituar e diferenciar algumas das estruturas de dados mais comuns em Python:
# MAGIC
# MAGIC 1. **Listas (Lists)**
# MAGIC 2. **Tuplas (Tuples)**
# MAGIC 3. **Conjuntos (Sets)**
# MAGIC 4. **Dicionários (Dictionaries)**
# MAGIC
# MAGIC #### Em Python, as estruturas de dados tradicionais de arrays, filas, pilhas e strings são frequentemente implementadas usando as estruturas de dados fornecidas pelo próprio Python, como listas, tuplas, strings e listas (no caso de filas e pilhas).
# MAGIC 5. **Strings (Strings)**
# MAGIC 6. **Arrays (Arrays)**
# MAGIC 7. **Pilhas (Stacks)**
# MAGIC 8. **Filas (Queues)**
# MAGIC 9. **Deque (Deque)**
# MAGIC
# MAGIC Essas são algumas das estruturas de dados mais comuns em Python. A escolha da estrutura de dados a ser usada depende dos requisitos específicos de um problema. Cada estrutura tem suas vantagens e limitações, e a compreensão de quando e como usá-las é fundamental para escrever código eficiente e legível.

# COMMAND ----------

# DBTITLE 1,Listas
#Conceito: Uma lista é uma coleção ordenada e mutável de elementos, que podem ser de diferentes tipos.
#Diferenciação: As listas são definidas entre colchetes `[]`, os elementos podem ser acessados por índices, podem conter valores duplicados e são mutáveis, o que significa que os elementos podem ser alterados, adicinonados ou removidos.

# Exemplo 1: Criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Exemplo 2: Criando uma lista de strings
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# Exemplo 3: Modificando uma lista
frutas[1] = "uva"
print(frutas)

# Exemplo 4: Adicionando um elemento à lista
frutas.append("morango")
print(frutas)

# Exemplo 5: Removendo um elemento da lista
frutas.remove("maçã")
print(frutas)

#noqa

# COMMAND ----------

# DBTITLE 1,Tuplas
#Conceito: Uma tupla é uma coleção ordenada e imutável de elementos, frequentemente usada para armazenar dados relacionados.
#Diferenciação: As tuplas são definidas entre parênteses `()`, os elementos podem ser acessados por índices, são imutáveis (não podem ser alterados após a criação) e podem conter elementos de diferentes tipos.

# Exemplo 1: Criando uma tupla de coordenadas
coordenadas = (3, 4)
print(coordenadas)

# Exemplo 2: Acessando elementos de uma tupla
x, y = coordenadas
print(f"Coordenada x: {x}, Coordenada y: {y}")

# Exemplo 3: Tupla de informações do aluno
aluno = ("João", 20, "Ciência da Computação")
print(aluno)

# Exemplo 4: Concatenando tuplas
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

# Exemplo 5: Verificando a existência de um elemento em uma tupla
frutas = ("maçã", "banana", "laranja")
existe_banana = "banana" in frutas
print(f"Banana existe na tupla: {existe_banana}")

#noqa

# COMMAND ----------

# DBTITLE 1,Conjuntos
#Conceito: Um conjunto é uma coleção desordenada e mutável de elementos únicos. É frequentemente usado para realizar operações de conjuntos, como união, interseção e diferença.
#Diferenciação: Os conjuntos são definidos entre chaves `{}`, não possuem índices, não permitem elementos duplicados e são mutáveis (podem ser modificados após a criação).

# Exemplo 1: Criando um conjunto de números inteiros
numeros = {1, 2, 3, 4, 5}
print(numeros)

# Exemplo 2: Adicionando elementos a um conjunto
numeros.add(6)
print(numeros)

# Exemplo 3: Removendo elementos de um conjunto
numeros.remove(3)
print(numeros)

# Exemplo 4: Realizando operações de conjunto
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
uniao = conjunto1.union(conjunto2)
print(f"União: {uniao}")

# Exemplo 5: Verificando a existência de um elemento em um conjunto
existe_4 = 4 in numeros
print(f"O número 4 existe no conjunto: {existe_4}")

#noqa

# COMMAND ----------

# DBTITLE 1,Dicionários
#Conceito: Um dicionário é uma coleção desordenada de pares chave-valor, onde cada chave é única e mapeia para um valor correspondente.
#Diferenciação: Os dicionários são definidos entre chaves `{}`, os elementos são acessados por meio de chaves, não permitem chaves duplicadas, são mutáveis (os valores associados às chaves podem ser alterados), e os valores podem ser de diferentes tipos.

# Exemplo 1: Criando um dicionário de informações de uma pessoa
pessoa = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
print(pessoa)

# Exemplo 2: Acessando valores por chave
nome = pessoa["nome"]
print(f"Nome: {nome}")

# Exemplo 3: Modificando valores em um dicionário
pessoa["idade"] = 26
print(pessoa)

# Exemplo 4: Adicionando um novo par chave-valor
pessoa["email"] = "alice@email.com"
print(pessoa)

# Exemplo 5: Verificando a existência de uma chave
existe_cidade = "cidade" in pessoa
print(f"Cidade existe no dicionário: {existe_cidade}")

#noqa

# COMMAND ----------

# DBTITLE 1,Strings
#Conceito: Uma string é uma sequência imutável de caracteres, usada para armazenar texto.
#Diferenciação: As strings são definidas entre aspas simples `' '` ou duplas `" "`, os caracteres podem ser acessados por índices, são imutáveis (não podem ser alteradas após a criação) e suportam operações de string, como concatenação e fatiamento.

# Exemplo 1: Concatenando strings
texto1 = "Olá"
texto2 = " Mundo"
texto_completo = texto1 + texto2
print(texto_completo)

# Exemplo 2: Dividindo uma string
frase = "Python é uma linguagem de programação"
palavras = frase.split(" ")
print(palavras)

# Exemplo 3: Substituindo caracteres em uma string
texto = "Hoje é um lindo dia"
novo_texto = texto.replace("lindo", "ensolarado")
print(novo_texto)

# Exemplo 4: Verificando se uma string começa com um prefixo
texto = "Python é ótimo"
comeca_com_python = texto.startswith("Python")
print(f"A string começa com 'Python': {comeca_com_python}")

# Exemplo 5: Transformando uma lista de palavras em uma única string
palavras = ["Python", "é", "fantástico"]
frase = " ".join(palavras)
print(frase)

#noqa

# COMMAND ----------

# DBTITLE 1,Arrays
#Conceito: Um array é uma estrutura de dados que armazena elementos do mesmo tipo em uma sequência contígua de memória.
#Diferenciação: Em Python, os arrays podem ser criados usando a biblioteca `array`, e os elementos são acessados por índices. A principal diferença em relação às listas é que os arrays são tipados, o que significa que todos os elementos devem ser do mesmo tipo.

from array import array

# Exemplo 1: Criando um array de inteiros
meu_array = array('i', [1, 2, 3, 4, 5])
print(meu_array)

# Exemplo 2: Adicionando elementos ao array
meu_array.append(6)
print(meu_array)

# Exemplo 3: Acessando elementos do array
elemento = meu_array[2]
print(f"Elemento 2: {elemento}")

# Exemplo 4: Removendo elementos do array
meu_array.remove(4)
print(meu_array)

# Exemplo 5: Encontrando o índice de um elemento no array
indice = meu_array.index(3)
print(f"Índice do elemento 3: {indice}")

#noqa

# COMMAND ----------

# DBTITLE 1,Pilhas
#Conceito: Uma pilha é uma estrutura de dados que segue o princípio "último a entrar, primeiro a sair" (LIFO). Também pode ser implementada usando listas.
#Diferenciação: Os elementos são adicionados e removidos sempre do topo da pilha.

# Exemplo 1: Criando uma pilha
pilha = []

pilha.append(1)  # Empilhar
pilha.append(2)
elemento = pilha.pop()  # Desempilhar
print(elemento)

# Exemplo 2: Empilhando e desempilhando elementos
pilha.append(3)
pilha.append(4)
elemento = pilha.pop()
print(elemento)

# Exemplo 3: Verificando se a pilha está vazia
vazia = not pilha
print(f"A pilha está vazia: {vazia}")

# Exemplo 4: Tamanho da pilha
tamanho = len(pilha)
print(f"Tamanho da pilha: {tamanho}")

# Exemplo 5: Invertendo uma lista com pilha
minha_lista = [1, 2, 3, 4, 5]
pilha = []
for elemento in minha_lista:
    pilha.append(elemento)
minha_lista_invertida = []
while pilha:
    minha_lista_invertida.append(pilha.pop())
print(minha_lista_invertida)

#noqa

# COMMAND ----------

# DBTITLE 1,Filas
#Conceito: Uma fila é uma estrutura de dados que segue o princípio "primeiro a entrar, primeiro a sair" (FIFO). Pode ser implementada usando listas.
#Diferenciação: Os elementos são adicionados ao final da fila e removidos do início da fila.

from collections import deque

# Exemplo 1: Criando uma fila
fila = deque()
fila.append(1)  # Enfileirar
fila.append(2)
elemento = fila.popleft()  # Desenfileirar
print(elemento)

# Exemplo 2: Enfileirando e desenfileirando elementos
fila.append(3)
fila.append(4)
elemento = fila.popleft()
print(elemento)

# Exemplo 3: Verificando se a fila está vazia
vazia = not fila
print(f"A fila está vazia: {vazia}")

# Exemplo 4: Tamanho da fila
tamanho = len(fila)
print(f"Tamanho da fila: {tamanho}")

# Exemplo 5: Convertendo uma lista em fila
minha_lista = [5, 6, 7]
fila.extend(minha_lista)
print(fila)

#noqa

# COMMAND ----------

# DBTITLE 1,Deque
#Conceito: Um deque (double-ended queue) é uma estrutura de dados que permite adicionar e remover elementos de ambos os extremos da sequência de forma eficiente.
#Diferenciação: Em Python, os deques podem ser criados usando a biblioteca `collections`, e são úteis quando é necessário desempenho rápido para operações de adição e remoção nos dois extremos da sequência.

from collections import deque

# Exemplo 1: Criando uma fila com deque
fila = deque()
fila.append(1)  # Enfileirar
fila.append(2)
elemento = fila.popleft()  # Desenfileirar
print(f"Elemento desenfileirado: {elemento}")

# Exemplo 2: Adicionando e removendo elementos da fila
fila.append(3)
fila.append(4)
fila.append(5)
elemento = fila.popleft()
print(f"Elemento desenfileirado: {elemento}")

# Exemplo 3: Verificando se a fila está vazia
vazia = not fila
print(f"A fila está vazia: {vazia}")

# Exemplo 4: Tamanho da fila
tamanho = len(fila)
print(f"Tamanho da fila: {tamanho}")

# Exemplo 5: Convertendo uma lista em fila
minha_lista = [6, 7, 8]
fila.extend(minha_lista)
print(fila)

#noqa

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ###Em Python, uma fila (queue) e um deque (double-ended queue) têm funcionalidades semelhantes, mas a principal diferença está na flexibilidade e na forma como são implementados.
# MAGIC
# MAGIC
# MAGIC ####Fila (Queue):
# MAGIC - Uma fila em Python é uma estrutura de dados que segue a política "primeiro a entrar, primeiro a sair" (FIFO - First-In-First-Out). Isso significa que o primeiro elemento adicionado é o primeiro a ser removido.
# MAGIC - As filas são implementadas usando a biblioteca queue em Python, geralmente por meio do módulo queue.Queue.
# MAGIC - As operações principais em uma fila são put() para adicionar elementos e get() para remover elementos.
# MAGIC - As filas são úteis para coordenar threads em programação concorrente e multithreading.
# MAGIC
# MAGIC ####Deque (collections.deque):
# MAGIC - Um deque é uma estrutura de dados mais geral que suporta operações de fila (enfileirar e desenfileirar) e pilha (empilhar e desempilhar).
# MAGIC - Os deque são implementados usando o módulo collections.deque.
# MAGIC - Eles permitem adicionar ou remover elementos tanto na parte da frente quanto na parte de trás da estrutura de dados de forma eficiente.
# MAGIC - Os métodos principais em um deque incluem append() e popleft() para operações de fila e appendleft() e popleft() para operações de pilha.
# MAGIC
# MAGIC ####Diferenças:
# MAGIC - As filas geralmente são usadas para fins específicos, como programação concorrente, enquanto os deque são mais versáteis e podem ser usados em várias situações.
# MAGIC - deque é mais eficiente para operações de enfileirar e desenfileirar em ambas as extremidades, o que pode ser útil em cenários onde a eficiência é importante.
# MAGIC - Em resumo, a escolha entre usar uma fila ou um deque depende das necessidades específicas do seu programa. Se você precisa apenas de uma fila com políticas FIFO, a fila é a escolha mais direta. No entanto, se precisa de flexibilidade adicional ou eficiência nas operações de enfileirar e desenfileirar, um deque é uma escolha mais versátil.
# MAGIC

# COMMAND ----------

# MAGIC %md #FUNÇÕES
# MAGIC
# MAGIC ###O que é uma função em Python?
# MAGIC Uma função em Python é um bloco de código reutilizável que realiza uma tarefa específica quando chamada. Ela é uma forma de organizar e reutilizar código, tornando-o mais modular e legível.

# COMMAND ----------

#Como definir uma função em Python:
#Para definir uma função em Python, você usa a palavra-chave def, seguida do nome da função e parênteses. Você também pode especificar argumentos (parâmetros) entre os parênteses, que são valores que a função aceitará quando for chamada. A definição da função termina com dois pontos, e o código da função é indentado (recuado) para formar um bloco. Aqui está a estrutura básica de uma função:

def nome_da_funcao(argumento1, argumento2, entre_outros):
  """
  Esta é uma função de exemplo.
  Args:
      parametro: Uma descrição do parâmetro.
  Returns:
      Uma descrição do que a função retorna.
  """
  # Código da função.Pode incluir qualquer lógica que você desejar
  return resultado  # Opcional, usado para retornar um valor da função

#Como chamar uma função:
#Para usar uma função em Python, você a chama pelo nome seguido dos argumentos necessários. Se a função retornar um valor, você pode atribuí-lo a uma variável ou usá-lo diretamente. Aqui está como você chama uma função:
"""
resultado = nome_da_funcao(valor1, valor2, ...)

"""

#noqa

# COMMAND ----------

#Exemplo de Definição e Chamada de Função:
#Vamos criar uma função simples que calcula a média de dois números:

def calcular_media(numero1, numero2):
    media = (numero1 + numero2) / 2
    return media

#Agora, podemos chamar essa função e armazenar o resultado em uma variável:
resultado = calcular_media(4, 6)
print(resultado)  # Isso imprimirá 5.0

#noqa

# COMMAND ----------

#Escopo de Variáveis:
#Variáveis definidas dentro de uma função são chamadas de variáveis locais e só podem ser acessadas dentro da função. Variáveis definidas fora de qualquer função são chamadas de variáveis globais e podem ser acessadas em todo o programa.

#Exemplo de Variáveis Locais e Globais:
variavel_global = 10  # Variável global

def minha_funcao():
    variavel_local = 5  # Variável local
    print(variavel_global)  # Esta linha é válida
    print(variavel_local)  # Esta linha é válida

minha_funcao()
print(variavel_global)  # Esta linha é válida
print(variavel_local)  # Isso resultará em um erro, pois variavel_local é uma variável local da função.

#noqa

# COMMAND ----------

#Retorno de Função:
#Uma função pode ou não retornar um valor. A palavra-chave return é usada para especificar o valor a ser retornado. Se uma função não tem uma instrução return, ela retorna None por padrão.

#Exemplo de Função com e sem Retorno:
def funcao_com_retorno():
    return "Isso é um retorno"

def funcao_sem_retorno():
    print("Isso não tem retorno")

resultado1 = funcao_com_retorno()
resultado2 = funcao_sem_retorno()

print(resultado1)  # Isso imprimirá "Isso é um retorno"
print(resultado2)  # Isso imprimirá "None", já que a segunda função não tem um retorno explícito.

#noqa

# COMMAND ----------

# MAGIC %md
# MAGIC #Argumentos e Parâmetros:
# MAGIC
# MAGIC - Argumentos: são os valores reais que são passados para uma função quando ela é chamada. Os argumentos são as informações reais que a função utilizará durante sua execução.
# MAGIC - Parâmetros: são nomes de variáveis que você especifica na definição de uma função. Eles representam os valores que a função espera receber quando é chamada. Os parâmetros são usados para transmitir informações da parte que chama a função para a função em si.

# COMMAND ----------

#Exemplo de Parâmetros e Argumentos:
def saudacao(nome):  # "nome" é um parâmetro
    print("Olá, " + nome + "!")

nome_da_pessoa = "Alice"  # "nome_da_pessoa" é uma variável
saudacao(nome_da_pessoa)  # "nome_da_pessoa" é um argumento

#No exemplo acima, nome é um parâmetro na definição da função saudacao. Ele atua como um marcador de posição para um valor que será fornecido quando a função for chamada.
#nome_da_pessoa é uma variável que armazena o valor "Alice". Quando chamamos a função saudacao e passamos nome_da_pessoa como argumento, estamos fornecendo o valor real que a função usará em seu corpo.

#noqa

# COMMAND ----------

# DBTITLE 1,Parâmetros
#Em Python, existem diferentes tipos de parâmetros que podem ser usados em funções:

# Parâmetros Posicionais: Os parâmetros posicionais são os mais comuns. Eles são passados na ordem em que são definidos na função. Por exemplo:
def soma(a, b):
    return a + b

resultado = soma(3, 5) #Nesse caso, a recebe o valor 3 e b recebe o valor 5.

#Parâmetros Padrão: Parâmetros padrão são parâmetros que têm um valor predefinido ***se nenhum valor for fornecido*** quando a função é chamada. Eles são úteis quando você deseja que a função tenha um valor padrão, mas também permita que o usuário substitua esse valor:
def saudacao(nome, mensagem="Olá"):
    print(mensagem + ", " + nome + "!")

saudacao("Alice")  # Nenhum valor fornecido para "mensagem", então o valor padrão "Olá" é usado.

#Você também pode desempacotar argumentos de uma sequência (como uma tupla ou lista) usando o operador *. Isso é útil quando você deseja passar uma sequência de valores como argumentos para uma função.
def soma(a, b):
    return a + b

valores = (3, 5)
resultado = soma(*valores)  # Desempacotando os valores da tupla

#noqa

# COMMAND ----------

#Parâmetros arbitrários: referem-se a uma técnica que permite que você defina funções que podem aceitar um número variável de argumentos. Isso é especialmente útil quando você não sabe de antemão quantos argumentos serão passados para a função. Existem dois tipos principais de parâmetros arbitrários em Python: parâmetros de palavras-chave arbitrários (*args) e parâmetros de palavras-chave arbitrários (**kwargs).

#Parâmetros de Palavras-Chave Arbitrários (*args):
"""
- Parâmetros *args permitem que uma função aceite um número arbitrário de argumentos posicionais (sem nomes específicos) em uma tupla.
- O asterisco (*) antes do nome "args" é uma convenção, mas você pode escolher qualquer nome.
- Esses parâmetros são frequentemente usados quando você deseja criar funções flexíveis que possam lidar com diferentes quantidades de dados.
"""
#Exemplo de *args:
def somar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

total = somar(1, 2, 3, 4, 5)
print(total)  # Isso imprimirá 15


#Parâmetros de Palavras-Chave Arbitrários (**kwargs):
"""
- Parâmetros **kwargs permitem que uma função aceite um número arbitrário de argumentos com nomes em um dicionário.
- O duplo asterisco (**) antes do nome "kwargs" é uma convenção, mas você pode escolher qualquer nome.
- Esses parâmetros são úteis quando você deseja passar argumentos nomeados para uma função e manipulá-los em um dicionário.
"""
#Exemplo de **kwargs:
def imprimir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_info(nome="Alice", idade=30, cidade="Exemplo")

#Neste exemplo, a função imprimir_info aceita argumentos nomeados arbitrários e imprime cada par chave-valor.

#**Combinando *args e kwargs:
#Você pode combinar *args e **kwargs em uma única função se precisar lidar com argumentos posicionais e nomeados arbitrários.
#Exemplo de combinação de *args e **kwargs:
def exemplo_combinado(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"Outros argumentos posicionais (args): {args}")
    print(f"Outros argumentos nomeados (kwargs): {kwargs}")

exemplo_combinado(1, 2, 3, 4, nome="Alice", idade=30)

#Neste exemplo, a função aceita argumentos posicionais a e b, bem como argumentos arbitrários em *args e **kwargs.
#Parâmetros arbitrários oferecem flexibilidade ao criar funções que podem ser usadas para uma variedade de casos, tornando seu código mais versátil e dinâmico. No entanto, é importante documentar claramente como a função deve ser usada, já que a flexibilidade adicional pode tornar o código menos autoexplicativo.

#noqa

# COMMAND ----------

# DBTITLE 1,Argumentos
#O desempacotamento de argumentos, também conhecido como "argumentos desempacotados" em Python, é uma técnica que permite passar argumentos de uma sequência, como uma tupla ou uma lista, para uma função como argumentos individuais. Isso pode ser especialmente útil quando você deseja chamar uma função que espera um número específico de argumentos, mas você já tem os valores organizados em uma sequência.

#Como Funciona o Desempacotamento de Argumentos:
#1 - Preparação da Sequência: Você começa com uma sequência de valores, como uma tupla ou uma lista, que contém os valores que deseja passar para a função.
#2 - Desempacotamento: Usando o operador *, você desempacota os valores da sequência e os passa como argumentos individuais para a função. Isso é feito durante a chamada da função.

#Exemplo de Desempacotamento de Argumentos:
#Suponha que você tenha uma função soma que espera dois argumentos individuais e deseja somar os valores de uma tupla:
def soma(a, b):
    return a + b

valores = (3, 5)

# Desempacotando os valores da tupla usando "*"
resultado = soma(*valores)

#Neste exemplo:

#'valores' é uma tupla que contém os valores (3, 5).
#Quando você chama 'soma(*valores)', o operador '*' desempacota a tupla e a função 'soma' recebe os valores como argumentos individuais, ou seja, 'a' recebe 3 e 'b' recebe 5.
#O resultado da função será a soma dos valores, que é 8.
#Vantagens do Desempacotamento de Argumentos: 
# - Permite reutilizar sequências de valores existentes para chamar funções que esperam argumentos individuais.
# - Torna o código mais legível e limpo, pois você não precisa acessar elementos da sequência explicitamente durante a chamada da função.

#noqa

# COMMAND ----------

# MAGIC %md #Funções Anônimas
# MAGIC
# MAGIC Também conhecidas como funções lambda, são funções pequenas e sem nome que podem ser usadas quando você precisa de uma função temporária para uma tarefa específica. As funções lambda são definidas usando a palavra-chave lambda e são frequentemente usadas em conjunto com funções como map(), filter(), sorted(), e em qualquer situação em que você deseja uma função simples e rápida.

# COMMAND ----------

#Sintaxe das Funções Lambda:
lambda argumentos: expressao
"""
- lambda é a palavra-chave que inicia a definição da função lambda.
- argumentos são os parâmetros da função lambda.
- expressao é o resultado que a função lambda deve retornar.
"""
#Exemplo de Função Lambda Simples:
soma = lambda a, b: a + b
resultado = soma(3, 5)
print(resultado)  # Isso imprimirá 8. Neste exemplo, a função lambda lambda a, b: a + b aceita dois argumentos, a e b, e retorna sua soma.

#Características das Funções Lambda:
"""
1 - Simplicidade: As funções lambda são concisas e podem ser definidas em uma única linha. Elas são úteis para funções simples.
2 - Expressões: A expressão após os dois pontos (:) é avaliada e seu resultado é retornado automaticamente. Não é necessário usar a palavra-chave return.
3 - Uso em Funções de Ordem Superior: Funções lambda são frequentemente usadas com funções de ordem superior, como map(), filter(), sorted(), que esperam uma função como argumento.
"""

#Exemplos de Uso de Funções Lambda:
#Map(): Aplicar uma função a cada elemento de uma sequência (lista, tupla, etc.).
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))

#Filter(): Filtrar elementos com base em uma condição.
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))

#Ordenação Personalizada: Ordenar uma lista com base em critérios específicos.
pessoas = [{"nome": "Alice", "idade": 30}, {"nome": "Bob", "idade": 25}]
ordenado = sorted(pessoas, key=lambda x: x['idade'])

#Funções lambda são limitadas em termos de complexidade. Elas são destinadas a funções simples. Se você precisar de uma função mais complexa, é melhor definir uma função regular usando def.

#noqa

# COMMAND ----------

#noqa
