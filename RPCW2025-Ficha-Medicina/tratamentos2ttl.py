
import pandas as pd
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF
import os

# Carregar a ontologia anterior
g = Graph()
g.parse("ex2/med_doencas.ttl", format="turtle")

# Namespace consistente
EX = Namespace("http://www.example.org/disease-ontology#")
g.bind("ex", EX)

# Carregar CSV de tratamentos
treatment_df = pd.read_csv("Disease_Treatment.csv")

# Formatador de URIs
def format_uri(name):
    return URIRef(EX + name.strip().replace(" ", "_").replace("-", "_").replace("__", "_"))

# Set para evitar duplicações
added_treatments = set()

# Associar tratamentos às doenças
for _, row in treatment_df.iterrows():
    disease_uri = format_uri(row['Disease'].strip())
    for col in row.index[1:]:
        treatment = row[col]
        if pd.notna(treatment):
            treatment_name = treatment.strip()
            treatment_uri = format_uri(treatment_name)

            if treatment_name not in added_treatments:
                g.add((treatment_uri, RDF.type, EX.Treatment))
                added_treatments.add(treatment_name)

            g.add((disease_uri, EX.hasTreatment, treatment_uri))

# Garantir pasta
os.makedirs("ex2", exist_ok=True)

# Guardar resultado
g.serialize(destination="ex2/med_tratamentos.ttl", format="turtle")
print("Ficheiro criado em ex2/med_tratamentos.ttl")


