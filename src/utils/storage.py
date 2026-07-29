"""
Conector do data lake (S3 em producao, disco local em desenvolvimento).

DECISAO EXPLICITA sobre nao ter um src/loaders/ separado ainda: no
escopo da Fase 1 (2 fontes, 2 tabelas fato), a logica de particionamento
e escrita em Parquet e simples o suficiente para caber aqui, com o
DataFrame ja pronto vindo do gold_builder. Se a Fase 2 aumentar a
complexidade de particionamento (ex.: parquet particionado por UF e
ano para fato_precos_medicamentos), reavaliar a extracao de um
src/loaders/ dedicado nesse ponto - nao antes.
"""
import os


class DataLakeConnector:
    def __init__(self, bucket: str | None = None):
        self.bucket = bucket or os.environ.get("DATA_LAKE_BUCKET")

    def write(self, layer: str, path: str, data) -> None:
        """layer: 'bronze' | 'silver' | 'gold'"""
        raise NotImplementedError

    def read(self, layer: str, path: str):
        raise NotImplementedError
