"""Test dell'entita' di dominio Spesa."""

import unittest
from datetime import datetime

from gestore_spese.domain.entities.spesa import Spesa


class TestSpesa(unittest.TestCase):
    def setUp(self) -> None:
        self._data = datetime(2025, 5, 1)
        self._descrizione = "spesa di test"
        self._importo = 30.41
        self._spesa = Spesa(self._data, self._descrizione, self._importo)

    def test_costruttore(self):
        """Il costruttore valorizza correttamente i campi."""
        self.assertEqual(self._spesa.data, self._data)
        self.assertEqual(self._spesa.descrizione, self._descrizione)
        self.assertEqual(self._spesa.importo, self._importo)

    def test_setter_data(self):
        """La data viene impostata e validata."""
        new_data = datetime(2025, 5, 7)
        self._spesa.data = new_data
        self.assertEqual(self._spesa.data, new_data)
        with self.assertRaises(TypeError):
            self._spesa.data = 0.0
        with self.assertRaises(TypeError):
            self._spesa.data = None
        with self.assertRaises(TypeError):
            self._spesa.data = "ciao"

    def test_setter_descrizione(self):
        """La descrizione viene impostata e validata."""
        new_descrizione = "nuova spesa di test"
        self._spesa.descrizione = new_descrizione
        self.assertEqual(self._spesa.descrizione, new_descrizione)
        with self.assertRaises(ValueError):
            self._spesa.descrizione = ""
        with self.assertRaises(ValueError):
            self._spesa.descrizione = "ab"
        with self.assertRaises(TypeError):
            self._spesa.descrizione = None
        with self.assertRaises(TypeError):
            self._spesa.descrizione = 5050

    def test_setter_importo(self):
        """L'importo viene impostato e validato."""
        new_importo = 99.99
        self._spesa.importo = new_importo
        self.assertEqual(self._spesa.importo, new_importo)
        with self.assertRaises(ValueError):
            self._spesa.importo = -1.0
        with self.assertRaises(ValueError):
            self._spesa.importo = 0.0
        with self.assertRaises(TypeError):
            self._spesa.importo = None
        with self.assertRaises(TypeError):
            self._spesa.importo = "ciao"

    def test_repr(self):
        """repr restituisce la rappresentazione tecnica attesa."""
        expected = (
            f"Spesa(data={self._data},descrizione='{self._descrizione}',importo={self._importo})"
        )
        self.assertEqual(repr(self._spesa), expected)

    def test_str(self):
        """str restituisce la rappresentazione leggibile attesa."""
        expected = (
            f"Data: {datetime.strftime(self._data, '%d/%m/%Y')}, "
            f"Descrizione: '{self._descrizione}', Importo: {self._importo}"
        )
        self.assertEqual(str(self._spesa), expected)

    def test_eq_uguali(self):
        """Due spese con stessi campi sono uguali."""
        spesa1 = Spesa(datetime(2025, 5, 1), "spesa di test", 30.41)
        spesa2 = Spesa(datetime(2025, 5, 1), "spesa di test", 30.41)
        self.assertEqual(spesa1, spesa2)

    def test_eq_diversa_data(self):
        """Spese con data diversa non sono uguali."""
        spesa1 = Spesa(datetime(2025, 5, 1), "spesa di test", 30.41)
        spesa2 = Spesa(datetime(2024, 5, 1), "spesa di test", 30.41)
        self.assertNotEqual(spesa1, spesa2)

    def test_eq_diversa_descrizione(self):
        """Spese con descrizione diversa non sono uguali."""
        spesa1 = Spesa(datetime(2025, 5, 1), "spesa di test1", 30.41)
        spesa2 = Spesa(datetime(2025, 5, 1), "spesa di test2", 30.41)
        self.assertNotEqual(spesa1, spesa2)

    def test_eq_diverso_importo(self):
        """Spese con importo diverso non sono uguali."""
        spesa1 = Spesa(datetime(2025, 5, 1), "spesa di test", 30.41)
        spesa2 = Spesa(datetime(2025, 5, 1), "spesa di test", 96.94)
        self.assertNotEqual(spesa1, spesa2)

    def test_eq_tipo_diverso(self):
        """Il confronto con un tipo diverso ritorna False senza sollevare (bugfix #6)."""
        self.assertNotEqual(self._spesa, "non una spesa")
        self.assertFalse(self._spesa == 42)

    def test_hashable(self):
        """La spesa e' hashable e coerente con __eq__ (bugfix #6)."""
        gemella = Spesa(self._data, self._descrizione, self._importo)
        self.assertEqual(hash(self._spesa), hash(gemella))
        self.assertIn(self._spesa, {gemella})
