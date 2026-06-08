"""Test del caso d'uso ReportMensileUseCase."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock

from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.application.use_cases.report_mensile_use_case import (
    ReportMensileUseCase,
)


class TestReportMensileUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self._provider = MagicMock(spec_set=AbstractReportingProvider)
        self._use_case = ReportMensileUseCase(self._provider)

    def test_execute_delega_al_provider(self):
        """Il caso d'uso restituisce il report del provider, senza rielaborarlo."""
        atteso = [ReportMensileDto(datetime(2025, 5, 1), 10.0)]
        self._provider.report_mensile.return_value = atteso

        result = self._use_case.execute()

        self._provider.report_mensile.assert_called_once_with()
        self.assertEqual(result, atteso)
