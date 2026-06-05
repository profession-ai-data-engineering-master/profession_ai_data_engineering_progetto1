"""Contratto astratto della sorgente dati delle spese."""

from __future__ import annotations

from abc import ABC, abstractmethod

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa


class AbstractSpesaDataSource(ABC):
    """Definisce le operazioni di una sorgente dati di spese.

    L'astrazione consente di sostituire la persistenza (CSV, DB, ...) senza
    impattare i layer superiori.
    """

    @abstractmethod
    def aggiungi_spesa(self, spesa: AbstractSpesa) -> None:
        """Aggiunge una nuova spesa alla sorgente dati.

        :param AbstractSpesa spesa: spesa da aggiungere
        """

    @abstractmethod
    def ottieni_tutte_le_spese(self) -> list[AbstractSpesa]:
        """Ritorna tutte le spese presenti nella sorgente dati.

        :return: tutte le spese presenti nella sorgente dati
        :rtype: list[AbstractSpesa]
        """
