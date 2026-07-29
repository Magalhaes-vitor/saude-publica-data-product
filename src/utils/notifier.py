"""
Notificacao via Slack (webhook), seguindo o mesmo padrao de webhook + retry usado nos outros modulos deste projeto.

Tambem e o canal por onde o resumo gerado pelo agente Bedrock chega —
sempre como rascunho para revisao humana, nunca como post automatico.
"""
import os
import requests


SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")


def notify(message: str, is_draft_for_review: bool = False) -> None:
    """Envia mensagem ao Slack.

    is_draft_for_review=True sinaliza que o conteudo foi gerado pelo
    agente Bedrock e precisa de aprovacao humana antes de qualquer
    publicacao externa (LinkedIn).
    """
    if not SLACK_WEBHOOK_URL:
        raise RuntimeError("SLACK_WEBHOOK_URL nao configurado.")
    prefix = ":robot_face: [RASCUNHO - revisar antes de publicar]\n" if is_draft_for_review else ""
    requests.post(SLACK_WEBHOOK_URL, json={"text": prefix + message}, timeout=10)
