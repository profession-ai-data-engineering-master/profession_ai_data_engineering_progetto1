"""Comando CLI: aggiunta di una nuova spesa."""

from __future__ import annotations

from datetime import datetime

from gestore_spese.application.use_cases.aggiungi_spesa_use_case import (
    AggiungiSpesaUseCase,
)
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.interfaces.cli.commands.abstract_command import AbstractCommand


class AggiungiSpesaCommand(AbstractCommand):
    """Raccoglie i dati da terminale e aggiunge una nuova spesa."""

    def __init__(self, use_case: AggiungiSpesaUseCase) -> None:
        self._use_case = use_case

    def _gestisci_input(self) -> AbstractSpesa:
        """Chiede i dati della spesa all'utente e costruisce l'entità.

        :return: la nuova spesa costruita dall'input
        :rtype: AbstractSpesa
        :raises ValueError: se data o importo non sono nel formato atteso
        """
        data_testo = input("Inserisci la data della nuova spesa (dd/mm/yyyy): ")
        data = datetime.strptime(data_testo, "%d/%m/%Y")
        descrizione = input("Inserisci la descrizione della nuova spesa: ")
        importo = float(input("Inserisci l'importo della nuova spesa: "))
        return Spesa(data, descrizione, importo)

    def _mostra_output(self, nuova_spesa: AbstractSpesa) -> None:
        """Conferma a video l'avvenuto inserimento.

        :param AbstractSpesa nuova_spesa: spesa appena aggiunta
        """
        print(f"Aggiunta con successo nuova Spesa: {nuova_spesa}")

    def execute(self) -> None:
        """Esegue il flusso completo: input -> caso d'uso -> output."""
        nuova_spesa = self._gestisci_input()
        self._use_case.execute(nuova_spesa)
        self._mostra_output(nuova_spesa)
