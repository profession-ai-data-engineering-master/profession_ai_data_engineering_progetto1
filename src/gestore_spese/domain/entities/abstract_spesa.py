"""Contratto astratto dell'entità di dominio Spesa."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime


class AbstractSpesa(ABC):
    """Definisce i metodi che ogni entità di tipo Spesa deve implementare."""

    @property
    @abstractmethod
    def data(self) -> datetime:
        """Ritorna la data della spesa.

        :return: data della spesa
        :rtype: datetime
        """

    @data.setter
    @abstractmethod
    def data(self, data: datetime) -> None:
        """Imposta la data della spesa.

        :param datetime data: nuova data della spesa
        """

    @property
    @abstractmethod
    def descrizione(self) -> str:
        """Ritorna la descrizione della spesa.

        :return: descrizione della spesa
        :rtype: str
        """

    @descrizione.setter
    @abstractmethod
    def descrizione(self, descrizione: str) -> None:
        """Imposta la descrizione della spesa.

        :param str descrizione: nuova descrizione della spesa
        """

    @property
    @abstractmethod
    def importo(self) -> float:
        """Ritorna l'importo della spesa.

        :return: importo della spesa
        :rtype: float
        """

    @importo.setter
    @abstractmethod
    def importo(self, importo: float) -> None:
        """Imposta l'importo della spesa.

        :param float importo: nuovo importo della spesa
        """

    @abstractmethod
    def __repr__(self) -> str:
        """Definisce la rappresentazione tecnica delle istanze di spesa.

        :return: rappresentazione tecnica della spesa
        :rtype: str
        """

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Definisce l'uguaglianza tra due istanze di spesa.

        :return: True se uguali, altrimenti False
        :rtype: bool
        """

    @abstractmethod
    def __hash__(self) -> int:
        """Ritorna un hash coerente con :meth:`__eq__`.

        :return: hash dell'istanza
        :rtype: int
        """
