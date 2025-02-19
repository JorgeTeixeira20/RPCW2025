# TPC 3 - Resolução Ficha Sobre História de Portugal

## b - Que classes estão definidas?
    ```
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

    select ?classe where {
    ?classe rdf:type owl:Class.
    }
    ```

## c - Que propriedades tem a classe "Rei"?
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select distinct ?prop where {
  ?s a :Rei .
  ?s ?prop ?o .
} order by ?prop
```

## d - Quantos reis aparecem na ontologia?
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select (count (?s) as ?triples) where {
  ?s a :Rei .
} 
```

## e - Calcula uma tabela com o seu nome, data de nascimento e cognome.
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?nome ?data ?cognome where {
	?s a :Rei .
	?s :nome ?nome .
   	?s :cognomes ?cognome .
    ?s :nascimento ?data .
} 
```

## f - Acrescenta à tabela anterior a dinastia em que cada rei reinou.
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?nome ?data ?cognome ?dinastia where {
	?s a :Rei .
	?s :nome ?nome .
   	?s :cognomes ?cognome .
    ?s :nascimento ?data .
    ?s :temReinado ?reinado.
    ?reinado :dinastia ?dinastia.
} 
```

## g - Qual a distribuição de reis pelas 4 dinastias?
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?dinastia ( count (?nome) as ?triples )  where {
	?s a :Rei .
	?s :nome ?nome .
   	?s :cognomes ?cognome .
    ?s :nascimento ?data .
    ?s :temReinado ?reinado.
    ?reinado :dinastia ?dinastia.
} GROUP BY ?dinastia
```

## h - Lista os descobrimentos (sua descrição) por ordem cronológica.
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?descricao where {
    ?descob a :Descobrimento .
    ?descob :data ?data .
    ?descob :notas ?descricao .
}
order by ?data
```

## i - Lista as várias conquistas, nome e data, com o nome do rei que reinava no momento.
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?nc ?dc ?nr where {
    ?conq a :Conquista .
    ?conq :nome ?nc .
    ?conq :data ?dc .
    ?conq :temReinado ?reinado .
    ?reinado :temMonarca ?rei .
    ?rei :nome ?nr .
}
```

## j - Calcula uma tabela com o nome, data de nascimento e número de mandatos de todos os presidentes portugueses.
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?np ?dn (COUNT(?nm) as ?triples) where {
	?p a :Presidente .
    ?p :nome ?np .
    ?p :nascimento ?dn .
    ?p :mandato ?nm
}
group by ?np ?dn
```

## k - Quantos mandatos teve o presidente Sidónio Pais? Em que datas iniciaram e terminaram esses mandatos?
```

```

## l - Quais os nomes dos partidos politicos presentes na ontologia?
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?nomepart where {
	?p a :Partido .
	?p :nome ?nomepart
}
```

## m - Qual a distribuição dos militantes por cada partido politico?
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

select ?nomepart (COUNT(?nummili) as ?triplets) where {
	?p a :Partido .
	?p :nome ?nomepart .
    ?p :temMilitante ?nummili .
}
Group by ?nomepart

```

## n - Qual o partido com maior número de presidentes militantes?
```

```

