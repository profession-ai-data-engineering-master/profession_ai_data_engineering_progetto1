"""Contratto astratto del DTO di report mensile."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime


class AbstractReportMensileDto(ABC):
    """Contratto di un DTO che rappresenta il totale speso in un dato mese."""

    @property
    @abstractmethod
    def data(self) -> datetime:
        """Ritorna la data (mese/anno) del report.

        :return: data del report
        :rtype: datetime
        """

    @data.setter
    @abstractmethod
    def data(self, data: datetime) -> None:
        """Imposta la data del report.

        :param datetime data: nuova data del report
        """

    @property
    @abstractmethod
    def importo(self) -> float:
        """Ritorna l'importo totale del report.

        :return: importo del report
        :rtype: float
        """

    @importo.setter
    @abstractmethod
    def importo(self, importo: float) -> None:
        """Imposta l'importo totale del report.

        :param float importo: nuovo importo del report
        """

    @abstractmethod
    def __repr__(self) -> str:
        """Rappresentazione tecnica del DTO.

        :return: rappresentazione tecnica
        :rtype: str
        """

    @abstractmethod
    def __str__(self) -> str:
        """Rappresentazione leggibile del DTO.

        :return: rappresentazione leggibile
        :rtype: str
        """

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Uguaglianza tra due DTO.

        :return: True se uguali, altrimenti False
        :rtype: bool
        """

    @abstractmethod
    def __hash__(self) -> int:
        """Hash coerente con :meth:`__eq__`.

        :return: hash dell'istanza
        :rtype: int
        """
