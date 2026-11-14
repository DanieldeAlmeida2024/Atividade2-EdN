# Atividade2-EdN — atividades Python

Exercícios Python de aritmética aplicada: conversão de moeda, desconto, médias, consumo e salário.

## Requisitos
Python 3.10+ e terminal local; não há serviço HTTP ou banco de dados obrigatório nesta atividade.

## Executar
```bash
python conversorDeMoeda.py
```

Cada script é um exercício independente. Outros arquivos existentes: `conversorDeMoeda.py, calculadoraDesconto.py, calculadoraMediaEscolar.py, calculadoraConsumoCombustivel.py, calciuladoraSalarioPorHora.py`.

## Testes
```bash
python -m unittest discover -s tests -v
```

Os testes adicionados verificam presença de arquivos, documentação e sintaxe de código; para validar comportamento, é necessário comparar a entrada e saída de cada exercício com o enunciado original.

## Correções funcionais e resultados verificáveis

Os cinco exercícios agora possuem funções reutilizáveis e testes automatizados de saída e validação:

- **Câmbio:** como a cotação é em **reais por 1 unidade estrangeira**, a conversão correta divide `R$ 100 / R$ 5,60` e `R$ 100 / R$ 6,60`. Resultados esperados: **US$ 17,86 e € 15,15**. São taxas fixas do enunciado, não cotações atuais.
- **Desconto:** verifica limites de 0 a 100%; R$ 50 com 20% resulta em R$ 40.
- **Média escolar:** apresenta as três notas e a média 7,33.
- **Combustível:** 300 km / 25 L = 12 km/L; consumo com zero litro é inválido.
- **Salário:** aceita horas fracionárias e rejeita números negativos ou não finitos.

Para reproduzir: `python -m unittest discover -s tests -p 'test_*.py' -v`. O CI executa esses cenários em PRs e na `main`.

## Documentação
[Requisitos](docs/REQUISITOS.md) · [Arquitetura](docs/ARQUITETURA.md) · [UML](docs/UML.puml) · [Plano de testes](docs/PLANO_TESTES.md) · [Guia de IA](AGENTS.md).

---

## Enunciados anteriores preservados

## Atividade Prática 02
### 1- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:



Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.


### 2- Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:



Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


### 3- Calculadora de Média Escolar 

Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:



Nota 1: 7.5

Nota 2: 8.0

Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.


### 4- Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:



Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.


### 5- Calculadora de Soma com Entrada do Usuário


Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.



### 6- Calculadora de salário por horas trabalhadas

Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:


Número do funcionário (numero_funcionario).

Quantidade de horas trabalhadas (horas_trabalhadas).

Valor recebido por hora (valor_por_hora).

Saída:








Imprima o número do funcionário e o salário calculado com duas casas decimais. Deve haver um espaço em branco antes e depois do sinal de igualdade, e no caso do salário, também um espaço em branco após o R$
