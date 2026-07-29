"""
Zona de quarentena / circuit breaker.

Principio central de qualidade do pipeline: registro que falha o contrato Pydantic
nunca chega na Gold. Fail-closed, nao fail-open — ausencia de campo
esperado (ex.: total oficial de um boletim) e tratada como falha
estrutural, nao como validacao ignorada.
"""


class QuarantineError(Exception):
    """Levantado quando um circuit breaker de qualidade e acionado."""


def check_coverage(rejected_count: int, total_count: int, threshold: float = 0.05) -> None:
    """Criterio 1 - taxa de rejeicao por linha. Aplica-se a todas as fontes."""
    if total_count == 0:
        raise QuarantineError("Lote vazio - total_count == 0.")
    rejection_rate = rejected_count / total_count
    if rejection_rate > threshold:
        raise QuarantineError(
            f"Taxa de rejeicao {rejection_rate:.2%} acima do limite {threshold:.0%}."
        )


def check_agregado_siops(soma_lote: float, total_declarado_periodo: float | None, threshold: float = 0.05) -> None:
    """Criterio 2 - cobertura de valor agregado. Especifico do SIOPS.

    DECISAO EXPLICITA (nao e esquecimento): o MVP roda inicialmente so
    com check_coverage (criterio 1) para SIOPS e CNES. Este segundo
    criterio existe pronto, mas so entra em producao para o SIOPS
    quando o spike confirmar um total agregado por municipio/periodo
    exposto pelo proprio TabNet para comparar contra a soma do lote.
    Motivo de nao aplicar ainda: sem confirmar que esse total existe e
    e confiavel, o criterio criaria falso positivo/negativo em vez de
    proteger o pipeline. CNES nao usa este segundo criterio porque e
    dado estruturado via API, com risco de inconsistencia agregada
    menor do que um dado autodeclarado bimestralmente.
    """
    if total_declarado_periodo is None:
        raise QuarantineError(
            "Total agregado ausente para o periodo - tratado como falha "
            "estrutural (fail-closed), nao como validacao ignorada."
        )
    desvio = abs(soma_lote - total_declarado_periodo) / total_declarado_periodo
    if desvio > threshold:
        raise QuarantineError(
            f"Desvio de cobertura agregada {desvio:.2%} acima do limite {threshold:.0%}."
        )
