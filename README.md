#  Trabalho Prático de Programação Dinâmica
`CURSO: Sistemas de Informação`

`DISCIPLINA: Fundamentos de Projeto e Análise de Algoritmos`

## Integrantes

* Ana Clara Lima Marçal
* Ana Flavia de Oliveira Costa
* Davi Júnio Rocha
* Diogo Campos Palhares
* Guilherme Henrique de Lima Machado
  
## Descrição
* Data: Junho de 2025
* Versão: 1.0
* Programação Dinâmica + Backtracking para listar todas as maiores subsequências comuns em ordem alfabética e GUI

## 1. Como a programação dinâmica foi aplicada na solução?
Utilizamos programação dinâmica para construir uma tabela (matriz DP) que armazena o comprimento da maior subsequência comum entre as sequências de Helena e Marcus. Essa tabela permite evitar recomputações de subproblemas ao reaproveitar os resultados parciais já calculados. Também foi implementada uma variação onde a própria tabela armazena conjuntos com as subsequências parciais, eliminando a necessidade de backtracking, embora com custo maior de memória.

## 2. Por que o uso de backtracking é necessário neste problema?
O backtracking é necessário na abordagem tradicional para reconstruir todas as possíveis subsequências comuns mais longas. A tabela construída pela programação dinâmica guarda apenas os tamanhos das LCS parciais, não suas composições. O backtracking percorre a tabela de forma recursiva, explorando todos os caminhos que levam ao valor máximo da LCS, adicionando cada solução válida a um conjunto de resultados.

## 3. Houve desafios na implementação? Quais? Como foram superados?
Sim. Os principais desafios foram:

Evitar duplicatas nas subsequências geradas durante o backtracking.

Garantir que as soluções fossem exibidas em ordem alfabética.

Controlar o uso de memória na versão alternativa com conjuntos de strings armazenadas diretamente na tabela.

Esses desafios foram superados:

Utilizando set() para armazenar os resultados, que elimina duplicatas automaticamente.

Ordenando os resultados com sorted() antes de exibir.

Implementando testes comparativos com psutil para avaliar e entender os impactos de memória entre as abordagens.

## 4. Qual é a complexidade da solução proposta? Faça o cálculo da ordem de complexidade passo a passo para:

---

### a) Versão utilizando apenas programação dinâmica (`lcs-dinamico.py`):

A matriz `dp` é criada com dimensão `(m+1) × (n+1)` e armazena, em cada célula, um **conjunto de todas as subsequências comuns mais longas** encontradas até aquele ponto. Essas subsequências são strings de tamanho até `L` (comprimento da LCS), e podem haver até `k` subsequências distintas (o enunciado limita em até 1000).

No trecho abaixo, vemos que cada célula do `dp` armazena e atualiza conjuntos de strings, com concatenação explícita:

```python
dp[i][j] = {lcs + seq1[i-1] for lcs in dp[i-1][j-1]}
```

Além disso, quando os caracteres são diferentes, o algoritmo faz união entre conjuntos:

```python
dp[i][j] = dp[i-1][j] | dp[i][j-1]
```

Portanto:

- **Complexidade de Tempo:**
  - **O(m × n × k × L)** no pior caso, com concatenação de até `k` strings por célula
  - **Ω(m × n)** no melhor caso (poucas ou nenhuma coincidência)
  - **Θ(m × n × k × L)** no caso médio

- **Complexidade de Espaço:**
  - **O(m × n × k × L)** (armazenamento de todas as subsequências por célula)
  - **Ω(m × n)** no melhor caso
  - **Θ(m × n × k × L)** no caso médio

---

### b) Versão com programação dinâmica e backtracking (`lcs-completo.py`):

Primeiro, é construída a matriz `dp` que armazena apenas inteiros com o tamanho da LCS:

```python
dp[i+1][j+1] = dp[i][j] + 1
```

Em seguida, o algoritmo aplica **backtracking recursivo** para reconstruir todas as LCS de tamanho máximo:

```python
results.add(''.join(reversed(path)))
```

Diferente da versão anterior, aqui **não são armazenadas todas as soluções intermediárias** — apenas a matriz de inteiros e o conjunto final com as LCS.

Portanto:

- **Complexidade de Tempo:**
  - **O(m × n + k × L)** no pior caso, somando o custo de construir a matriz e gerar todas as `k` subsequências
  - **Ω(m × n)** no melhor caso
  - **Θ(m × n + k × L)** no caso médio

- **Complexidade de Espaço:**
  - **O(m × n + k × L)** (matriz + conjunto de resultados)
  - **Ω(m × n)** no melhor caso
  - **Θ(m × n + k × L)** no caso médio

## 5. O que o grupo aprendeu ao resolver esse problema?
Aprendemos a aplicar a programação dinâmica como ferramenta para dividir e resolver problemas complexos, e também a usar backtracking para reconstruir soluções completas a partir de uma estrutura de apoio. Aprendemos a importância de:

Tratar eficientemente estruturas de dados, como conjuntos (set) para eliminar duplicações.

Comparar abordagens com base em desempenho e consumo de memória, aplicando medição com psutil e time.

Desenvolver uma interface gráfica com tkinter que integra entrada, processamento e saída de forma intuitiva para o usuário.
