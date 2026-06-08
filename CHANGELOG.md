# Changelog

Tutte le modifiche rilevanti a questo progetto sono documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/it/1.1.0/)
e il progetto aderisce al [Versionamento Semantico](https://semver.org/lang/it/).

## [Non rilasciato]

### Aggiunto

- README disponibile in inglese (`README.md`, default) e italiano
  (`README.it.md`), con link reciproci.

## [0.1.0] - 2026-06-08

### Aggiunto

- CLI interattiva per la gestione delle spese domestiche con tre operazioni:
  aggiunta di una spesa, report mensile e top 10 delle spese maggiori.
- Persistenza delle spese su file CSV (`storico_spese.csv`).
- Architettura a quattro layer (domain, application, infrastructure, interfaces)
  secondo i principi di Clean Architecture e Domain-Driven Design, con i comandi
  CLI realizzati tramite il pattern Command.
- Motore di reporting intercambiabile: aggregazione in Python in-memory (default,
  zero dipendenze) oppure in SQL con DuckDB (extra opzionale `analytics`),
  selezionabile a runtime tramite la variabile d'ambiente `GESTORE_SPESE_ENGINE`.
- Console script `gestore-spese` come entry point.
- Suite di test con pytest e misura della coverage; type checking statico con
  mypy (strict); lint e formattazione con ruff.
- Integrazione continua su GitHub Actions (Python 3.10, 3.11, 3.12) con upload
  della coverage su Codecov.
- Documentazione API generata con Sphinx e pubblicata su GitHub Pages.
