"""Factory che seleziona il motore di reporting in base alla configurazione."""

from __future__ import annotations

import os

from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.application.reporting.in_memory_reporting_provider import (
    InMemoryReportingProvider,
)
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService

#: Variabile d'ambiente che seleziona il motore di reporting.
ENV_VARIABILE_MOTORE = "GESTORE_SPESE_ENGINE"
#: Valore per il motore SQL DuckDB.
MOTORE_DUCKDB = "duckdb"
#: Valore (e default) per il motore Python in-memory.
MOTORE_INMEMORY = "inmemory"


def crea_reporting_provider(
    service: AbstractSpesaService,
    csv_filepath: str,
    motore: str | None = None,
) -> AbstractReportingProvider:
    """Crea il provider di reporting secondo il motore richiesto.

    Se ``motore`` non è passato, viene letto dalla variabile d'ambiente
    ``GESTORE_SPESE_ENGINE``; il default è il motore Python in-memory. Il valore
    ``duckdb`` seleziona il motore SQL: se l'extra ``analytics`` non è
    installato si ricade automaticamente sull'in-memory, con un avviso, così
    l'applicazione non si interrompe mai.

    :param AbstractSpesaService service: servizio usato dal motore in-memory
    :param str csv_filepath: percorso del CSV letto dal motore DuckDB
    :param motore: motore richiesto (``inmemory`` o ``duckdb``); se ``None``
        viene letto dall'ambiente
    :type motore: str | None
    :return: il provider di reporting selezionato
    :rtype: AbstractReportingProvider
    """
    if motore is None:
        motore = os.environ.get(ENV_VARIABILE_MOTORE, MOTORE_INMEMORY)

    if motore.strip().lower() == MOTORE_DUCKDB:
        duckdb_provider = _prova_a_creare_duckdb_provider(csv_filepath)
        if duckdb_provider is not None:
            return duckdb_provider
        print(
            "Avviso: motore 'duckdb' richiesto ma l'extra 'analytics' non è "
            "installato; uso il motore in-memory. "
            "Installa con: pip install gestore-spese[analytics]"
        )

    return InMemoryReportingProvider(service)


def _prova_a_creare_duckdb_provider(csv_filepath: str) -> AbstractReportingProvider | None:
    """Istanzia il provider DuckDB, se l'extra ``analytics`` è disponibile.

    L'import è lazy: senza ``duckdb`` installato ritorna ``None`` invece di
    propagare l'``ImportError``.

    :param str csv_filepath: percorso del CSV letto dal motore DuckDB
    :return: il provider DuckDB, oppure ``None`` se ``duckdb`` non è installato
    :rtype: AbstractReportingProvider | None
    """
    try:
        from gestore_spese.infrastructure.reporting.duckdb_reporting_provider import (
            DuckDbReportingProvider,
        )
    except ImportError:
        return None
    return DuckDbReportingProvider(csv_filepath)
