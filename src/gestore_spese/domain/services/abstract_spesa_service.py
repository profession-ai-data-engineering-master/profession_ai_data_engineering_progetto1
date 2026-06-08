"""Contratto astratto del servizio di dominio delle spese."""

from __future__ import annotations

from abc import ABC, abstractmethod

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa


class AbstractSpesaService(ABC):
    """Contratto del servizio che coordina la logica di dominio sulle spese.

    Incapsula la logica di business che può coinvolgere più entità,
    mediando l'accesso al repository.
    """

    @abstractmethod
    def aggiungi_spesa(self, spesa: AbstractSpesa) -> None:
        """Aggiunge una nuova spesa tramite il repository.

        :param AbstractSpesa spesa: spesa da aggiungere
        """

    @abstractmethod
    def ottieni_tutte_le_spese(self) -> list[AbstractSpesa]:
        """Ritorna tutte le spese tramite il repository.

        :return: tutte le spese disponibili
        :rtype: list[AbstractSpesa]
        """
