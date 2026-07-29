"""
Entrypoint de producao (AWS Lambda).

DECISAO: Lambda "Master" unica, nao Step Functions.

Para a Fase 1 (SIOPS + CNES + populacao, sequenciais, volume pequeno,
execucao mensal/bimestral), uma Lambda unica orquestrando internamente
extract -> validate -> transform -> load e suficiente e mais simples
de operar/depurar do que uma state machine. Este handler e uma casca
fina: toda a logica real vive em orchestrator.run(), para que o mesmo
pipeline rode identico local (python orchestrator.py) e em producao
(este handler).

Reavaliar Step Functions se a Fase 2 introduzir ramos que precisem
rodar em paralelo com tratamento de erro independente por ramo (ex.:
BPS e CMED podem ser extraidos em paralelo antes do join item<->item) -
nesse ponto o ganho de orquestracao visual e retry por estado passa a
compensar a complexidade adicional de operar uma state machine.
"""
from orchestrator import run


def handler(event, context):
    return run()
