"""Testes de cálculo e dos cinco exercícios em CLI da Atividade 02."""
import importlib.util
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def carregar(path):
    spec = importlib.util.spec_from_file_location(path.replace(".py", ""), ROOT / path)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

moeda = carregar("conversorDeMoeda.py")
desconto = carregar("calculadoraDesconto.py")
media = carregar("calculadoraMediaEscolar.py")
consumo = carregar("calculadoraConsumoCombustivel.py")
salario = carregar("calciuladoraSalarioPorHora.py")


class TestesAtividade02(unittest.TestCase):
    def test_cambio_divide_por_taxa_em_brl(self):
        self.assertAlmostEqual(17.857142857, moeda.converter_reais(100, 5.60), places=6)
        self.assertAlmostEqual(15.151515151, moeda.converter_reais(100, 6.60), places=6)
        self.assertEqual(0, moeda.converter_reais(0, 5.6))

    def test_cambio_rejeita_taxa_invalida(self):
        for valor, taxa in ((100, 0), (100, -1), (-1, 5.6), (100, float('nan'))):
            with self.subTest(valor=valor, taxa=taxa), self.assertRaises(ValueError):
                moeda.converter_reais(valor, taxa)

    def test_desconto_do_enunciado(self):
        self.assertEqual((10.0, 40.0), desconto.calcular_desconto(50, 20))
        self.assertEqual((50.0, 0.0), desconto.calcular_desconto(50, 100))
        with self.assertRaises(ValueError):
            desconto.calcular_desconto(50, 120)

    def test_media_e_intervalos(self):
        self.assertAlmostEqual(7.3333333, media.calcular_media([7.5, 8, 6.5]), places=6)
        with self.assertRaises(ValueError):
            media.calcular_media([])
        with self.assertRaises(ValueError):
            media.calcular_media([11])

    def test_consumo_e_divisao_por_zero(self):
        self.assertAlmostEqual(12, consumo.calcular_consumo(300, 25))
        with self.assertRaises(ValueError):
            consumo.calcular_consumo(300, 0)

    def test_salario_com_horas_fracionarias(self):
        self.assertAlmostEqual(175, salario.calcular_salario(7.5, 23.333333333), places=5)
        with self.assertRaises(ValueError):
            salario.calcular_salario(-1, 20)

    def test_cli_cambio_mostra_dolares_e_euros(self):
        p = subprocess.run([sys.executable, str(ROOT / "conversorDeMoeda.py")],
                           capture_output=True, text=True, timeout=10)
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("US$ 17.86", p.stdout)
        self.assertIn("€ 15.15", p.stdout)

    def test_cli_media_mostra_todas_as_notas(self):
        p = subprocess.run([sys.executable, str(ROOT / "calculadoraMediaEscolar.py")],
                           capture_output=True, text=True, timeout=10)
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("Nota 1: 7.50", p.stdout)
        self.assertIn("Nota 2: 8.00", p.stdout)
        self.assertIn("Nota 3: 6.50", p.stdout)
        self.assertIn("Média das notas: 7.33", p.stdout)

    def test_cli_salario_validacao(self):
        p = subprocess.run([sys.executable, str(ROOT / "calciuladoraSalarioPorHora.py")],
                           input="42\n40\n20\n", capture_output=True, text=True, timeout=10)
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("R$ 800.00", p.stdout)
        invalid = subprocess.run([sys.executable, str(ROOT / "calciuladoraSalarioPorHora.py")],
                                 input="42\n-5\n20\n", capture_output=True, text=True, timeout=10)
        self.assertNotEqual(0, invalid.returncode)
        self.assertIn("Erro:", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
