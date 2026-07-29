"""
Testes dos transformers (cleaners + gold_builder).

TODO: casos a cobrir assim que os cleaners saírem do NotImplementedError:
- normalização de tipos e datas
- rejeição correta de linha inválida (integração com quarantine.py)
- cálculo de gasto per capita usando PopulacaoMunicipio como denominador
- comportamento de fato_precos_medicamentos quando BPS está ausente
  (fonte opcional, Fase 2) - pipeline não pode quebrar
"""
