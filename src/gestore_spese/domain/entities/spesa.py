"""Entità di dominio Spesa."""

from __future__ import annotations

from datetime import datetime

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa


class Spesa(AbstractSpesa):
    """Rappresenta una spesa, implementando il contratto :class:`AbstractSpesa`.

    Le regole di business sono applicate nei setter: una spesa non può avere
    una data assente, una descrizione troppo corta o un importo non positivo.
    """

    def __init__(self, data: datetime, descrizione: str, importo: float) -> None:
        self.data = data
        self.descrizione = descrizione
        self.importo = importo

    @property
    def data(self) -> datetime:
        """Ritorna la data della spesa.

        :return: data della spesa
        :rtype: datetime
        """
        return self._data

    @data.setter
    def data(self, data: datetime) -> None:
        """Imposta la data della spesa.

        :param datetime data: nuova data della spesa
        :raises TypeError: se la data è None o non è di tipo datetime
        """
        if data is None or not isinstance(data, datetime):
            raise TypeError("La data deve essere di tipo datetime e non può essere None")
        self._data = data

    @property
    def descrizione(self) -> str:
        """Ritorna la descrizione della spesa.

        :return: descrizione della spesa
        :rtype: str
        """
        return self._descrizione

    @descrizione.setter
    def descrizione(self, descrizione: str) -> None:
        """Imposta la descrizione della spesa.

        :param str descrizione: nuova descrizione della spesa
        :raises TypeError: se la descrizione non è di tipo str
        :raises ValueError: se la descrizione ha meno di 3 caratteri non-spazio
        """
        if descrizione is None or not isinstance(descrizione, str):
            raise TypeError("La descrizione deve essere di tipo str")
        if len(descrizione.strip()) < 3:
            raise ValueError("La descrizione deve avere minimo 3 caratteri che non siano spazi")
        self._descrizione = descrizione

    @property
    def importo(self) -> float:
        """Ritorna l'importo della spesa.

        :return: importo della spesa
        :rtype: float
        """
        return self._importo

    @importo.setter
    def importo(self, importo: float) -> None:
        """Imposta l'importo della spesa.

        :param float importo: nuovo importo della spesa
        :raises TypeError: se l'importo non è di tipo numerico
        :raises ValueError: se l'importo è minore o uguale a 0
        """
        if importo is None or not isinstance(importo, (int, float)):
            raise TypeError("L'importo deve essere di tipo numerico")
        if importo <= 0:
            raise ValueError("L'importo deve essere maggiore di 0")
        self._importo = float(importo)

    def __repr__(self) -> str:
        """Rappresentazione tecnica della spesa."""
        return f"Spesa(data={self.data},descrizione='{self.descrizione}',importo={self.importo})"

    def __str__(self) -> str:
        """Rappresentazione leggibile della spesa."""
        return (
            f"Data: {datetime.strftime(self._data, '%d/%m/%Y')}, "
            f"Descrizione: '{self.descrizione}', Importo: {self.importo}"
        )

    def __eq__(self, other: object) -> bool:
        """Due spese sono uguali se coincidono data, descrizione e importo.

        :return: True se uguali, altrimenti False
        :rtype: bool
        """
        if not isinstance(other, AbstractSpesa):
            return NotImplemented
        return (self.data, self.descrizione, self.importo) == (
            other.data,
            other.descrizione,
            other.importo,
        )

    def __hash__(self) -> int:
        """Hash coerente con :meth:`__eq__` (sui campi della spesa).

        :return: hash dell'istanza
        :rtype: int
        """
        return hash((self.data, self.descrizione, self.importo))
