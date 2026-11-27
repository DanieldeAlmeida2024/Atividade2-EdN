# Plano de testes — Atividade2-EdN

- CT-01 Arquivos do exercício presentes.
- CT-02 Todos os scripts .py compilam sintaticamente via ast.parse, sem executar.
- CT-03 Comparar manualmente os exemplos do README com as saídas.
- CT-04 Testar dados inválidos quando especificado no enunciado.

Executar `python -m unittest discover -s tests -v`. Os testes de comportamento cobrem cálculos, entradas inválidas e saídas reais em subprocessos. Os testes estruturais conferem os arquivos e a sintaxe.

Em CT-04, a soma recusa valor não inteiro e entrada incompleta. O salário recusa entrada encerrada antes da tarifa. Nos três casos, o processo sai com código 1, mostra uma mensagem de erro e não imprime resultado parcial.
