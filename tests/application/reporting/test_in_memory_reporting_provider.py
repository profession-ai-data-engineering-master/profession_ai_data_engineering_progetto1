"""Test del provider di reporting in-memory."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock

from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.reporting.in_memory_reporting_provider import (
    InMemoryReportingProvider,
)
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class TestInMemoryReportingProvider(unittest.TestCase):
    def setUp(self) -> None:
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._provider = InMemoryReportingProvider(self._service)

    def test_report_mensile(self):
        """Le spese vengono aggregate per mese e ordinate per data decrescente."""
        spese = [
            Spesa(datetime(2026, 1, 1), "sigarette", 3),
            Spesa(datetime(2025, 12, 1), "sigarette", 1),
            Spesa(datetime(2025, 12, 2), "sigarette", 2),
            Spesa(datetime(2026, 2, 2), "sigarette", 4),
            Spesa(datetime(2026, 2, 2), "sigarette", 4),
        ]
        expected = [
            ReportMensileDto(datetime(2026, 2, 2), 8),
            ReportMensileDto(datetime(2026, 1, 1), 3),
            ReportMensileDto(datetime(2025, 12, 1), 3),
        ]
        self._service.ottieni_tutte_le_spese.return_value = spese

        result = self._provider.report_mensile()

        self._service.ottieni_tutte_le_spese.assert_called_once_with()
        self.assertEqual(result, expected)

    def test_top_10(self):
        """Le spese vengono ordinate per (importo, data) decrescente."""
        spese = [
            Spesa(datetime(2025, 2, 2), "sigarette", 2.0),
            Spesa(datetime(2025, 2, 2), "sigarette", 3.0),
            Spesa(datetime(2025, 2, 3), "sigarette", 2.0),
            Spesa(datetime(2025, 3, 2), "sigarette", 5.0),
            Spesa(datetime(2025, 4, 2), "sigarette", 12.0),
        ]
        expected = [
            Spesa(datetime(2025, 4, 2), "sigarette", 12.0),
            Spesa(datetime(2025, 3, 2), "sigarette", 5.0),
            Spesa(datetime(2025, 2, 2), "sigarette", 3.0),
            Spesa(datetime(2025, 2, 3), "sigarette", 2.0),
            Spesa(datetime(2025, 2, 2), "sigarette", 2.0),
        ]
        self._service.ottieni_tutte_le_spese.return_value = spese

        result = self._provider.top_10()

        self._service.ottieni_tutte_le_spese.assert_called_once_with()
        self.assertEqual(result, expected)
