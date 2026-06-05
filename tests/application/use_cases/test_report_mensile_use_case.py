"""Test del caso d'uso ReportMensileUseCase."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock

from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.use_cases.report_mensile_use_case import (
    ReportMensileUseCase,
)
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class TestReportMensileUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._use_case = ReportMensileUseCase(self._service)

    def test_execute(self):
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

        result = self._use_case.execute()

        self._service.ottieni_tutte_le_spese.assert_called_once_with()
        self.assertEqual(result, expected)
