"""Testes dos contratos Pydantic. Expandir conforme os spikes fecham o schema real."""
from datetime import date

import pytest
from pydantic import ValidationError

from src.models.contracts import CnesCapacidadeInstalada, PopulacaoMunicipio


def test_cnes_capacidade_instalada_valido():
    registro = CnesCapacidadeInstalada(
        codigo_cnes="1234567",
        codigo_ibge="3550308",
        municipio="Sao Paulo",
        uf="SP",
        competencia=date(2026, 1, 1),
        leitos_total=120,
        leitos_uti=20,
    )
    assert registro.leitos_uti <= registro.leitos_total


def test_cnes_rejeita_leitos_uti_maior_que_total():
    """O contrato, não só o teste de exemplo, precisa impedir isso."""
    with pytest.raises(ValidationError):
        CnesCapacidadeInstalada(
            codigo_cnes="1234567",
            codigo_ibge="3550308",
            municipio="Sao Paulo",
            uf="SP",
            competencia=date(2026, 1, 1),
            leitos_total=10,
            leitos_uti=20,
        )


def test_populacao_municipio_valido():
    registro = PopulacaoMunicipio(
        codigo_ibge="3550308",
        municipio="Sao Paulo",
        uf="SP",
        ano=2026,
        populacao_estimada=12_300_000,
    )
    assert registro.populacao_estimada > 0
