"""Caso d'uso: generazione del report mensile."""

from __future__ import annotations

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.application.use_cases.abstract_use_case import AbstractUseCase


class ReportMensileUseCase(AbstractUseCase[None, list[AbstractReportMensileDto]]):
    """Restituisce i totali mensili delegando al provider di reporting.

    L'aggregazione effettiva (in Python o in SQL) dipende dal motore iniettato
    tramite :class:`AbstractReportingProvider`: il caso d'uso resta agnostico.
    """

    def __init__(self, provider: AbstractReportingProvider) -> None:
        self._provider = provider

    def execute(self, dati: None = None) -> list[AbstractReportMensileDto]:
        """Ritorna i totali mensili in ordine di data decrescente.

        :param dati: non utilizzato (il caso d'uso non richiede input)
        :type dati: None
        :return: totali mensili in ordine di data decrescente
        :rtype: list[AbstractReportMensileDto]
        """
        return self._provider.report_mensile()
