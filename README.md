# Household Expense Manager

📖 **English** · [Italiano](README.it.md)

[![CI](https://github.com/profession-ai-data-engineering-master/profession_ai_data_engineering_progetto1/actions/workflows/ci.yml/badge.svg)](https://github.com/profession-ai-data-engineering-master/profession_ai_data_engineering_progetto1/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
[![codecov](https://codecov.io/gh/profession-ai-data-engineering-master/profession_ai_data_engineering_progetto1/branch/main/graph/badge.svg)](https://codecov.io/gh/profession-ai-data-engineering-master/profession_ai_data_engineering_progetto1)
![License](https://img.shields.io/badge/license-MIT-green)
[![Docs](https://img.shields.io/badge/docs-online-8a2be2)](https://profession-ai-data-engineering-master.github.io/profession_ai_data_engineering_progetto1/)

A command-line application to track personal expenses, produce a monthly report
and surface the most significant spendings. Data is persisted to a simple CSV
file.

The project was built as a portfolio exercise: beyond meeting the functional
requirements, it is structured around the principles of **Clean Architecture**
and **Domain-Driven Design**, with test coverage, static type checking and CI.

> The interactive CLI is in Italian (the application's user-facing language).

## Features

- **Add an expense** — date, description and amount, saved to CSV.
- **Monthly report** — total spending aggregated by year/month, in descending date order.
- **Top 10 expenses** — the ten largest expenses by amount.

## Usage example

![Household Expense Manager CLI demo](docs/assets/cli-demo.svg)

<details>
<summary>Text transcript of the session</summary>

```text
$ gestore-spese
Gestore Spese
Scegli un'opzione (inserisci la chiave):
[1] Aggiungi una Spesa
[2] Mostra Report Mensile
[3] Mostra Top 10 delle Spese
[esci] Esci dal programma
> 1
Inserisci la data della nuova spesa (dd/mm/yyyy): 01/05/2025
Inserisci la descrizione della nuova spesa: spesa di test
Inserisci l'importo della nuova spesa: 30.41
Aggiunta con successo nuova Spesa: Data: 01/05/2025, Descrizione: 'spesa di test', Importo: 30.41
...
> 2
Report Mensile:
Data: 2025-05, Importo: 830.41
```

</details>

## Requirements

- Python **>= 3.10**
- No external runtime dependencies for the core functionality (standard library
  only). The SQL reporting engine is **optional** (the `analytics` extra, based
  on DuckDB) — see [Reporting engine](#reporting-engine-in-memory-vs-sql).

## Installation

```bash
# clone the repository, then:
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

## Running

```bash
gestore-spese
```

Alternatively, without installing the console script:

```bash
python -m gestore_spese.interfaces.cli.main
```

Expenses are saved to a `storico_spese.csv` file in the current directory.

## Architecture

The code is organized into four concentric layers; dependencies always point
towards the domain (Dependency Inversion through abstract classes):

```
interfaces/      CLI (Command pattern) + composition root
   │  depends on
application/     use cases (Add / MonthlyReport / Top10) + DTOs
   │  depends on
domain/          entities (Spesa), repository contracts, services  ← core, no dependencies
   ▲  implemented by
infrastructure/  CSV persistence (datasource + repository)
```

- **`domain`** — the `Spesa` entity with its validation rules, plus the abstract repository and service contracts. It depends on no other layer.
- **`application`** — the use cases that orchestrate the domain, and the monthly report DTO.
- **`infrastructure`** — the concrete CSV persistence implementation, behind the domain abstractions.
- **`interfaces`** — the CLI: each operation is a *Command* (Command pattern → open for extension, closed for modification) and `GestoreSpeseCli` acts as the *composition root* wiring the dependencies.
- **Swappable reporting** — read-only reports go through the `AbstractReportingProvider` port, with two implementations (Python in-memory by default, optional DuckDB/SQL) selectable at runtime. See [Reporting engine](#reporting-engine-in-memory-vs-sql).

The design choices (DDD, SOLID, patterns adopted) are described in the module
docstrings, available in the [API documentation](#documentation).

## Project structure

```
src/gestore_spese/
├── domain/
│   ├── entities/          # AbstractSpesa, Spesa
│   ├── repositories/      # AbstractSpesaRepository
│   └── services/          # AbstractSpesaService, SpesaService
├── application/
│   ├── dtos/              # ReportMensileDto
│   ├── ports/             # AbstractReportingProvider (reporting port)
│   ├── reporting/         # InMemoryReportingProvider (in-memory engine, default)
│   └── use_cases/         # AbstractUseCase, AggiungiSpesa/ReportMensile/Top10
├── infrastructure/
│   ├── persistence/
│   │   ├── datasources/   # SpesaDataSourceCsv
│   │   └── repositories/  # SpesaRepository
│   └── reporting/         # DuckDbReportingProvider + engine selection factory
└── interfaces/
    └── cli/               # commands/, main.py (GestoreSpeseCli + entry point)
tests/                     # pytest suite, mirroring src/
docs/                      # project brief
```

## Reporting engine (in-memory vs SQL)

The read-only reports (*Monthly Report* and *Top 10*) can be computed with two
interchangeable engines behind the same abstraction (`AbstractReportingProvider`):

- **in-memory (default)** — aggregation happens in Python; no external
  dependency;
- **DuckDB / SQL** — aggregation is *pushed down* into the data engine
  (*push-down*) and expressed in SQL (`GROUP BY`/`SUM`, `ORDER BY`/`LIMIT`),
  reading the CSV file directly.

> ⚠️ **Intellectual honesty.** On a household-expenses CSV the data volume is
> tiny: the SQL engine brings **no** performance benefit (it may even be
> marginally slower due to engine overhead). It is not an optimization: it is a
> demonstration of the data-engineering *push-down* pattern, and of how
> *Dependency Inversion* lets you swap the computation engine without touching
> the upper layers. The output of the two engines is identical.

To use the SQL engine, install the extra and set the environment variable:

```bash
pip install -e ".[analytics]"            # adds duckdb
GESTORE_SPESE_ENGINE=duckdb gestore-spese
```

Without the extra (or with the variable unset) the in-memory engine is used. If
you request `duckdb` but the extra is not installed, the app warns and falls
back automatically to in-memory.

## Development

Install the development dependencies and run the quality checks:

```bash
pip install -e ".[dev]"

ruff check .             # lint
ruff format --check .    # formatting
mypy src                 # static type checking (strict)
pytest                   # tests + coverage (90% threshold)
```

The same checks run in **CI** on GitHub Actions for Python 3.10, 3.11 and 3.12.

## Documentation

The API documentation is generated by Sphinx (from the reStructuredText
docstrings) and published on **GitHub Pages**:

🔗 https://profession-ai-data-engineering-master.github.io/profession_ai_data_engineering_progetto1/

To build it locally:

```bash
pip install -e ".[dev]"
sphinx-build -b html docs docs/_build/html
# open docs/_build/html/index.html
```

## Contributing

Development guidelines are in [CONTRIBUTING.md](CONTRIBUTING.md); notable changes
are tracked in [CHANGELOG.md](CHANGELOG.md).

## License

Distributed under the [MIT](LICENSE) license.
