# Tabelas de referencia

Esta pasta guarda de-para e dicionarios versionados usados pelos
transformers.

- `catmat_registro_anvisa_map.csv` (Fase 2, ainda nao criado): de-para
  entre Codigo BR/CATMAT (BPS) e registro Anvisa/apresentacao (CMED).
  Este e o cruzamento fragil do projeto: de-para semantico entre chaves
  diferentes, nao join por igualdade. So sera criado apos o spike de
  cobertura confirmar viabilidade da Fase 2.

- `populacao_municipio.csv` (Fase 1): população residente estimada por
  município/ano (fonte IBGE/SIDRA). Tabela de apoio pequena, não uma
  quinta fonte de alta fricção — mas obrigatória para o cálculo de
  gasto per capita prometido como marco publicável da Fase 1.
