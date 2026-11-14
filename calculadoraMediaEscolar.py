"""Média aritmética de notas escolares."""
import math

def calcular_media(notas: list[float]) -> float:
    if not notas or any(not isinstance(n, (int, float)) or not math.isfinite(n) or not 0 <= n <= 10 for n in notas):
        raise ValueError("Informe notas finitas entre 0 e 10.")
    return sum(notas) / len(notas)

def main():
    notas = [7.5, 8.0, 6.5]
    for indice, nota in enumerate(notas, start=1):
        print(f"Nota {indice}: {nota:.2f}")
    print(f"Média das notas: {calcular_media(notas):.2f}")

if __name__ == "__main__":
    main()
