"""Conversão de BRL para moedas cotadas em reais por unidade."""
import math

def converter_reais(valor_brl: float, reais_por_unidade: float) -> float:
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in (valor_brl, reais_por_unidade)):
        raise ValueError("Valor e taxa devem ser números finitos.")
    if valor_brl < 0 or reais_por_unidade <= 0:
        raise ValueError("Valor não pode ser negativo e taxa deve ser positiva.")
    return valor_brl / reais_por_unidade

def main():
    valor_real, taxa_dolar, taxa_euro = 100.00, 5.60, 6.60
    print(f"Valor em reais: R$ {valor_real:.2f}")
    print(f"Valor em dólares: US$ {converter_reais(valor_real, taxa_dolar):.2f}")
    print(f"Valor em euros: € {converter_reais(valor_real, taxa_euro):.2f}")

if __name__ == "__main__":
    main()
