"""Sorgente dati delle spese su file CSV."""

from __future__ import annotations

import csv
from datetime import datetime
from os import path

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.infrastructure.persistence.datasources.abstract_spesa_datasource import (
    AbstractSpesaDataSource,
)


class SpesaDataSourceCsv(AbstractSpesaDataSource):
    """Persiste e legge le spese da un file CSV.

    Il file ha tre colonne (``data``, ``descrizione``, ``importo``) e viene
    creato con l'intestazione alla prima scrittura, se mancante o vuoto.
    """

    INTESTAZIONE = ["data", "descrizione", "importo"]
    FORMATO_DATA = "%Y-%m-%d %H:%M:%S"

    def __init__(self, filepath: str = "storico_spese.csv") -> None:
        self._filepath = filepath

    def _verifica_inizializzazione_sorgente(self) -> bool:
        """Indica se il file esiste ed e' gia' inizializzato (non vuoto).

        :return: True se la sorgente esiste ed e' inizializzata, altrimenti False
        :rtype: bool
        """
        return path.exists(self._filepath) and path.getsize(self._filepath) > 0

    def _inizializza_sorgente(self) -> None:
        """Crea il file della sorgente scrivendone l'intestazione."""
        with open(self._filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.INTESTAZIONE)

    def aggiungi_spesa(self, spesa: AbstractSpesa) -> None:
        """Aggiunge una nuova spesa alla sorgente dati (creandola se assente).

        :param AbstractSpesa spesa: spesa da aggiungere
        """
        if not self._verifica_inizializzazione_sorgente():
            self._inizializza_sorgente()
        with open(self._filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([spesa.data, spesa.descrizione, spesa.importo])

    def ottieni_tutte_le_spese(self) -> list[AbstractSpesa]:
        """Legge tutte le spese dalla sorgente dati.

        :return: tutte le spese presenti nel file (vuoto se la sorgente manca)
        :rtype: list[AbstractSpesa]
        """
        result: list[AbstractSpesa] = []
        if not self._verifica_inizializzazione_sorgente():
            return result
        with open(self._filepath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # salta l'intestazione
            for riga in reader:
                result.append(
                    Spesa(
                        datetime.strptime(riga[0], self.FORMATO_DATA),
                        riga[1],
                        float(riga[2]),
                    )
                )
        return result
