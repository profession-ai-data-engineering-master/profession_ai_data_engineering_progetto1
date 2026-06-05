"""Test del servizio di dominio SpesaService."""

import unittest
from unittest.mock import MagicMock

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.repositories.abstract_spesa_repository import (
    AbstractSpesaRepository,
)
from gestore_spese.domain.services.spesa_service import SpesaService


class TestSpesaService(unittest.TestCase):
    def setUp(self) -> None:
        self._repository = MagicMock(spec_set=AbstractSpesaRepository)
        self._service = SpesaService(self._repository)

    def test_aggiungi_spesa(self):
        """Il service inoltra l'aggiunta al repository."""
        spesa = MagicMock(spec_set=AbstractSpesa)
        self._service.aggiungi_spesa(spesa)
        self._repository.aggiungi_spesa.assert_called_once_with(spesa)

    def test_ottieni_tutte_le_spese(self):
        """Il service inoltra la lettura al repository e ne ritorna il risultato."""
        attese = [MagicMock(spec_set=AbstractSpesa), MagicMock(spec_set=AbstractSpesa)]
        self._repository.ottieni_tutte_le_spese.return_value = attese
        result = self._service.ottieni_tutte_le_spese()
        self._repository.ottieni_tutte_le_spese.assert_called_once_with()
        self.assertEqual(result, attese)
