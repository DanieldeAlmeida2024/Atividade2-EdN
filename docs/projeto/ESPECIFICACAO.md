# Entrada de dados, salário e conversões em Python

**Versão do documento:** 1.0.0 | **Data:** 11/11/2026 | **Commit auditado:** `ecde9d5c162a66cb80e4581856d7d353c2bb4a34` | **Estado:** análise estática, testes de execução ainda não confirmados.

## Contexto de engenharia
Este repositório contém 6 exercícios Python independentes, executados diretamente no terminal. Cada arquivo representa uma competência distinta; não foi introduzida uma arquitetura de microserviços ou aplicação web artificial.

## Inventário por arquivo e contrato
| Arquivo de origem | Comportamento implementado | Regra ou exemplo de aceitação |
|---|---|---|
| `calciuladoraSalarioPorHora.py` | Lê id, horas inteiras e valor/hora decimal | 40h a R$20,50 produz R$820,00 |
| `calculadoraConsumoCombustivel.py` | 300 km / 25 litros | Imprime consumo médio de 12,00 km/l |
| `calculadoraDesconto.py` | Cálculo de percentual de desconto | Testar desconto zero e total |
| `calculadoraMediaEscolar.py` | Média de notas | Conferir divisão e notas limites |
| `calculadoraSomaComEntradaUsuario.py` | Soma por input | Testar valores e entrada não numérica |
| `conversorDeMoeda.py` | Taxas literais dólar 5,6/euro 6,6, base R$100 | Atenção: código multiplica reais por taxas, não necessariamente converte corretamente |

## Decisões e limitações observadas
O arquivo de salário não valida horas negativas. O conversor usa taxas de câmbio fixas e multiplica o valor em reais; isso pode inverter o sentido da conversão BRL → moeda estrangeira. Não utilizar como cotação atual.

## Como executar
```powershell
python calciuladoraSalarioPorHora.py
python -m unittest discover -s tests -v
```

O segundo comando valida principalmente documentação existente; ele não substitui testes de saídas dos scripts. Para refatorar, primeiro isole cálculos em funções de Python com parâmetros explícitos e preserve os exemplos antes/depois.
