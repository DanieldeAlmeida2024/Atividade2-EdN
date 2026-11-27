"""Soma de dois números inteiros informados no terminal."""


def main():
    try:
        primeiro = int(input("Digite o primeiro valor: "))
        segundo = int(input("Digite o segundo valor: "))
    except EOFError:
        raise SystemExit("Erro: entrada encerrada antes dos dois números inteiros.") from None
    except ValueError:
        raise SystemExit("Erro: informe dois números inteiros.") from None
    print(f"X = {primeiro + segundo}")


if __name__ == "__main__":
    main()
