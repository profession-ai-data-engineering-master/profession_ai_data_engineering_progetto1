"""Gestore delle Spese Domestiche.

Applicazione CLI per il tracciamento delle spese personali, organizzata
secondo i principi della Clean Architecture / DDD:

- ``domain``: entità, contratti dei repository e servizi di dominio.
- ``application``: DTO e casi d'uso (logica applicativa).
- ``infrastructure``: implementazioni concrete della persistenza.
- ``interfaces``: punti di accesso esterni (CLI).
"""

__version__ = "0.1.0"
