# TPC 6

## Objetivo

**Povoar a ontologia** cinema-base.ttl desenvolvida na aula TP6 com 500 filmes.

> [!NOTE]
> A informação sobre os filmes foi obtida através do script abaixo.

```sh
./get_imdb_movie_files
```

### Concatenar a informação

- Cria um ficheiro `movies.json` na diretoria `data` com a informação sobre os mesmos concatenada.

```sh
python3 concatenate_data.py
```

### Criar um novo ficheiro Turtle

Juntando assim toda a informação numa ontologia nova e redirecionando-a para um novo ficheiro.

```sh
python3 populate.py > cinema.ttl
```

