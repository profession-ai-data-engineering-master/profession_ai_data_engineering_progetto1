"""Test del caso d'uso Top10SpeseUseCase."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock

from gestore_spese.application.ports.abstract_reporting_provider import (
    AbstractReportingProvider,
)
from gestore_spese.application.use_cases.top_10_spese_use_case import Top10SpeseUseCase
from gestore_spese.domain.entities.spesa import Spesa


class TestTop10SpeseUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self._provider = MagicMock(spec_set=AbstractReportingProvider)
        self._use_case = Top10SpeseUseCase(self._provider)

    def test_execute_delega_al_provider(self):
        """Il caso d'uso restituisce le spese del provider, senza rielaborarle."""
        atteso = [Spesa(datetime(2025, 4, 2), "sigarette", 12.0)]
        self._provider.top_10.return_value = atteso

        result = self._use_case.execute()

        self._provider.top_10.assert_called_once_with()
        self.assertEqual(result, atteso)
