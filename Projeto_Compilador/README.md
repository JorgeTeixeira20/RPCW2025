# 📚 Portal de Mestrados em Portugal

Este projeto é uma aplicação web interativa que permite explorar, visualizar, adicionar e analisar cursos de mestrado oferecidos por várias universidades portuguesas. Foi desenvolvido no âmbito da unidade curricular de **Representação do Conhecimento e Raciocínio Web (RPCW)**, utilizando tecnologias semânticas e web scraping.

---

## Grupo de Trabalho

- **Jorge Teixeira** - PG55965 - [JorgeTeixeira20](https://github.com/JorgeTeixeira20) 
- **Rui Pinto** - PG56010 - [RuiPintoUM](https://github.com/RuiPintoUM)
- **Pedro Azevedo** - PG57897 - [Pexometro](https://github.com/Pexometro)

---

## 📦 Índice

1. [Objetivos e Motivação](#objetivos-e-motivação)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Funcionalidades](#funcionalidades)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Detalhes Técnicos](#detalhes-técnicos)
6. [Como Executar](#como-executar)

---

## 🎯 Objetivos e Motivação

- Criar uma ontologia para representar cursos de mestrado, universidades, escolas e áreas científicas.
- Recolher dados reais a partir de websites oficiais e transformá-los em RDF com significado semântico.
- Desenvolver uma interface web que permita:
  - Navegar por universidades e escolas.
  - Filtrar e pesquisar mestrados.
  - Visualizar estatísticas por área científica.
  - Adicionar novos cursos via formulário.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** – Linguagem principal.
- **Flask** – Framework web para o back-end.
- **RDFlib** – Manipulação de grafos RDF e serialização `.ttl`.
- **SPARQL** – Consultas à ontologia.
- **HTML + CSS + Jinja2** – Front-end dinâmico.
- **BeautifulSoup + requests** – Web scraping.

---

## 🌐 Funcionalidades

- 📍 Listagem de universidades com design moderno.
- 🏫 Escolas e departamentos por universidade.
- 🎓 Visualização e detalhe dos cursos de mestrado.
- 🔍 Pesquisa por nome e filtro por área científica.
- 📊 Estatísticas globais ou por universidade.
- ➕ Adição de novos mestrados via formulário.
- 🧠 Ontologia em formato `.ttl`, representando todas as entidades semânticas.

---

## 📁 Estrutura do Projeto

```
cursos_portugal/
├── app.py                   # Aplicação principal Flask
├── templates/               # Templates HTML Jinja2
├── static/                  # Ficheiros CSS e imagens
├── scripts/                 # Scripts de scraping/povoamento
│   ├── uminho/
│   ├── utad/
│   ├── coimbra/
│   └── fctnova/
├── ontologias/
│   ├── cursos.ttl           # Ontologia base
│   └── cursos_povoados.ttl  # Ontologia com dados reais
```

---

## 🧪 Detalhes Técnicos

### Ontologia RDF

- Criada com vocabulário próprio:
  - `:Universidade`, `:Escola`, `:Mestrado`, `:UnidadeCurricular`, `:AreaCientifica`
  - Propriedades: `temEscola`, `ofereceCurso`, `pertenceA`, `temArea`, `temRegime`, etc.
- Representada em `.ttl` (Turtle), manipulada com `rdflib`.

### Web Scraping

- Feito com `requests` + `BeautifulSoup`.
- Script específico para cada universidade:
  - Extrai nome, escola, área científica, unidades curriculares, regime, localização e website.

### Página de Estatísticas

- Gera ranking de áreas científicas com mais mestrados.
- Permite visualização geral ou filtrada por universidade.

---

## ▶️ Como Executar

1. Instala dependências:
```bash
pip install flask rdflib beautifulsoup4
```

2. Executa a aplicação:
```bash
python app.py
```

3. Abre o browser:
```
http://127.0.0.1:5000
```

---

## 👨‍💻 Autores

- **Jorge Teixeira** - PG55965 - [JorgeTeixeira20](https://github.com/JorgeTeixeira20)
- **Rui Pinto** - PG56010 - [RuiPintoUM](https://github.com/RuiPintoUM)
- **Pedro Azevedo** - PG57897 - [Pexometro](https://github.com/Pexometro)

---

## 📚 Nota Final

Este projeto demonstrou a aplicação de ontologias no desenvolvimento web, aliando scraping, processamento semântico e visualização. É uma plataforma escalável que poderá, futuramente, integrar outras fontes de dados como a API da DGES.