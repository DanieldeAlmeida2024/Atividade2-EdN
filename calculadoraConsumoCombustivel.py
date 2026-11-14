"""Consumo médio em quilômetros por litro."""
import math

def calcular_consumo(distancia_km: float, litros: float) -> float:
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in (distancia_km, litros)):
        raise ValueError("Distância e combustível devem ser números finitos.")
    if distancia_km < 0 or litros <= 0:
        raise ValueError("Distância não pode ser negativa e litros devem ser positivos.")
    return distancia_km / litros

def main():
    distancia_km, combustivel_litros = 300, 25
    print(f"Distância percorrida: {distancia_km} Km")
    print(f"Combustível gasto: {combustivel_litros} Litros")
    print(f"Consumo médio do veículo: {calcular_consumo(distancia_km, combustivel_litros):.2f} Km/l")

if __name__ == "__main__":
    main()
