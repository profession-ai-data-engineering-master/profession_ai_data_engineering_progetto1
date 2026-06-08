"""Caso d'uso: le 10 spese di importo maggiore."""

from __future__ import annotations

from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.application.use_cases.abstract_use_case import AbstractUseCase
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa


class Top10SpeseUseCase(AbstractUseCase[None, list[AbstractSpesa]]):
    """Restituisce le 10 spese maggiori delegando al provider di reporting.

    L'ordinamento e la selezione (in Python o in SQL) dipendono dal motore
    iniettato tramite :class:`AbstractReportingProvider`.
    """

    def __init__(self, provider: AbstractReportingProvider) -> None:
        self._provider = provider

    def execute(self, dati: None = None) -> list[AbstractSpesa]:
        """Ritorna le prime 10 spese per importo decrescente.

        :param dati: non utilizzato (il caso d'uso non richiede input)
        :type dati: None
        :return: le prime 10 spese per importo decrescente
        :rtype: list[AbstractSpesa]
        """
        return self._provider.top_10()
