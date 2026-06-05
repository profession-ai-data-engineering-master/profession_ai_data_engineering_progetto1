"""Caso d'uso: aggiunta di una nuova spesa."""

from __future__ import annotations

from gestore_spese.application.use_cases.abstract_use_case import AbstractUseCase
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class AggiungiSpesaUseCase(AbstractUseCase[AbstractSpesa, None]):
    """Aggiunge una nuova spesa delegando al servizio di dominio."""

    def __init__(self, service: AbstractSpesaService) -> None:
        self._service = service

    def execute(self, dati: AbstractSpesa) -> None:
        """Salva la nuova spesa tramite il servizio.

        :param AbstractSpesa dati: spesa da aggiungere
        """
        self._service.aggiungi_spesa(dati)
