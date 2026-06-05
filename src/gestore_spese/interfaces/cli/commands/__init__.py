"""Comandi della CLI (pattern Command)."""

from gestore_spese.interfaces.cli.commands.abstract_command import AbstractCommand
from gestore_spese.interfaces.cli.commands.aggiungi_spesa_command import (
    AggiungiSpesaCommand,
)
from gestore_spese.interfaces.cli.commands.report_mensile_command import (
    ReportMensileCommand,
)
from gestore_spese.interfaces.cli.commands.top_10_spese_command import Top10SpeseCommand

__all__ = [
    "AbstractCommand",
    "AggiungiSpesaCommand",
    "ReportMensileCommand",
    "Top10SpeseCommand",
]
