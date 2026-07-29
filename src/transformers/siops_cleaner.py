"""Limpeza e normalizacao dos registros SIOPS (Bronze -> Silver)."""
import pandas as pd


def clean_siops(raw: pd.DataFrame) -> pd.DataFrame:
    """Normaliza tipos, trata inconsistencia de preenchimento entre municipios.

    TODO: documentar aqui, de forma explicita, os municipios/periodos
    com preenchimento ausente ou inconsistente identificados no spike -
    nao tratar como dado valido por omissao.
    """
    raise NotImplementedError
