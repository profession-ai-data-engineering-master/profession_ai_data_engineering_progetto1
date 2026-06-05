"""Contratto astratto del repository delle spese."""

from __future__ import annotations

from abc import ABC, abstractmethod

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa


class AbstractSpesaRepository(ABC):
    """Definisce le operazioni che un repository di spese deve offrire."""

    @abstractmethod
    def aggiungi_spesa(self, spesa: AbstractSpesa) -> None:
        """Aggiunge una nuova spesa al repository.

        :param AbstractSpesa spesa: spesa da aggiungere
        """

    @abstractmethod
    def ottieni_tutte_le_spese(self) -> list[AbstractSpesa]:
        """Ritorna tutte le spese presenti nel repository.

        :return: tutte le spese presenti nel repository
        :rtype: list[AbstractSpesa]
        """
