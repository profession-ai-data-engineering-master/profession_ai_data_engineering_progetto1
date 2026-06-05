"""Caso d'uso: le 10 spese di importo maggiore."""

from __future__ import annotations

from gestore_spese.application.use_cases.abstract_use_case import AbstractUseCase
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class Top10SpeseUseCase(AbstractUseCase[None, list[AbstractSpesa]]):
    """Restituisce le 10 spese con l'importo piu' alto."""

    def __init__(self, service: AbstractSpesaService) -> None:
        self._service = service

    def execute(self, dati: None = None) -> list[AbstractSpesa]:
        """Ordina le spese per importo (poi data) decrescente e ne prende 10.

        :param dati: non utilizzato (il caso d'uso non richiede input)
        :type dati: None
        :return: le prime 10 spese per importo decrescente
        :rtype: list[AbstractSpesa]
        """
        spese = self._service.ottieni_tutte_le_spese()
        # Doppio criterio di ordinamento: prima importo, poi data, decrescenti.
        spese_ordinate = sorted(spese, key=lambda spesa: (spesa.importo, spesa.data), reverse=True)
        return spese_ordinate[0:10]
