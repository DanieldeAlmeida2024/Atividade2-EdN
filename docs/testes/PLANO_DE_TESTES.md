# Plano de testes — Atividade2-EdN

**Versão do documento:** 1.0.0 | **Data:** 11/11/2026 | **Commit auditado:** `ecde9d5c162a66cb80e4581856d7d353c2bb4a34` | **Estado:** análise estática, testes de execução ainda não confirmados.

Os IDs abaixo são **casos propostos**; o repositório tem `tests/test_documentacao.py`, mas não uma suíte dedicada cobrindo os resultados de todos esses scripts. Não marcar como aprovado sem registrar stdout/entrada por commit.

| Caso | Script | Procedimento e resultado esperado | Situação |
|---|---|---|---|
| EDT-01 | `calciuladoraSalarioPorHora.py` | 40h a R$20,50 produz R$820,00 | Planejado |
| EDT-02 | `calculadoraConsumoCombustivel.py` | Imprime consumo médio de 12,00 km/l | Planejado |
| EDT-03 | `calculadoraDesconto.py` | Testar desconto zero e total | Planejado |
| EDT-04 | `calculadoraMediaEscolar.py` | Conferir divisão e notas limites | Planejado |
| EDT-05 | `calculadoraSomaComEntradaUsuario.py` | Testar valores e entrada não numérica | Planejado |
| EDT-06 | `conversorDeMoeda.py` | Atenção: código multiplica reais por taxas, não necessariamente converte corretamente | Planejado |

## Testes negativos
N-01: executar scripts com entrada não numérica quando houver `input()` e registrar exceção/mensagem. N-02: valores zero e negativos conforme contrato de cada exercício. N-03: verificar formatação local (vírgula decimal, unidade e R$). N-04: comparar saída Python em duas versões suportadas e documentar diferenças.

## Evidências e execução
Rodar `python calciuladoraSalarioPorHora.py` para o exemplo principal, depois cada arquivo individualmente. Testes automáticos futuros devem usar `subprocess.run` e capturar saída. Registrar: SHA, Python version, entrada, stdout, expected, status. A mera presença de um arquivo de teste documental não comprova a aritmética.
