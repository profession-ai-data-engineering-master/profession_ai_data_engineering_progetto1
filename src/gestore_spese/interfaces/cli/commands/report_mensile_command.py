"""Comando CLI: visualizzazione del report mensile."""

from __future__ import annotations

from gestore_spese.application.dtos.abstract_report_mensile_dto import (
    AbstractReportMensileDto,
)
from gestore_spese.application.use_cases.report_mensile_use_case import (
    ReportMensileUseCase,
)
from gestore_spese.interfaces.cli.commands.abstract_command import AbstractCommand


class ReportMensileCommand(AbstractCommand):
    """Mostra a video il report mensile delle spese."""

    def __init__(self, use_case: ReportMensileUseCase) -> None:
        self._use_case = use_case

    def _mostra_output(self, report: list[AbstractReportMensileDto]) -> None:
        """Stampa le voci del report.

        :param list[AbstractReportMensileDto] report: totali mensili
        """
        print("Report Mensile:")
        for voce in report:
            print(voce)

    def execute(self) -> None:
        """Esegue il caso d'uso e ne mostra il risultato."""
        report = self._use_case.execute()
        self._mostra_output(report)
