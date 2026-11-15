# EDN02-NUM-02 — Contrato numérico dos cinco calculadores

14/11/2026 · Conversão de moeda, desconto, média, consumo e salário.

## Defeitos
- Em Python, `bool` herda de `int`: `True` era aceito como quantidade 1 e `False` como zero, inclusive em preços e taxas.
- `math.isfinite()` em inteiros enormes podia levantar `OverflowError` fora do contrato público.
- Divisões, somas ou multiplicações com operandos finitos podiam produzir resultado infinito, aceito silenciosamente.

## Correção
- `numeros.py` concentra a validação estrita de `int` e `float`, exclui `bool` e trata o overflow de coerção para ponto flutuante.
- Os cinco exercícios verificam operandos e resultados antes de retornar.
- Desconto efetua `preco * (percentual / 100)` para evitar overflow intermediário evitável.
- Regressões rejeitam booleanos e overflow, preservando a saída CLI dos valores originais.

## Limites
São cálculos didáticos em float, não aritmética monetária de produção com Decimal e arredondamento contábil.
