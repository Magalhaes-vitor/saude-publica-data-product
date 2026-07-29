-- DDL de referencia para as tabelas fato da camada Gold (Fase 1).
-- Ajustar particionamento e tipos apos os schemas reais serem confirmados
-- nos spikes de SIOPS e CNES.
--
-- Gasto per capita e leitos por habitante (marco publicavel da Fase 1)
-- sao calculados via view/query no Athena, fazendo JOIN de
-- fato_gasto_saude e fato_capacidade_instalada com
-- dim_populacao_municipio por (codigo_ibge, ano) - nao sao colunas
-- fisicas nas tabelas fato, para nao acoplar o fato a uma revisao
-- futura da estimativa populacional.

CREATE EXTERNAL TABLE IF NOT EXISTS fato_gasto_saude (
    codigo_ibge         string,
    municipio           string,
    uf                  string,
    ano                 int,
    bimestre            int,
    despesa_total_saude decimal(18,2)
)
STORED AS PARQUET
LOCATION 's3://<bucket>/gold/fato_gasto_saude/'
TBLPROPERTIES ('parquet.compression'='SNAPPY');

-- Tabela de apoio, nao um fato: denominador do calculo de per capita.
CREATE EXTERNAL TABLE IF NOT EXISTS dim_populacao_municipio (
    codigo_ibge         string,
    municipio           string,
    uf                  string,
    ano                 int,
    populacao_estimada  bigint
)
STORED AS PARQUET
LOCATION 's3://<bucket>/gold/dim_populacao_municipio/'
TBLPROPERTIES ('parquet.compression'='SNAPPY');

CREATE EXTERNAL TABLE IF NOT EXISTS fato_capacidade_instalada (
    codigo_cnes   string,
    codigo_ibge   string,
    municipio     string,
    uf            string,
    competencia   date,
    leitos_total  int,
    leitos_uti    int
)
STORED AS PARQUET
LOCATION 's3://<bucket>/gold/fato_capacidade_instalada/'
TBLPROPERTIES ('parquet.compression'='SNAPPY');
