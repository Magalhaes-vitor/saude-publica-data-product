"""
Entrypoint de execucao — chamado tanto localmente quanto pelo
lambda_function.py em producao. Mesmo pipeline nos dois casos, sem
duplicacao de logica entre ambiente local e Lambda.
"""


def run():
    raise NotImplementedError("Pipeline aguardando conclusao dos spikes de Fase 1.")


if __name__ == "__main__":
    run()
