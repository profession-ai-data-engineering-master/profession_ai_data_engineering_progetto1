# Come contribuire

Grazie per l'interesse verso il progetto! Questa guida riassume come preparare
l'ambiente, eseguire i controlli di qualità e proporre modifiche.

## Ambiente di sviluppo

Requisiti: Python **>= 3.10**.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e ".[dev]"            # strumenti di sviluppo + DuckDB
```

L'extra `dev` installa anche `duckdb`, così i test coprono entrambi i motori di
reporting (in-memory e SQL).

## Controlli di qualità

Prima di aprire una pull request, esegui in locale gli stessi controlli della CI:

```bash
ruff check .             # lint
ruff format --check .    # formattazione
mypy src                 # type checking statico (strict)
pytest                   # test + coverage (soglia 90%)
```

Per generare la documentazione:

```bash
sphinx-build -b html docs docs/_build/html
```

## Workflow dei contributi

- Una **issue per attività** e un **branch dedicato** per ogni issue, con base
  `main`.
- Una **pull request per issue**, collegata all'issue che chiude.
- Messaggi di commit secondo la convenzione del repo: `Mn #<issue>: descrizione`.
- La PR può essere unita solo con la **CI verde** (lint, type check e test su
  Python 3.10, 3.11 e 3.12).

## Stile del codice

- Architettura a layer (domain, application, infrastructure, interfaces): le
  dipendenze puntano sempre verso il dominio.
- Ogni componente ha un contratto astratto e un'implementazione concreta
  (Dependency Inversion).
- Docstring in formato reStructuredText (`:param:`, `:return:`, `:rtype:`),
  coerenti con quelle esistenti.
- Mantieni la coverage sopra la soglia e i controlli `ruff`/`mypy` puliti.
