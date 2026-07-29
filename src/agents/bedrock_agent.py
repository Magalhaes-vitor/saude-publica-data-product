"""
Agente de análise (Amazon Bedrock, Nova Micro ou equivalente).

Separado de src/utils/notifier.py de proposito: aqui mora a construcao
de prompt e a chamada ao modelo (a parte que pode mudar de provider/
modelo); notifier.py so cuida da entrega da mensagem (Slack), e nao
sabe nada sobre LLM. Isso evita que trocar de modelo exija tocar no
codigo de notificacao, e vice-versa.

Governanca (repetida aqui de proposito, e nao so no README): a saida
deste modulo e SEMPRE tratada como rascunho. Quem publica no Slack
(via notifier.notify(..., is_draft_for_review=True)) e quem decide se
vira post no LinkedIn e humano.
"""
import json


def build_prompt(gold_summary: dict) -> str:
    """Monta o prompt a partir de um resumo ja validado da camada Gold.

    Recebe apenas dado que ja passou pelo circuit breaker - o agente
    interpreta o que existe, nunca gera fato novo.
    """
    return (
        "Resuma em portugues, de forma objetiva, os principais outliers "
        "do periodo com base nestes dados agregados e ja validados:\n"
        f"{json.dumps(gold_summary, ensure_ascii=False)}"
    )


def summarize(gold_summary: dict) -> str:
    """Chama o Bedrock e retorna o rascunho de resumo.

    TODO: implementar chamada real via boto3 (bedrock-runtime) apos a
    Fase 1 estar em producao - nao ha necessidade do agente antes de
    existir Gold para resumir.
    """
    raise NotImplementedError("Agente entra apenas após a Fase 1 estar em produção.")
