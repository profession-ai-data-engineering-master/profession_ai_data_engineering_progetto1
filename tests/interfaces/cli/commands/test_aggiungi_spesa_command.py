"""Test del comando AggiungiSpesaCommand."""

import unittest
from unittest.mock import MagicMock, patch

from gestore_spese.application.use_cases.aggiungi_spesa_use_case import (
    AggiungiSpesaUseCase,
)
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.interfaces.cli.commands.aggiungi_spesa_command import (
    AggiungiSpesaCommand,
)


class TestAggiungiSpesaCommand(unittest.TestCase):
    def setUp(self) -> None:
        self._use_case = MagicMock(spec_set=AggiungiSpesaUseCase)
        self._command = AggiungiSpesaCommand(self._use_case)

    @patch.object(AggiungiSpesaCommand, "_mostra_output")
    @patch.object(AggiungiSpesaCommand, "_gestisci_input")
    def test_execute(self, mock_gestisci_input, mock_mostra_output):
        """execute orchestra input -> caso d'uso -> output."""
        spesa = MagicMock(spec_set=AbstractSpesa)
        mock_gestisci_input.return_value = spesa

        self._command.execute()

        mock_gestisci_input.assert_called_once_with()
        self._use_case.execute.assert_called_once_with(spesa)
        mock_mostra_output.assert_called_once_with(spesa)
