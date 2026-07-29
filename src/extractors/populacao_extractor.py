"""
Extrator de população residente por município (IBGE/SIDRA).

Adicionado apos revisao: sem esta tabela de apoio, o marco publicavel
da Fase 1 ("dashboard de gasto per capita x leitos/UTI por municipio")
nao fecha — nao ha como calcular "per capita" sem denominador.

Nao e uma quinta fonte de alta fricao: a API SIDRA e publica, estavel
e nao exige spike de descoberta como SIOPS/BPS. Ainda assim, roda no
mesmo pipeline de validacao (Pydantic + quarentena) que as demais.
"""
from src.models.contracts import PopulacaoMunicipio


def extract_populacao(ano: int) -> list[PopulacaoMunicipio]:
    """Extrai população estimada por município para um ano de referência.

    TODO: confirmar tabela/agregado SIDRA a usar (estimativas
    populacionais têm mais de uma tabela candidata) e cadência de
    atualização (anual, com possível revisão pós-Censo).
    """
    raise NotImplementedError(
        "Extrator de população aguardando confirmação da tabela SIDRA a usar."
    )
