# Databricks notebook source
# 1.Escreva um programa que imprima todos os números pares entre 0 e 100.

# Usando compreensão de lista para encontrar todos os números pares entre 0 e 100

numeros_pares = [num for num in range(101) if num % 2 == 0]

# Imprimindo os números pares
print("Números pares entre 0 e 100:")
print(numeros_pares)

