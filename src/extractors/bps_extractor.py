"""
Extrator BPS — preco pago em compras publicas de medicamentos. FASE 2.

So entra em desenvolvimento apos o spike confirmar:
1) taxa de nulidade do campo municipio na base anual compilada;
2) se o "Relatorio de Precos Pagos x Precos Regulados" do Painel de
   Precos da Saude ja resolve o cruzamento BPS x CMED nativamente
   (o que mudaria este extrator de "reconstruir join" para "extrair
   relatorio pronto").

Ver docs/DOCUMENTACAO_TECNICA.md, secao "Fase 2 - criterio de go/no-go".
"""
from src.models.contracts import BpsPrecoPago


def extract_bps(*args, **kwargs) -> list[BpsPrecoPago]:
    raise NotImplementedError("Fase 2 - aguardando decisao go/no-go do spike BPS.")
