"""Regras de competencia/periodo (bimestre SIOPS, competencia mensal CNES)."""


def bimestre_atual(ano: int, mes: int) -> int:
    """Converte mes (1-12) no bimestre correspondente (1-6) usado pelo SIOPS."""
    return (mes - 1) // 2 + 1
