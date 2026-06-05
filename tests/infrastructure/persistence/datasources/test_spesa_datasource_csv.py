"""Test della sorgente dati CSV SpesaDataSourceCsv."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock, mock_open, patch

from gestore_spese.domain.entities.abstract_spesa import AbstractSpesa
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.infrastructure.persistence.datasources.spesa_datasource_csv import (
    SpesaDataSourceCsv,
)

MODULE = "gestore_spese.infrastructure.persistence.datasources.spesa_datasource_csv"
INTESTAZIONE = ["data", "descrizione", "importo"]


class TestSpesaDataSourceCsv(unittest.TestCase):
    def setUp(self) -> None:
        self._ds = SpesaDataSourceCsv()

    @patch(f"{MODULE}.path.exists", return_value=False)
    def test_verifica_sorgente_file_non_esiste(self, _mock_exists):
        """File assente -> sorgente non inizializzata."""
        self.assertFalse(self._ds._verifica_inizializzazione_sorgente())

    @patch(f"{MODULE}.path.getsize", return_value=0)
    @patch(f"{MODULE}.path.exists", return_value=True)
    def test_verifica_sorgente_file_vuoto(self, _mock_exists, _mock_getsize):
        """File vuoto -> sorgente non inizializzata."""
        self.assertFalse(self._ds._verifica_inizializzazione_sorgente())

    @patch(f"{MODULE}.path.getsize", return_value=1)
    @patch(f"{MODULE}.path.exists", return_value=True)
    def test_verifica_sorgente_file_ok(self, _mock_exists, _mock_getsize):
        """File esistente e non vuoto -> sorgente inizializzata."""
        self.assertTrue(self._ds._verifica_inizializzazione_sorgente())

    @patch(f"{MODULE}.csv.writer")
    @patch(f"{MODULE}.open", new_callable=mock_open)
    def test_inizializza_sorgente(self, mock_file, mock_csv_writer):
        """L'inizializzazione apre il file in scrittura e scrive l'intestazione."""
        writer = MagicMock()
        mock_csv_writer.return_value = writer

        self._ds._inizializza_sorgente()

        mock_file.assert_called_once_with(self._ds._filepath, "w", newline="", encoding="utf-8")
        writer.writerow.assert_called_once_with(INTESTAZIONE)

    @patch(f"{MODULE}.csv.writer")
    @patch(f"{MODULE}.open", new_callable=mock_open)
    def test_aggiungi_spesa_inizializza_se_assente(self, mock_file, mock_csv_writer):
        """Se la sorgente manca viene creata (header) e poi la spesa appesa."""
        spesa = MagicMock(spec_set=AbstractSpesa)
        spesa.data = datetime(2025, 5, 1)
        spesa.descrizione = "spesa di test"
        spesa.importo = 30.41

        writer_init = MagicMock()
        writer_append = MagicMock()
        mock_csv_writer.side_effect = [writer_init, writer_append]

        with patch.object(
            SpesaDataSourceCsv, "_verifica_inizializzazione_sorgente", return_value=False
        ):
            self._ds.aggiungi_spesa(spesa)

        mock_file.assert_any_call("storico_spese.csv", "w", newline="", encoding="utf-8")
        mock_file.assert_any_call("storico_spese.csv", "a", newline="", encoding="utf-8")
        writer_init.writerow.assert_called_once_with(INTESTAZIONE)
        writer_append.writerow.assert_called_once_with(
            [spesa.data, spesa.descrizione, spesa.importo]
        )

    @patch(f"{MODULE}.csv.writer")
    @patch(f"{MODULE}.open", new_callable=mock_open)
    def test_aggiungi_spesa_solo_append(self, mock_file, mock_csv_writer):
        """Se la sorgente esiste, la spesa viene solo appesa."""
        spesa = MagicMock(spec_set=AbstractSpesa)
        spesa.data = datetime(2025, 5, 1)
        spesa.descrizione = "spesa di test"
        spesa.importo = 30.41

        writer = MagicMock()
        mock_csv_writer.return_value = writer

        with patch.object(
            SpesaDataSourceCsv, "_verifica_inizializzazione_sorgente", return_value=True
        ):
            self._ds.aggiungi_spesa(spesa)

        mock_file.assert_called_once_with("storico_spese.csv", "a", newline="", encoding="utf-8")
        writer.writerow.assert_called_once_with([spesa.data, spesa.descrizione, spesa.importo])

    @patch(f"{MODULE}.csv.reader")
    @patch(f"{MODULE}.open", new_callable=mock_open)
    def test_ottieni_tutte_le_spese_file_presente(self, mock_file, mock_csv_reader):
        """Con sorgente presente, le righe vengono lette come Spesa (saltando l'header)."""
        riga1 = ["2025-05-01 00:00:00", "spesa di test 1", "45.72"]
        riga2 = ["2025-06-01 00:00:00", "spesa di test 2", "0.99"]
        mock_csv_reader.return_value = iter([INTESTAZIONE, riga1, riga2])

        with patch.object(
            SpesaDataSourceCsv, "_verifica_inizializzazione_sorgente", return_value=True
        ):
            result = self._ds.ottieni_tutte_le_spese()

        mock_file.assert_called_once_with("storico_spese.csv", newline="", encoding="utf-8")
        self.assertEqual(len(result), 2)
        self.assertEqual(
            result[0],
            Spesa(datetime.strptime(riga1[0], "%Y-%m-%d %H:%M:%S"), riga1[1], float(riga1[2])),
        )
        self.assertEqual(
            result[1],
            Spesa(datetime.strptime(riga2[0], "%Y-%m-%d %H:%M:%S"), riga2[1], float(riga2[2])),
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
