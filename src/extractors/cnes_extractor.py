"""
Extrator CNES — capacidade instalada (leitos, UTIs) por municipio.

CNES expoe API publica. Este extrator segue o mesmo padrao dos
outros extratores de API deste projeto: requests + Tenacity
para retry com backoff, rate limiting explicito.

TODO(spike-cnes): confirmar endpoint estavel, paginacao e limites de
taxa antes de fechar a implementacao final.
"""
from src.models.contracts import CnesCapacidadeInstalada


def extract_cnes(codigo_ibge: str, competencia: str) -> list[CnesCapacidadeInstalada]:
    """Extrai capacidade instalada (leitos/UTIs) de um municipio/competencia."""
    raise NotImplementedError(
        "Extrator CNES aguardando confirmacao de contrato de API no spike."
    )
