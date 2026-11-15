"""Contrato numérico compartilhado pelos cinco exercícios da Atividade 02."""
import math


def numero_finito(valor) -> bool:
    """bool não é quantidade numérica; inteiros arbitrários não podem estourar math.isfinite."""
    if type(valor) not in (int, float):
        return False
    try:
        return math.isfinite(valor)
    except OverflowError:
        return False


def resultado_finito(valor: float) -> float:
    if not numero_finito(valor):
        raise ValueError("O resultado numérico está fora do intervalo finito.")
    return valor
