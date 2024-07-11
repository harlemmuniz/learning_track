# Databricks notebook source
# 1.Escreva um programa que imprima todos os números pares entre 0 e 100.

# Usando compreensão de conjunto para encontrar todos os números pares entre 0 e 100

numeros_pares = {num for num in range(0, 101, 2)}  # Começa do 0, vai até 100, passo de 2

# Imprimindo os números pares
print("Números pares entre 0 e 100:")
print(numeros_pares)


# COMMAND ----------

# 2.Escreva um programa que calcule a soma de todos os números ímpares entre 0 e 1000.

# Usando compreensão de conjunto para encontrar todos os números ímpares entre 0 e 1000
numeros_impares = {num for num in range(1, 1001, 2)}

# Calculando a soma dos números ímpares
soma_impares = sum(numeros_impares)

# Imprimindo a soma dos números ímpares
print("A soma de todos os números ímpares entre 0 e 1000 é:", soma_impares)


# COMMAND ----------

# 3.Escreva um programa que leia uma lista de números inteiros e determine o maior número na lista.

# Solicita ao usuário para inserir uma lista de números inteiros separados por espaço
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista_numeros = [int(num) for num in entrada.split()]

# Usa a compreensão de conjunto para remover duplicatas
numeros_unicos = {num for num in lista_numeros}

# Determina o maior número na lista original
maior_numero = max(numeros_unicos)

# Imprime o maior número na lista
print("O maior número na lista é:", maior_numero)


# COMMAND ----------

# 4.Escreva um programa que converta uma temperatura em graus Celsius para graus Fahrenheit.

# Solicita ao usuário para inserir a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte Celsius para Fahrenheit usando a fórmula: (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Imprime a temperatura convertida em Fahrenheit
print("A temperatura de", celsius, "graus Celsius é igual a", fahrenheit, "graus Fahrenheit.")


# COMMAND ----------

# 5.Escreva um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

# Função para calcular o fatorial de um número
def calcular_fatorial(numero):
    # Caso base: fatorial de 0 é 1
    if numero == 0:
        return 1
    else:
        # Inicializa o fatorial como 1
        fatorial = 1
        # Multiplica os números de 1 até o número fornecido para calcular o fatorial
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

# Função principal
def main():
    # Solicita ao usuário para inserir o número
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))

    # Verifica se o número é negativo
    if numero < 0:
        print("O fatorial não está definido para números negativos.")
    else:
        # Calcula o fatorial e imprime o resultado
        resultado = calcular_fatorial(numero)
        print("O fatorial de", numero, "é:", resultado)

if __name__ == "__main__":
    main()


# COMMAND ----------

# 5.Escreva um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

# Solicita ao usuário para inserir o número inteiro para calcular o fatorial
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial do número usando um loop
for i in range(1, numero + 1):
    fatorial *= i

# Imprime o resultado
print("O fatorial de", numero, "é:", fatorial)


# COMMAND ----------

# 6.Escreva um programa que verifique se um número fornecido pelo usuário é um número primo.
# Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

# Função para verificar se um número é primo
def verificar_numero_primo(numero):
    # Verifica se o número é menor que 2, pois números menores que 2 não são primos
    if numero < 2:
        return False
    # Verifica se o número é divisível por qualquer número de 2 até a raiz quadrada do número + 1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Função principal
def main():
    # Solicita ao usuário para inserir o número
    numero = int(input("Digite um número inteiro para verificar se é primo: "))

    # Verifica se o número é primo e imprime o resultado
    if verificar_numero_primo(numero):
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")

if __name__ == "__main__":
    main()


# COMMAND ----------

# 6.Escreva um programa que verifique se um número fornecido pelo usuário é um número primo.
# Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

# Solicita ao usuário para inserir o número
numero = int(input("Digite um número inteiro para verificar se é primo: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Verifica se o número é divisível apenas por 1 e por ele mesmo
    divisores = {num for num in range(1, numero + 1) if numero % num == 0}
    if len(divisores) == 2:  # Se tiver exatamente 2 divisores (1 e o próprio número)
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")
else:
    print(numero, "não é um número primo.")


# COMMAND ----------

# 7.Escreva um programa que gere uma lista de todos os números perfeitos entre 1 e 1000.
# Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios positivos, excluindo ele mesmo.

# Função para verificar se um número é perfeito
def verificar_numero_perfeito(numero):
    soma_divisores = 0
    # Encontrar todos os divisores próprios do número
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    # Verificar se a soma dos divisores é igual ao número original
    return soma_divisores == numero

# Função principal
def main():
    numeros_perfeitos = []
    # Iterar através dos números de 1 a 1000
    for num in range(1, 1001):
        if verificar_numero_perfeito(num):
            numeros_perfeitos.append(num)
    # Imprimir os números perfeitos encontrados
    print("Números perfeitos entre 1 e 1000:", numeros_perfeitos)

if __name__ == "__main__":
    main()


# COMMAND ----------

# 7.Escreva um programa que gere uma lista de todos os números perfeitos entre 1 e 1000.
# Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios positivos, excluindo ele mesmo.

# Função para verificar se um número é perfeito
def verificar_numero_perfeito(numero):
    soma_divisores = sum({num for num in range(1, numero) if numero % num == 0})
    return soma_divisores == numero

# Lista para armazenar os números perfeitos encontrados
numeros_perfeitos = []

# Encontrando todos os números perfeitos entre 1 e 1000
for num in range(2, 1001):
    if verificar_numero_perfeito(num):
        numeros_perfeitos.append(num)

# Imprimindo a lista de números perfeitos
print("Números perfeitos entre 1 e 1000:", numeros_perfeitos)

