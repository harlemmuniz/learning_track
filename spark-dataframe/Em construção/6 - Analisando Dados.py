# Databricks notebook source
import random

names = ["Gabriela","Celso","João","Pedro","José"]
surnames = ["Almeida","Pereira","Cavalcante","Gomes","da Silva"]
#salaries = [500*random.randint(1,30) for _ in range(10)]
metric = [random.randint(0,30) for _ in range(10)]
year = [random.randint(2000,2020) for _ in range(10)]

def generate_random_person(names, surnames, salaries, year):
    return {"nome":random.sample(names,1)[0],
            "sobrenome":random.sample(surnames,1)[0],
            "metric":random.sample(metric,1)[0],
            "ano":random.sample(year,1)[0]}

def generate_people(k):
    return [generate_random_person(names, surnames, metric, year) for _ in range(k)]

# COMMAND ----------

import pandas as pd

df = pd.DataFrame(generate_people(50),
                  columns=["nome","sobrenome","metric","ano"])

# df.to_csv("random_people.csv")
# df = pd.read_csv("random_people.csv")

# COMMAND ----------

df

# COMMAND ----------

df[df["nome"]=="Celso"]

# COMMAND ----------

df_high = df[df["metric"]>=20]

# COMMAND ----------

df_low = df.loc[df["metric"]<20]
#df_low = df.loc[df["metric"]<20,"metric"]

# COMMAND ----------

#noqa
