"""Entry point della CLI del Gestore delle Spese Domestiche.

Questo modulo espone la funzione :func:`main`, registrata come console script
``gestore-spese`` in ``pyproject.toml``.

In questa fase di scaffolding (milestone M0) la funzione e' un segnaposto:
l'orchestrazione vera e propria (la classe ``GestoreSpeseCli`` che fa da
composition root e avvia il menu) verra' introdotta con la migrazione del
layer ``interfaces/cli`` dal notebook prototipale (milestone M1, issue #13).
"""

from __future__ import annotations


def main() -> None:
    """Punto di ingresso del comando console ``gestore-spese``.

    Per ora stampa un messaggio segnaposto; sara' sostituita da
    ``GestoreSpeseCli().run()`` nella milestone M1.
    """
    print(
        "Gestore delle Spese Domestiche - scaffolding pronto.\n"
        "La CLI interattiva verra' implementata nella milestone M1."
    )


if __name__ == "__main__":
    main()
