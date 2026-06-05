"""Test del caso d'uso AggiungiSpesaUseCase."""

import unittest
from unittest.mock import MagicMock

from gestore_spese.application.use_cases.aggiungi_spesa_use_case import (
    AggiungiSpesaUseCase,
)
from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService


class TestAggiungiSpesaUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._use_case = AggiungiSpesaUseCase(self._service)

    def test_execute(self):
        """Il caso d'uso inoltra la spesa al service."""
        spesa = MagicMock(spec_set=AbstractSpesa)
        self._use_case.execute(spesa)
        self._service.aggiungi_spesa.assert_called_once_with(spesa)
