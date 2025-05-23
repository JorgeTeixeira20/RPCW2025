
import json
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, XSD
import os

# Carregar a ontologia anterior
g = Graph()
g.parse("ex2/med_tratamentos.ttl", format="turtle")

# Namespace consistente
EX = Namespace("http://www.example.org/disease-ontology#")
g.bind("ex", EX)

# Carregar dados dos doentes
with open("doentes.json", "r", encoding="utf-8") as f:
    doentes = json.load(f)

# Adicionar instâncias de Patient
for i, doente in enumerate(doentes, start=1):
    nome = doente["nome"].strip()
    sintomas = doente["sintomas"]
    paciente_uri = URIRef(EX + f"paciente{i}")

    g.add((paciente_uri, RDF.type, EX.Patient))
    g.add((paciente_uri, EX.name, Literal(nome, datatype=XSD.string)))

    for sintoma in sintomas:
        sintoma_uri = URIRef(EX + sintoma.strip().replace(" ", "_").replace("-", "_"))
        g.add((paciente_uri, EX.exhibitsSymptom, sintoma_uri))

# Garantir pasta
os.makedirs("ex2", exist_ok=True)

# Guardar TTL final
g.serialize(destination="ex2/med_doentes.ttl", format="turtle")
print("Ficheiro criado em ex2/med_doentes.ttl")
