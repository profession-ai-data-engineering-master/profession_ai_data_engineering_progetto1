"""Implementazione del repository delle spese."""

from __future__ import annotations

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.repositories.abstract_spesa_repository import (
    AbstractSpesaRepository,
)
from gestore_spese.infrastructure.persistence.datasources.abstract_spesa_datasource import (
    AbstractSpesaDataSource,
)


class SpesaRepository(AbstractSpesaRepository):
    """Adapter tra il dominio e la sorgente dati.

    Implementa il contratto :class:`AbstractSpesaRepository` delegando a una
    :class:`AbstractSpesaDataSource`, da cui dipende solo per astrazione.
    """

    def __init__(self, datasource: AbstractSpesaDataSource) -> None:
        self._datasource = datasource

    def aggiungi_spesa(self, spesa: AbstractSpesa) -> None:
        """Aggiunge una nuova spesa tramite la sorgente dati.

        :param AbstractSpesa spesa: spesa da aggiungere
        """
        self._datasource.aggiungi_spesa(spesa)

    def ottieni_tutte_le_spese(self) -> list[AbstractSpesa]:
        """Ritorna tutte le spese dalla sorgente dati.

        :return: tutte le spese presenti nel repository
        :rtype: list[AbstractSpesa]
        """
        return self._datasource.ottieni_tutte_le_spese()
