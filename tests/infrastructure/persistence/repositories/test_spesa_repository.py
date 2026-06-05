"""Test del repository SpesaRepository."""

import unittest
from unittest.mock import MagicMock

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.infrastructure.persistence.datasources.abstract_spesa_datasource import (
    AbstractSpesaDataSource,
)
from gestore_spese.infrastructure.persistence.repositories.spesa_repository import (
    SpesaRepository,
)


class TestSpesaRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._datasource = MagicMock(spec_set=AbstractSpesaDataSource)
        self._repository = SpesaRepository(self._datasource)

    def test_aggiungi_spesa(self):
        """Il repository inoltra l'aggiunta al datasource."""
        spesa = MagicMock(spec_set=AbstractSpesa)
        self._repository.aggiungi_spesa(spesa)
        self._datasource.aggiungi_spesa.assert_called_once_with(spesa)

    def test_ottieni_tutte_le_spese(self):
        """Il repository inoltra la lettura al datasource e ne ritorna il risultato."""
        attese = [MagicMock(spec_set=AbstractSpesa), MagicMock(spec_set=AbstractSpesa)]
        self._datasource.ottieni_tutte_le_spese.return_value = attese
        result = self._repository.ottieni_tutte_le_spese()
        self._datasource.ottieni_tutte_le_spese.assert_called_once_with()
        self.assertEqual(result, attese)
