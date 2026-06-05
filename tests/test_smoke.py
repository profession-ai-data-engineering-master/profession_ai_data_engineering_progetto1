"""Smoke test: verifica che il pacchetto sia importabile e installato.

Test di infrastruttura introdotto con la configurazione di pytest (M0).
La suite vera e propria viene migrata dal notebook nella milestone M2.
"""

from __future__ import annotations

import gestore_spese


def test_pacchetto_importabile() -> None:
    """Il pacchetto si importa ed espone una versione semantica."""
    assert isinstance(gestore_spese.__version__, str)
    assert gestore_spese.__version__.count(".") >= 2
