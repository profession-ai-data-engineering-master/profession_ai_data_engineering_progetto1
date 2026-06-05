"""Contratto astratto di un comando della CLI (pattern Command)."""

from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    """Definisce l'interfaccia di un comando invocabile dalla CLI."""

    @abstractmethod
    def execute(self) -> None:
        """Esegue l'azione associata al comando."""
