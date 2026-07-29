# Documentacao tecnica

Este arquivo cresce junto com o codigo. Por enquanto, a fonte de verdade
do escopo, arquitetura e decisoes tomadas ate aqui e o brief do projeto:
`saude-publica-data-product-brief.md` (na raiz ou anexado ao README).

## Spikes pendentes (bloqueiam inicio da Fase 1)

1. **Spike CNES** — confirmar endpoint estavel de API, paginacao e taxa
   de requisicao segura.
2. **Spike SIOPS** — mapear o fluxo do TabNet (parametros de consulta,
   formato de exportacao) e decidir estrategia de extracao.

## Spikes pendentes (bloqueiam decisao go/no-go da Fase 2)

3. **Spike BPS** — taxa de nulidade do campo municipio na base anual
   compilada; verificar se o "Relatorio de Precos Pagos x Precos
   Regulados" do Painel de Precos da Saude ja resolve nativamente o
   cruzamento BPS x CMED.

Cada spike concluido deve ser registrado aqui com data, achado e link
para o material bruto (print, CSV de amostra, etc.), no mesmo espirito
do runbook operacional (sintoma -> causa provavel -> acao).

## Revisão pós-esqueleto (antes do início dos spikes)

Duas revisões externas do esqueleto inicial apontaram gaps e decisões
implícitas que precisavam virar decisões explícitas. Aplicado:

1. **Gap: ausência de fonte de população.** O marco publicável da Fase 1
   (gasto per capita) não fechava sem denominador. Adicionado
   `PopulacaoMunicipio` como contrato, `populacao_extractor.py`
   (IBGE/SIDRA) e `dim_populacao_municipio` no DDL — tabela de apoio,
   não uma quinta fonte de alta fricção.
2. **Gap: contrato sem validator estrutural.** `CnesCapacidadeInstalada`
   não impedia `leitos_uti > leitos_total` no schema — só por acaso o
   teste de exemplo respeitava a regra. Adicionado `model_validator`.
3. **Regressão não documentada: circuit breaker simples.** A versão
   anterior tinha só `check_coverage` (critério de rejeição por linha),
   sem nota explicando por que o segundo critério do MVP anterior não
   foi trazido. Decisão registrada: `check_agregado_siops` existe no
   código, mas só ativa quando o spike do SIOPS confirmar um total
   agregado confiável para comparar — ver "Decisões de design
   aplicadas" no README.
4. **Organização:** `src/agents/` separado de `src/utils/notifier.py`
   (prompt/modelo vs. entrega); decisão registrada de manter a lógica
   de carga em `storage.py` em vez de um `src/loaders/` ainda;
   `orchestrator.py` confirmado como lógica única, com
   `lambda_function.py` como casca fina — decisão de não usar Step
   Functions na Fase 1.
