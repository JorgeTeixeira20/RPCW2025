# FICHA DE AFERIÇÃO MEDICINA

- **Nome** Jorge Teixeira 

- **Número de Aluno** PG55965


## Ex1

## EX2

### 11. Queries

**1.** - Quantas doenças estão presentes na ontologia?

```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT (COUNT(?doenca) AS ?totalDoencas)
WHERE {
  ?doenca a ex:Disease .
}
```

**2.** - Que doenças estão associadas ao sintoma "yellowish_skin"?

```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?doenca
WHERE {
  ?doenca a ex:Disease ;
          ex:hasSymptom ex:yellowish_skin .
}
```

**3.** - Que doenças estão associadas ao tratamento "exercise"?

```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?doenca
WHERE {
  ?doenca a ex:Disease ;
          ex:hasTreatment ex:exercise .
}
```

**4.** - Produz uma lista ordenada alfabeticamente com o nome dos doentes.

```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?nome
WHERE {
  ?paciente a ex:Patient ;
            ex:name ?nome .
}
ORDER BY ?nome
```
>  [!NOTE]
> Ontologia criada pela query foi guardada em "query-result.ttl", tendo sido adicionada à ontologia principal através 

### 12. 

```
PREFIX ex: <http://www.example.org/disease-ontology#>

CONSTRUCT {
  ?paciente ex:hasDisease ?doenca .
}
WHERE {
  {
    SELECT ?paciente ?doenca
    WHERE {
      # Total de sintomas da doença
      {
        SELECT ?doenca (COUNT(?sintoma) AS ?totalSintomas)
        WHERE {
          ?doenca a ex:Disease ;
                  ex:hasSymptom ?sintoma .
        }
        GROUP BY ?doenca
      }

      # Total de sintomas que o paciente tem dessa doença
      {
        SELECT ?paciente ?doenca (COUNT(?sintomaComum) AS ?totalDoPaciente)
        WHERE {
          ?doenca a ex:Disease ;
                  ex:hasSymptom ?sintomaComum .
          ?paciente a ex:Patient ;
                    ex:exhibitsSymptom ?sintomaComum .
        }
        GROUP BY ?paciente ?doenca
      }

      # Condição: o paciente tem todos os sintomas da doença
      FILTER(?totalSintomas = ?totalDoPaciente)
    }
  }
}
```

### 13.

```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?doenca (COUNT(?paciente) AS ?numDoentes)
WHERE {
  ?paciente a ex:Patient ;
            ex:hasDisease ?doenca .
}
GROUP BY ?doenca
ORDER BY DESC(?numDoentes)
```

### 14.
```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?sintoma (COUNT(?doenca) AS ?numDoencas)
WHERE {
  ?doenca a ex:Disease ;
          ex:hasSymptom ?sintoma .
}
GROUP BY ?sintoma
ORDER BY DESC(?numDoencas)
```


### 15.
```
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?tratamento (COUNT(?doenca) AS ?numDoencas)
WHERE {
  ?doenca a ex:Disease ;
          ex:hasTreatment ?tratamento .
}
GROUP BY ?tratamento
ORDER BY DESC(?numDoencas)
```