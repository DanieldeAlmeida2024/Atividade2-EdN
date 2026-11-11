import ast
import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class TestesAtividades(unittest.TestCase):
    def test_documentos(self):
        for f in ('README.md','AGENTS.md','docs/REQUISITOS.md','docs/ARQUITETURA.md','docs/UML.puml','docs/PLANO_TESTES.md'):
            with self.subTest(f=f):self.assertTrue((R/f).is_file())
    def test_scripts_python_sintaxe(self):
        scripts=[p for p in R.rglob('*.py') if 'tests' not in p.parts]
        self.assertTrue(scripts)
        for p in scripts:
            with self.subTest(p=p): ast.parse(p.read_text(encoding='utf-8-sig'))
