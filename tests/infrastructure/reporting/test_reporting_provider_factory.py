"""Test della factory di selezione del motore di reporting."""

import os
import sys
import unittest
from unittest.mock import MagicMock, patch

from gestore_spese.application.reporting.in_memory_reporting_provider import (
    InMemoryReportingProvider,
)
from gestore_spese.domain.services.abstract_spesa_service import AbstractSpesaService
from gestore_spese.infrastructure.reporting import reporting_provider_factory as factory
from gestore_spese.infrastructure.reporting.duckdb_reporting_provider import (
    DuckDbReportingProvider,
)
from gestore_spese.infrastructure.reporting.reporting_provider_factory import (
    crea_reporting_provider,
)

_MODULO_DUCKDB = "gestore_spese.infrastructure.reporting.duckdb_reporting_provider"


class TestReportingProviderFactory(unittest.TestCase):
    def setUp(self) -> None:
        self._service = MagicMock(spec_set=AbstractSpesaService)

    def test_default_in_memory_senza_env(self):
        """Senza variabile d'ambiente si usa il motore in-memory."""
        with patch.dict(os.environ, {}, clear=True):
            provider = crea_reporting_provider(self._service, "x.csv")
        self.assertIsInstance(provider, InMemoryReportingProvider)

    def test_env_inmemory_esplicito(self):
        """Il valore 'inmemory' seleziona il motore in-memory."""
        with patch.dict(os.environ, {factory.ENV_VARIABILE_MOTORE: "inmemory"}, clear=True):
            provider = crea_reporting_provider(self._service, "x.csv")
        self.assertIsInstance(provider, InMemoryReportingProvider)

    def test_env_duckdb(self):
        """Il valore 'duckdb' (case-insensitive) seleziona il motore SQL."""
        with patch.dict(os.environ, {factory.ENV_VARIABILE_MOTORE: " DuckDB "}, clear=True):
            provider = crea_reporting_provider(self._service, "x.csv")
        self.assertIsInstance(provider, DuckDbReportingProvider)

    def test_parametro_esplicito_prevale_sull_ambiente(self):
        """Il parametro 'motore' ha la precedenza sulla variabile d'ambiente."""
        with patch.dict(os.environ, {factory.ENV_VARIABILE_MOTORE: "inmemory"}, clear=True):
            provider = crea_reporting_provider(self._service, "x.csv", motore="duckdb")
        self.assertIsInstance(provider, DuckDbReportingProvider)

    def test_fallback_a_inmemory_se_extra_assente(self):
        """Se il provider DuckDB non è disponibile, fallback all'in-memory."""
        with patch.object(factory, "_prova_a_creare_duckdb_provider", return_value=None):
            provider = crea_reporting_provider(self._service, "x.csv", motore="duckdb")
        self.assertIsInstance(provider, InMemoryReportingProvider)

    def test_helper_ritorna_none_su_importerror(self):
        """L'helper ritorna None (non solleva) se l'import di duckdb fallisce."""
        with patch.dict(sys.modules, {_MODULO_DUCKDB: None}):
            result = factory._prova_a_creare_duckdb_provider("x.csv")
        self.assertIsNone(result)
