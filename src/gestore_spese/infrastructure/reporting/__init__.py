"""Reporting infrastrutturale: motore SQL (DuckDB) e factory di selezione.

Il provider DuckDB non viene importato qui: dipende dall'extra opzionale
``analytics`` e viene caricato in modo lazy dalla factory, così l'import di
questo package non richiede ``duckdb``.
"""

from gestore_spese.infrastructure.reporting.reporting_provider_factory import (
    crea_reporting_provider,
)

__all__ = ["crea_reporting_provider"]
