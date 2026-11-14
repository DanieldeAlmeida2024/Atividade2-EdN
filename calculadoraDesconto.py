"""Desconto em porcentagem com validação de dados."""
import math

def calcular_desconto(preco: float, percentual: float) -> tuple[float, float]:
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in (preco, percentual)):
        raise ValueError("Preço e desconto devem ser números finitos.")
    if preco < 0 or not 0 <= percentual <= 100:
        raise ValueError("Preço não pode ser negativo; desconto precisa estar entre 0 e 100.")
    valor_desconto = preco * percentual / 100
    return valor_desconto, preco - valor_desconto

def main():
    nome_produto = "Camiseta"
    preco_original = 50.00
    porcentagem_desconto = 20
    valor_desconto, preco_final = calcular_desconto(preco_original, porcentagem_desconto)
    print(f"Produto: {nome_produto}")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto Aplicado: {porcentagem_desconto}%")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
    print(f"Preço Final: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
