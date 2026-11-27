"""Calculadora interativa de salário por hora trabalhada."""
from numeros import numero_finito, resultado_finito

def calcular_salario(horas: float, valor_hora: float) -> float:
    if not all(numero_finito(x) for x in (horas, valor_hora)):
        raise ValueError("Horas e valor por hora devem ser números finitos.")
    if horas < 0 or valor_hora < 0:
        raise ValueError("Horas e valor por hora não podem ser negativos.")
    return resultado_finito(horas * valor_hora)

def main():
    try:
        numero = int(input("Digite o número do funcionário: "))
        horas = float(input("Digite a quantidade de horas trabalhadas: "))
        valor_hora = float(input("Digite o valor recebido por hora(separe com .): "))
        if numero <= 0:
            raise ValueError("O número do funcionário deve ser positivo.")
        salario = calcular_salario(horas, valor_hora)
    except EOFError:
        raise SystemExit("Erro: entrada encerrada antes dos três dados do salário.") from None
    except ValueError as erro:
        raise SystemExit(f"Erro: {erro}")
    print(f"Número do funcionário : {numero}")
    print(f"Salário calculado : R$ {salario:.2f}")

if __name__ == "__main__":
    main()
