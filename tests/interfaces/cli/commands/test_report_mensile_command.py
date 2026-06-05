"""Test del comando ReportMensileCommand."""

import unittest
from unittest.mock import MagicMock, patch

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.application.use_cases.report_mensile_use_case import (
    ReportMensileUseCase,
)
from gestore_spese.interfaces.cli.commands.report_mensile_command import (
    ReportMensileCommand,
)


class TestReportMensileCommand(unittest.TestCase):
    def setUp(self) -> None:
        self._use_case = MagicMock(spec_set=ReportMensileUseCase)
        self._command = ReportMensileCommand(self._use_case)

    @patch.object(ReportMensileCommand, "_mostra_output")
    def test_execute(self, mock_mostra_output):
        """execute esegue il caso d'uso e ne mostra il risultato."""
        report = [
            MagicMock(spec_set=AbstractReportMensileDto),
            MagicMock(spec_set=AbstractReportMensileDto),
        ]
        self._use_case.execute.return_value = report

        self._command.execute()

        self._use_case.execute.assert_called_once_with()
        mock_mostra_output.assert_called_once_with(report)
