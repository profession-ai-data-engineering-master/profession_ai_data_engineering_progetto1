"""CLI del Gestore delle Spese Domestiche: composition root ed entry point.

Espone :class:`GestoreSpeseCli` (che istanzia e collega tutti i componenti
dei layer sottostanti) e la funzione :func:`main`, registrata come console
script ``gestore-spese`` in ``pyproject.toml``.
"""

from __future__ import annotations

from dataclasses import dataclass

from gestore_spese.application.use_cases.aggiungi_spesa_use_case import (
    AggiungiSpesaUseCase,
)
from gestore_spese.application.use_cases.report_mensile_use_case import (
    ReportMensileUseCase,
)
from gestore_spese.application.use_cases.top_10_spese_use_case import Top10SpeseUseCase
from gestore_spese.domain.services.spesa_service import SpesaService
from gestore_spese.infrastructure.persistence.datasources.spesa_datasource_csv import (
    SpesaDataSourceCsv,
)
from gestore_spese.infrastructure.persistence.repositories.spesa_repository import (
    SpesaRepository,
)
from gestore_spese.interfaces.cli.commands.abstract_command import AbstractCommand
from gestore_spese.interfaces.cli.commands.aggiungi_spesa_command import (
    AggiungiSpesaCommand,
)
from gestore_spese.interfaces.cli.commands.report_mensile_command import (
    ReportMensileCommand,
)
from gestore_spese.interfaces.cli.commands.top_10_spese_command import Top10SpeseCommand


@dataclass(frozen=True)
class VoceMenu:
    """Voce del menu della CLI.

    :param str descrizione: testo mostrato all'utente
    :param comando: comando da eseguire, oppure ``None`` per la voce di uscita
    :type comando: AbstractCommand | None
    """

    descrizione: str
    comando: AbstractCommand | None


class GestoreSpeseCli:
    """Interfaccia a riga di comando dell'applicazione.

    Funge da *composition root*: costruisce la catena di dipendenze
    (datasource -> repository -> service -> casi d'uso -> comandi) e guida
    l'utente attraverso un menu interattivo.
    """

    def __init__(self) -> None:
        datasource = SpesaDataSourceCsv()
        repository = SpesaRepository(datasource)
        service = SpesaService(repository)

        aggiungi_command = AggiungiSpesaCommand(AggiungiSpesaUseCase(service))
        report_command = ReportMensileCommand(ReportMensileUseCase(service))
        top10_command = Top10SpeseCommand(Top10SpeseUseCase(service))

        # Una voce con comando None rappresenta l'uscita: nessun confronto
        # speciale su stringhe, basta riconoscere il comando assente.
        self._voci: dict[str, VoceMenu] = {
            "1": VoceMenu("Aggiungi una Spesa", aggiungi_command),
            "2": VoceMenu("Mostra Report Mensile", report_command),
            "3": VoceMenu("Mostra Top 10 delle Spese", top10_command),
            "esci": VoceMenu("Esci dal programma", None),
        }

    def _mostra_menu(self) -> None:
        """Stampa le opzioni disponibili."""
        print("Scegli un'opzione (inserisci la chiave):")
        for chiave, voce in self._voci.items():
            print(f"[{chiave}] {voce.descrizione}")

    def run(self) -> None:
        """Avvia il loop interattivo del menu fino all'uscita."""
        print("Gestore Spese")
        while True:
            try:
                self._mostra_menu()
                scelta = input("> ").strip().lower()
                voce = self._voci[scelta]
                if voce.comando is None:
                    print("Grazie e arrivederci!")
                    break
                voce.comando.execute()
            except KeyError:
                print("Comando non valido, riprova")
            except ValueError:
                print("Valore di input non valido")


def main() -> None:
    """Punto di ingresso del comando console ``gestore-spese``."""
    GestoreSpeseCli().run()


if __name__ == "__main__":
    main()
