"""Provider di reporting in-memory: aggregazione in Python."""

from __future__ import annotations

from itertools import groupby

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class InMemoryReportingProvider(AbstractReportingProvider):
    """Calcola i report aggregando in memoria con Python.

    È il motore di **default**: recupera tutte le spese tramite il servizio di
    dominio e ne calcola i report in Python, senza dipendenze esterne.
    """

    def __init__(self, service: AbstractSpesaService) -> None:
        self._service = service

    def report_mensile(self) -> list[AbstractReportMensileDto]:
        """Aggrega le spese per anno/mese sommandone gli importi.

        Converte le spese in DTO (data normalizzata al mese), le ordina per
        data decrescente e le raggruppa per mese sommando gli importi.

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

    def top_10(self) -> list[AbstractSpesa]:
        """Ordina le spese per (importo, data) decrescente e ne prende 10.

        :return: le prime 10 spese per importo decrescente
        :rtype: list[AbstractSpesa]
        """
        spese = self._service.ottieni_tutte_le_spese()
        # Doppio criterio di ordinamento: prima importo, poi data, decrescenti.
        spese_ordinate = sorted(spese, key=lambda spesa: (spesa.importo, spesa.data), reverse=True)
        return spese_ordinate[0:10]
