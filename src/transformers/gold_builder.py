"""
Construcao da camada Gold.

Fase 1: fato_gasto_saude + fato_capacidade_instalada, cruzadas por
dim_municipio (codigo IBGE) e dim_tempo.

Fase 2 (condicional): fato_precos_medicamentos, via de-para
catmat_registro_anvisa_map.csv em src/reference/.

O indice composto de eficiencia (gasto x capacidade x preco), se
implementado, deve ser calculado aqui e SEMPRE acompanhado, na
documentacao e nos posts, do aviso de que e uma hipotese de pesquisa
exploratoria — sem normalizacao por perfil populacional, complexidade
de rede ou efeito de municipio-polo. Ver README, secao "Limitacoes".
"""
import pandas as pd


def build_fato_gasto_saude(siops_silver: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


def build_fato_capacidade_instalada(cnes_silver: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


def build_fato_precos_medicamentos(bps_silver: pd.DataFrame, cmed_silver: pd.DataFrame) -> pd.DataFrame:
    """Fase 2 — condicional a cobertura do de-para item<->item."""
    raise NotImplementedError
