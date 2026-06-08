"""Test del provider di reporting DuckDB (aggregazione in SQL)."""

import os
import shutil
import tempfile
import unittest
from datetime import datetime

from gestore_spese.application.dtos.report_mensile_dto import ReportMensileDto
from gestore_spese.application.reporting.in_memory_reporting_provider import (
    InMemoryReportingProvider,
)
from gestore_spese.domain.entities.spesa import Spesa
from gestore_spese.domain.services.spesa_service import SpesaService
from gestore_spese.infrastructure.persistence.datasources.spesa_datasource_csv import (
    SpesaDataSourceCsv,
)
from gestore_spese.infrastructure.persistence.repositories.spesa_repository import (
    SpesaRepository,
)
from gestore_spese.infrastructure.reporting.duckdb_reporting_provider import (
    DuckDbReportingProvider,
)


class TestDuckDbReportingProvider(unittest.TestCase):
    def setUp(self) -> None:
        self._dir = tempfile.mkdtemp()
        self._path = os.path.join(self._dir, "storico_spese.csv")
        self._datasource = SpesaDataSourceCsv(self._path)
        # Importi distinti e interi: somme esatte, nessuna ambiguità di ordine.
        self._spese = [
            Spesa(datetime(2025, 12, 1), "spesa a", 1.0),
            Spesa(datetime(2025, 12, 2), "spesa b", 2.0),
            Spesa(datetime(2026, 1, 1), "spesa c", 3.0),
            Spesa(datetime(2026, 2, 2), "spesa d", 4.0),
            Spesa(datetime(2026, 2, 3), "spesa e", 8.0),
        ]
        for spesa in self._spese:
            self._datasource.aggiungi_spesa(spesa)
        # Usa la property del datasource: stessa sorgente CSV, come in main.py.
        self._provider = DuckDbReportingProvider(self._datasource.filepath)

    def tearDown(self) -> None:
        shutil.rmtree(self._dir, ignore_errors=True)

    def test_report_mensile(self):
        """L'aggregazione SQL somma per mese e ordina per data decrescente."""
        expected = [
            ReportMensileDto(datetime(2026, 2, 1), 12.0),
            ReportMensileDto(datetime(2026, 1, 1), 3.0),
            ReportMensileDto(datetime(2025, 12, 1), 3.0),
        ]
        self.assertEqual(self._provider.report_mensile(), expected)

    def test_top_10(self):
        """La selezione SQL ordina per (importo, data) decrescente."""
        expected = sorted(self._spese, key=lambda spesa: (spesa.importo, spesa.data), reverse=True)[
            0:10
        ]
        self.assertEqual(self._provider.top_10(), expected)

    def test_sorgente_mancante_ritorna_liste_vuote(self):
        """Senza file sorgente i report sono liste vuote (come l'in-memory)."""
        provider = DuckDbReportingProvider(os.path.join(self._dir, "assente.csv"))
        self.assertEqual(provider.report_mensile(), [])
        self.assertEqual(provider.top_10(), [])

    def test_stesso_output_dei_due_motori(self):
        """A parità di dati, motore SQL e motore in-memory danno lo stesso output."""
        service = SpesaService(SpesaRepository(self._datasource))
        inmemory = InMemoryReportingProvider(service)
        self.assertEqual(self._provider.report_mensile(), inmemory.report_mensile())
        self.assertEqual(self._provider.top_10(), inmemory.top_10())
