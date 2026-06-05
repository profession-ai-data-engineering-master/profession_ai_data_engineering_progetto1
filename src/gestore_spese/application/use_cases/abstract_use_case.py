"""Contratto astratto generico per i casi d'uso applicativi."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Tipi generici segnaposto per input e output del caso d'uso.
InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class AbstractUseCase(ABC, Generic[InputT, OutputT]):
    """Contratto generico di un caso d'uso: trasforma un input in un output.

    Il tipo dell'input e dell'output sono parametrici, cosi' ogni caso d'uso
    dichiara con precisione cosa riceve e cosa restituisce.
    """

    @abstractmethod
    def execute(self, dati: InputT) -> OutputT:
        """Esegue il caso d'uso.

        :param dati: input del caso d'uso (eventualmente ``None``)
        :type dati: InputT
        :return: output prodotto dal caso d'uso (eventualmente ``None``)
        :rtype: OutputT
        """
