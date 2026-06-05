"""Comando CLI: visualizzazione delle 10 spese maggiori."""

from __future__ import annotations

from gestore_spese.application.use_cases.top_10_spese_use_case import Top10SpeseUseCase
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.interfaces.cli.commands.abstract_command import AbstractCommand


class Top10SpeseCommand(AbstractCommand):
    """Mostra a video le 10 spese di importo maggiore."""

    def __init__(self, use_case: Top10SpeseUseCase) -> None:
        self._use_case = use_case

    def _mostra_output(self, spese: list[AbstractSpesa]) -> None:
        """Stampa le spese.

        :param list[AbstractSpesa] spese: spese da mostrare
        """
        print("Top 10 Spese:")
        for spesa in spese:
            print(spesa)

    def execute(self) -> None:
        """Esegue il caso d'uso e ne mostra il risultato."""
        spese = self._use_case.execute()
        self._mostra_output(spese)
