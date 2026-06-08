"""Provider di reporting basato su DuckDB: aggregazione in SQL.

Richiede l'extra opzionale ``analytics`` (``pip install gestore-spese[analytics]``).
"""

from __future__ import annotations

from os import path

import duckdb

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.entities.spesa import Spesa


class DuckDbReportingProvider(AbstractReportingProvider):
    """Calcola i report con DuckDB, leggendo il CSV direttamente in SQL.

    Dimostra il *push-down* dell'aggregazione: il calcolo (``GROUP BY``/``SUM``,
    ``ORDER BY``/``LIMIT``) avviene nel motore dati invece che in Python. Legge
    la stessa sorgente CSV usata dalla persistenza, senza modificarla.
    """

    _QUERY_REPORT_MENSILE = (
        "SELECT date_trunc('month', data) AS mese, SUM(importo) AS totale "
        "FROM read_csv_auto(?, header=true) "
        "GROUP BY mese ORDER BY mese DESC"
    )

    _QUERY_TOP_10 = (
        "SELECT data, descrizione, importo "
        "FROM read_csv_auto(?, header=true) "
        "ORDER BY importo DESC, data DESC LIMIT 10"
    )

    def __init__(self, filepath: str = "storico_spese.csv") -> None:
        self._filepath = filepath

    def _sorgente_disponibile(self) -> bool:
        """Indica se il file CSV esiste ed è non vuoto.

        Replica il comportamento del datasource: con sorgente assente i report
        sono liste vuote, senza interrogare il motore.

        :return: True se la sorgente è interrogabile, altrimenti False
        :rtype: bool
        """
        return path.exists(self._filepath) and path.getsize(self._filepath) > 0

    def report_mensile(self) -> list[AbstractReportMensileDto]:
        """Aggrega i totali mensili in SQL (``GROUP BY``/``SUM``).

        :return: totali mensili in ordine di data decrescente
        :rtype: list[AbstractReportMensileDto]
        """
        if not self._sorgente_disponibile():
            return []
        righe = duckdb.execute(self._QUERY_REPORT_MENSILE, [self._filepath]).fetchall()
        report: list[AbstractReportMensileDto] = [
            ReportMensileDto(riga[0], float(riga[1])) for riga in righe
        ]
        return report

    def top_10(self) -> list[AbstractSpesa]:
        """Seleziona le 10 spese maggiori in SQL (``ORDER BY``/``LIMIT``).

        :return: le prime 10 spese per importo decrescente
        :rtype: list[AbstractSpesa]
        """
        if not self._sorgente_disponibile():
            return []
        righe = duckdb.execute(self._QUERY_TOP_10, [self._filepath]).fetchall()
        spese: list[AbstractSpesa] = [Spesa(riga[0], riga[1], float(riga[2])) for riga in righe]
        return spese
