"""DTO di report mensile."""

from __future__ import annotations

from datetime import datetime

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)


class ReportMensileDto(AbstractReportMensileDto):
    """Totale speso in un mese, implementa :class:`AbstractReportMensileDto`.

    La data viene normalizzata al primo giorno del mese: in questo modo due
    DTO dello stesso mese sono uguali e raggruppabili.
    """

    def __init__(self, data: datetime, importo: float) -> None:
        self.data = data
        self.importo = importo

    @property
    def data(self) -> datetime:
        """Ritorna la data (primo giorno del mese) del report.

        :return: data del report
        :rtype: datetime
        """
        return self._data

    @data.setter
    def data(self, data: datetime) -> None:
        """Imposta la data del report, normalizzandola al primo del mese.

        :param datetime data: nuova data del report
        :raises TypeError: se la data è None o non è di tipo datetime
        """
        if data is None or not isinstance(data, datetime):
            raise TypeError("La data deve essere di tipo datetime e non può essere None")
        self._data = datetime(data.year, data.month, 1)

    @property
    def importo(self) -> float:
        """Ritorna l'importo totale del report.

        :return: importo del report
        :rtype: float
        """
        return self._importo

    @importo.setter
    def importo(self, importo: float) -> None:
        """Imposta l'importo totale del report.

        :param float importo: nuovo importo del report
        :raises TypeError: se l'importo non è di tipo numerico
        :raises ValueError: se l'importo è minore o uguale a 0
        """
        if importo is None or not isinstance(importo, (int, float)):
            raise TypeError("L'importo deve essere di tipo numerico")
        if importo <= 0:
            raise ValueError("L'importo deve essere maggiore di 0")
        self._importo = float(importo)

    def __repr__(self) -> str:
        """Rappresentazione tecnica del DTO."""
        data_fmt = datetime.strftime(self._data, "%Y-%m-%d %H:%M:%S")
        return f"ReportMensileDto(data={data_fmt},importo={self._importo})"

    def __str__(self) -> str:
        """Rappresentazione leggibile del DTO."""
        return f"Data: {datetime.strftime(self._data, '%Y-%m')}, Importo: {self._importo}"

    def __eq__(self, other: object) -> bool:
        """Due report sono uguali se coincidono data (mese) e importo.

        :return: True se uguali, altrimenti False
        :rtype: bool
        """
        if not isinstance(other, ReportMensileDto):
            return NotImplemented
        return self.data == other.data and self.importo == other.importo

    def __hash__(self) -> int:
        """Hash coerente con :meth:`__eq__`.

        :return: hash dell'istanza
        :rtype: int
        """
        return hash((self.data, self.importo))
