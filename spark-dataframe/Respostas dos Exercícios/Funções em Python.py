# Databricks notebook source
# 1. Soma de Dois Números
def soma(a, b):
    return a + b

# 2. Maior de Três Números
def maior_de_tres(a, b, c):
    return max(a, b, c)

# 3. Verificador de Palíndromo
def verifica_palindromo(string):
    return string == string[::-1]

# 4. Calculadora de Média
def calcula_media(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0

# 5. Contagem de Vogais
def conta_vogais(string):
    vogais = "aeiouAEIOU"
    return sum(1 for char in string if char in vogais)

# 6. Fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# 7. Conversor de Temperatura
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 8. Verificador de Número Primo
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# 9. Ordenação de Lista
def ordena_lista(lista):
    return sorted(lista)

# 10. Cálculo de Juros Compostos
def juros_compostos(principal, taxa, anos):
    return principal * (1 + taxa/100)**anos

# Exemplos de uso:
print(soma(2, 3))
print(maior_de_tres(10, 5, 8))
print(verifica_palindromo("radar"))
print(calcula_media([1, 2, 3, 4, 5]))
print(conta_vogais("Python é incrível!"))
print(fatorial(5))
print(celsius_para_fahrenheit(25))
print(eh_primo(17))
print(ordena_lista([5, 2, 9, 1, 3]))
print(juros_compostos(1000, 5, 3))


# COMMAND ----------

def valores_repetidos(lista):
    # Crie um dicionário para contar a frequência de cada valor na lista
    frequencia = {}
    
    # Inicialize uma lista vazia para armazenar os valores repetidos
    repetidos = []
    
    # Percorra a lista e atualize o dicionário de frequência
    for valor in lista:
        if valor in frequencia:
            frequencia[valor] += 1
        else:
            frequencia[valor] = 1
    
    # Percorra o dicionário de frequência e encontre os valores repetidos
    for valor, contagem in frequencia.items():
        if contagem > 1:
            repetidos.append(valor)
    
    # Exiba os valores repetidos
    if repetidos:
        print("Valores repetidos na lista:")
        for valor in repetidos:
            print(valor)
    else:
        print("Não há valores repetidos na lista.")

# Exemplo de uso da função:
minha_lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
valores_repetidos(minha_lista)


# COMMAND ----------

# Exercício 1: Função para calcular o custo com imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    # Calcula o valor do imposto
    imposto = custo * (taxaImposto / 100)
    
    # Calcula o custo total com imposto
    custo_com_imposto = custo + imposto
    
    # Retorna o custo total com imposto
    return custo_com_imposto

# Exemplo de uso:
taxa = 10  # 10% de imposto
custo_item = 50
custo_total = somaImposto(taxa, custo_item)
print(f'O custo total com imposto é: {custo_total}')


# COMMAND ----------

# Exercício 2: Função para contar a quantidade de dígitos em um número inteiro.
def quantidade_digitos(numero):
    # Converte o número para string e calcula o comprimento da string
    return len(str(numero))

# Exemplo de uso:
num = int(input('Digite um número inteiro: '))
qtde = quantidade_digitos(num)
print(f'O número {num} possui {qtde} dígito(s).')


# COMMAND ----------

# Exercício 3: Função para verificar se um número é positivo, negativo ou zero.
def verifica_positivo_negativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Exemplo de uso:
num = int(input('Digite um número: '))
resultado = verifica_positivo_negativo(num)
print(f'O resultado é: {resultado}')


# COMMAND ----------

# Exercício 4: Função para inverter um número inteiro.
def reverso_numero(numero):
    # Converte o número para string, inverte e converte de volta para inteiro
    return int(str(numero)[::-1])

# Exemplo de uso:
num = 127
reverso = reverso_numero(num)
print(f'O reverso de {num} é: {reverso}')


# COMMAND ----------

# Exercício 5: Função para calcular o MDC de dois números usando recursão.
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Exemplo de uso:
num1 = 48
num2 = 18
resultado = mdc(num1, num2)
print(f'O MDC de {num1} e {num2} é: {resultado}')


# COMMAND ----------

# Exercício 9: Função para converter a notação de 24 horas para 12 horas.
def converte_hora(hora24):
    partes = hora24.split(":")
    horas = int(partes[0])
    minutos = int(partes[1])
    
    if horas >= 12:
        periodo = "P.M"
        if horas > 12:
            horas -= 12
    else:
        periodo = "A.M"
        if horas == 0:
            horas = 12
    
    return f"{horas}:{minutos:02d} {periodo}"

# Exemplo de uso:
hora = input('Digite a hora no formato 24 horas (hh:mm): ')
hora12 = converte_hora(hora)
print(f'A hora no formato 12 horas é: {hora12}')


# COMMAND ----------

# Exercício 10: Função para inverter o nome do usuário em maiúsculas.
def inverte_nome(nome):
    # Converte o nome para maiúsculas, inverte e retorna
    nome_maiusculo = nome.upper()
    nome_invertido = nome_maiusculo[::-1]
    return nome_invertido

# Exemplo de uso:
nome = input('Digite seu nome: ')
nome_invertido = inverte_nome(nome)
print(f'Seu nome invertido em maiúsculas é: {nome_invertido}')


# COMMAND ----------

# Exercício 11: Função para converter a data de nascimento em formato estendido.
def converte_mes_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    partes = data.split("/")
    dia = partes[0]
    mes = meses[int(partes[1]) - 1]
    ano = partes[2]
    return f'Você nasceu em {dia} de {mes} de {ano}.'

# Exemplo de uso:
data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')
data_extenso = converte_mes_extenso(data_nascimento)
print(data_extenso)


# COMMAND ----------



# COMMAND ----------

#noqa
