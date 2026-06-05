"""Test del comando Top10SpeseCommand."""

import unittest
from unittest.mock import MagicMock, patch

from gestore_spese.application.use_cases.top_10_spese_use_case import Top10SpeseUseCase
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.interfaces.cli.commands.top_10_spese_command import Top10SpeseCommand


class TestTop10SpeseCommand(unittest.TestCase):
    def setUp(self) -> None:
        self._use_case = MagicMock(spec_set=Top10SpeseUseCase)
        self._command = Top10SpeseCommand(self._use_case)

    @patch.object(Top10SpeseCommand, "_mostra_output")
    def test_execute(self, mock_mostra_output):
        """execute esegue il caso d'uso e ne mostra il risultato."""
        spese = [
            MagicMock(spec_set=AbstractSpesa),
            MagicMock(spec_set=AbstractSpesa),
        ]
        self._use_case.execute.return_value = spese

        self._command.execute()

        self._use_case.execute.assert_called_once_with()
        mock_mostra_output.assert_called_once_with(spese)
