
import pandas as pd
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, XSD
import os

# Criar grafo e namespace
g = Graph()
EX = Namespace("http://www.example.org/disease-ontology#")
g.bind("ex", EX)

# Carregar CSVs
syntoms_df = pd.read_csv("Disease_Syntoms.csv")
description_df = pd.read_csv("Disease_Description.csv")

# Função para formatar URIs
def format_uri(name):
    return URIRef(EX + name.strip().replace(" ", "_").replace("-", "_").replace("__", "_"))

# Sets para evitar duplicação
added_symptoms = set()
added_diseases = set()

# Adicionar doenças e sintomas
for _, row in syntoms_df.iterrows():
    disease_name = row['Disease'].strip()
    disease_uri = format_uri(disease_name)

    if disease_name not in added_diseases:
        g.add((disease_uri, RDF.type, EX.Disease))
        added_diseases.add(disease_name)

    for col in row.index[1:]:
        symptom = row[col]
        if pd.notna(symptom):
            symptom_name = symptom.strip()
            symptom_uri = format_uri(symptom_name)

            if symptom_name not in added_symptoms:
                g.add((symptom_uri, RDF.type, EX.Symptom))
                added_symptoms.add(symptom_name)

            g.add((disease_uri, EX.hasSymptom, symptom_uri))

# Adicionar descrições
for _, row in description_df.iterrows():
    disease_uri = format_uri(row['Disease'].strip())
    desc = Literal(row['Description'].strip(), datatype=XSD.string)
    g.add((disease_uri, EX.descricao, desc))

# Criar pasta se não existir
os.makedirs("ex2", exist_ok=True)

# Guardar TTL
g.serialize(destination="ex2/med_doencas.ttl", format="turtle")
print("Ficheiro criado em ex2/med_doencas.ttl")



