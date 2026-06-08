"""Contratto astratto del provider di reporting (aggregazione in lettura)."""

from __future__ import annotations

from abc import ABC, abstractmethod

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa


class AbstractReportingProvider(ABC):
    """Porta di reporting: fornisce i report aggregati in sola lettura.

    Astrae *dove* avviene l'aggregazione, così il motore di calcolo (Python
    in-memory oppure SQL/DuckDB) può essere scambiato senza impatto sui casi
    d'uso e sui layer superiori (Dependency Inversion).
    """

    @abstractmethod
    def report_mensile(self) -> list[AbstractReportMensileDto]:
        """Ritorna i totali mensili in ordine di data decrescente.

        :return: totali mensili in ordine di data decrescente
        :rtype: list[AbstractReportMensileDto]
        """

    @abstractmethod
    def top_10(self) -> list[AbstractSpesa]:
        """Ritorna le 10 spese di importo maggiore.

        :return: le prime 10 spese per importo decrescente
        :rtype: list[AbstractSpesa]
        """
