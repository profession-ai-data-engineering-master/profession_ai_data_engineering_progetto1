"""Servizio di dominio delle spese."""

from __future__ import annotations

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.repositories.abstract_spesa_repository import (
    AbstractSpesaRepository,
)
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class SpesaService(AbstractSpesaService):
    """Implementa :class:`AbstractSpesaService` delegando al repository.

    Dipende dall'astrazione :class:`AbstractSpesaRepository` (Dependency
    Inversion): in questo dominio la logica è semplice, ma il servizio
    fornisce il punto di estensione per regole che coinvolgano più entità.
    """

    def __init__(self, repository: AbstractSpesaRepository) -> None:
        self._repository = repository

    def aggiungi_spesa(self, spesa: AbstractSpesa) -> None:
        """Aggiunge una nuova spesa tramite il repository.

        :param AbstractSpesa spesa: spesa da aggiungere
        """
        self._repository.aggiungi_spesa(spesa)

    def ottieni_tutte_le_spese(self) -> list[AbstractSpesa]:
        """Ritorna tutte le spese tramite il repository.

        :return: tutte le spese disponibili
        :rtype: list[AbstractSpesa]
        """
        return self._repository.ottieni_tutte_le_spese()
