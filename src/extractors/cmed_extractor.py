"""
Extrator CMED — preco-teto regulado de medicamentos (ANVISA). FASE 2.

Fonte publica planilha/PDF periodica, sujeita a formatacao suja
(separador decimal inconsistente, marcadores como asterisco no preco).
Parsing precisa ser resiliente a mudanca de layout entre publicacoes.
"""
from src.models.contracts import CmedPrecoRegulado


def extract_cmed(*args, **kwargs) -> list[CmedPrecoRegulado]:
    raise NotImplementedError("Fase 2 - aguardando decisao go/no-go do spike BPS.")
