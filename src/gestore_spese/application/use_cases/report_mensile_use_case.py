"""Caso d'uso: generazione del report mensile."""

from __future__ import annotations

from itertools import groupby

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.use_cases.abstract_use_case import AbstractUseCase
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class ReportMensileUseCase(AbstractUseCase[None, list[AbstractReportMensileDto]]):
    """Aggrega le spese per anno/mese e ne somma gli importi.

    Restituisce i totali mensili ordinati per data decrescente.
    """

    def __init__(self, service: AbstractSpesaService) -> None:
        self._service = service

    def execute(self, dati: None = None) -> list[AbstractReportMensileDto]:
        """Calcola i totali mensili a partire da tutte le spese.

        Reperisce le spese dal servizio, le converte in DTO (data
        normalizzata al mese), le ordina per data decrescente, le raggruppa
        per mese sommando gli importi.

        :param dati: non utilizzato (il caso d'uso non richiede input)
        :type dati: None
        :return: totali mensili in ordine di data decrescente
        :rtype: list[AbstractReportMensileDto]
        """
        results: list[AbstractReportMensileDto] = []
        spese = self._service.ottieni_tutte_le_spese()

        dtos = [ReportMensileDto(spesa.data, spesa.importo) for spesa in spese]
        dtos_ordinati = sorted(dtos, key=lambda dto: dto.data, reverse=True)

        for data, gruppo in groupby(dtos_ordinati, key=lambda dto: dto.data):
            importo = sum(dto.importo for dto in gruppo)
            results.append(ReportMensileDto(data, importo))

        return results
