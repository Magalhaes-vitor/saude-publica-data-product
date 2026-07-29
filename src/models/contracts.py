"""
Contratos de dados (Pydantic) do projeto.

Cada extrator so pode escrever na camada Bronze/Silver apos validar
o registro contra o contrato correspondente aqui. Registro invalido
vai para a zona de quarentena (ver src/utils/quarantine.py), nunca
para a Gold.

Campos marcados com TODO(spike) dependem da confirmacao de schema
real feita nos spikes de SIOPS e BPS (ver docs/DOCUMENTACAO_TECNICA.md).
"""
from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class SiopsGastoSaude(BaseModel):
    """Registro de execucao orcamentaria em saude por municipio (SIOPS/TabNet)."""

    codigo_ibge: str = Field(..., min_length=7, max_length=7)
    municipio: str
    uf: str = Field(..., min_length=2, max_length=2)
    ano: int
    bimestre: int = Field(..., ge=1, le=6)
    despesa_total_saude: Decimal
    despesa_recursos_proprios: Optional[Decimal] = None
    fonte: str = "SIOPS"

    # TODO(spike): confirmar se o TabNet expoe o dado ja consolidado por
    # bimestre ou se e necessario acumular a partir de lancamentos mensais.


class PopulacaoMunicipio(BaseModel):
    """População residente estimada por município/ano (IBGE/SIDRA).

    Tabela de apoio da Fase 1 — sem ela não é possível calcular
    gasto per capita nem aplicar a normalização mínima exigida pelo
    caveat do índice composto (ver README, "Limitações do índice
    composto").
    """

    codigo_ibge: str = Field(..., min_length=7, max_length=7)
    municipio: str
    uf: str = Field(..., min_length=2, max_length=2)
    ano: int
    populacao_estimada: int = Field(..., gt=0)
    fonte: str = "IBGE/SIDRA"


class CnesCapacidadeInstalada(BaseModel):
    """Registro de capacidade instalada por estabelecimento (CNES)."""

    codigo_cnes: str
    codigo_ibge: str = Field(..., min_length=7, max_length=7)
    municipio: str
    uf: str = Field(..., min_length=2, max_length=2)
    competencia: date
    leitos_total: int = Field(..., ge=0)
    leitos_uti: int = Field(..., ge=0)
    natureza_juridica: Optional[str] = None
    fonte: str = "CNES"

    @model_validator(mode="after")
    def leitos_uti_nao_excede_total(self):
        if self.leitos_uti > self.leitos_total:
            raise ValueError("leitos_uti não pode exceder leitos_total")
        return self


class BpsPrecoPago(BaseModel):
    """Registro de compra publica de medicamento/insumo (BPS) — Fase 2.

    TODO(spike): confirmar se o campo municipio ja vem preenchido na base
    anual compilada e qual a taxa de nulidade antes de tratar este contrato
    como estavel.
    """

    codigo_br_catmat: str
    descricao_item: str
    codigo_ibge_comprador: Optional[str] = None
    cnpj_comprador: str
    uf: str
    data_compra: date
    preco_unitario_pago: Decimal
    fonte: str = "BPS"


class CmedPrecoRegulado(BaseModel):
    """Registro de preco-teto regulado (CMED/ANVISA) — Fase 2.

    TODO(spike): a chave de item aqui (registro Anvisa/apresentacao) nao
    bate diretamente com o Codigo BR/CATMAT do BPS — ver de-para em
    src/reference/.
    """

    registro_anvisa: str
    apresentacao: str
    principio_ativo: str
    preco_fabrica: Decimal
    preco_maximo_consumidor: Optional[Decimal] = None
    data_vigencia: date
    fonte: str = "CMED"
