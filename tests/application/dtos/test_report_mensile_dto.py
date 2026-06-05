"""Test del DTO ReportMensileDto."""

import unittest
from datetime import datetime

from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto


class TestReportMensileDto(unittest.TestCase):
    def setUp(self) -> None:
        self._data = datetime(2025, 5, 1)
        self._importo = 30.41
        self._dto = ReportMensileDto(self._data, self._importo)

    def test_costruttore(self):
        """Il costruttore valorizza data (normalizzata) e importo."""
        self.assertEqual(self._dto.data, self._data)
        self.assertEqual(self._dto.importo, self._importo)

    def test_setter_data_normalizza_al_mese(self):
        """La data viene normalizzata al primo giorno del mese e validata."""
        new_data = datetime(2025, 5, 7)
        self._dto.data = new_data
        self.assertEqual(self._dto.data, datetime(new_data.year, new_data.month, 1))
        with self.assertRaises(TypeError):
            self._dto.data = 0.0
        with self.assertRaises(TypeError):
            self._dto.data = None
        with self.assertRaises(TypeError):
            self._dto.data = "ciao"

    def test_setter_importo(self):
        """L'importo viene impostato e validato."""
        new_importo = 99.99
        self._dto.importo = new_importo
        self.assertEqual(self._dto.importo, new_importo)
        with self.assertRaises(ValueError):
            self._dto.importo = -1.0
        with self.assertRaises(ValueError):
            self._dto.importo = 0.0
        with self.assertRaises(TypeError):
            self._dto.importo = None
        with self.assertRaises(TypeError):
            self._dto.importo = "ciao"

    def test_repr(self):
        """repr restituisce la rappresentazione tecnica attesa."""
        data_fmt = datetime.strftime(self._data, "%Y-%m-%d %H:%M:%S")
        expected = f"ReportMensileDto(data={data_fmt},importo={self._importo})"
        self.assertEqual(repr(self._dto), expected)

    def test_str(self):
        """str restituisce la rappresentazione leggibile attesa."""
        expected = f"Data: {datetime.strftime(self._data, '%Y-%m')}, Importo: {self._importo}"
        self.assertEqual(str(self._dto), expected)

    def test_eq_uguali(self):
        """Due DTO con stessi campi sono uguali."""
        dto1 = ReportMensileDto(datetime(2025, 5, 1), 30.41)
        dto2 = ReportMensileDto(datetime(2025, 5, 1), 30.41)
        self.assertEqual(dto1, dto2)

    def test_eq_diversa_data(self):
        """DTO con mese diverso non sono uguali."""
        dto1 = ReportMensileDto(datetime(2025, 5, 1), 30.41)
        dto2 = ReportMensileDto(datetime(2024, 5, 1), 30.41)
        self.assertNotEqual(dto1, dto2)

    def test_eq_diverso_importo(self):
        """DTO con importo diverso non sono uguali."""
        dto1 = ReportMensileDto(datetime(2025, 5, 1), 30.41)
        dto2 = ReportMensileDto(datetime(2025, 5, 1), 96.94)
        self.assertNotEqual(dto1, dto2)

    def test_eq_tipo_diverso(self):
        """Il confronto con un tipo diverso ritorna False senza sollevare."""
        self.assertNotEqual(self._dto, "non un dto")

    def test_hashable(self):
        """Il DTO e' hashable e coerente con __eq__."""
        gemello = ReportMensileDto(self._data, self._importo)
        self.assertEqual(hash(self._dto), hash(gemello))
        self.assertIn(self._dto, {gemello})
