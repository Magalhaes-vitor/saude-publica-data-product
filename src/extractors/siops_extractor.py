"""
Extrator SIOPS — execucao orcamentaria em saude por municipio.

O SIOPS e consultado via TabNet (consulta parametrizada), sem API REST.
Isso significa que este extrator provavelmente sera automacao de
formulario/download, nao uma chamada requests.get() simples como no
extrator do CNES deste projeto.

TODO(spike-siops): mapear o fluxo real do TabNet (parametros de consulta,
formato de exportacao disponivel) antes de implementar. Ver
docs/DOCUMENTACAO_TECNICA.md, secao "Spikes".
"""
from src.models.contracts import SiopsGastoSaude


def extract_siops(uf: str, ano: int, bimestre: int) -> list[SiopsGastoSaude]:
    """Extrai gasto em saude por municipio de uma UF/periodo.

    Levanta NotImplementedError ate o spike do TabNet definir a
    estrategia de extracao (form automation vs. endpoint de exportacao).
    """
    raise NotImplementedError(
        "Extrator SIOPS depende do spike de mapeamento do TabNet. "
        "Ver docs/DOCUMENTACAO_TECNICA.md."
    )
