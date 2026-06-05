"""Test del caso d'uso Top10SpeseUseCase."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock

from gestore_spese.application.use_cases.top_10_spese_use_case import Top10SpeseUseCase
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class TestTop10SpeseUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._use_case = Top10SpeseUseCase(self._service)

    def test_execute(self):
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

        result = self._use_case.execute()

        self._service.ottieni_tutte_le_spese.assert_called_once_with()
        self.assertEqual(result, expected)
