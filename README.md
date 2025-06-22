# README - Trabalho Prático de Programação Dinâmica

# Autores: Guilherme Machado, Diogo Palhares, Ana Clara, Ana Flavia e Davi Junio Roccha
# Data: Junho de 2025
# Versão: 1.0
# Descrição: Programação Dinâmica + Backtracking para listar todas as maiores subsequências comuns em ordem alfabética e GUI

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

## 4. Qual é a complexidade da solução proposta?
Versão com apenas programação dinâmica (sem backtracking):

Tempo: O(n × m), onde n e m são os tamanhos das sequências.

Espaço: Pode chegar a O(n × m × k), onde k é o número médio de subsequências por célula — potencialmente muito alto.

Versão com programação dinâmica + backtracking:

Tempo: O(2^(n+m)) no pior caso, pois o número de caminhos válidos pode crescer exponencialmente, embora a tabela DP limite as chamadas.

Espaço: O(n × m) para a tabela de inteiros + uso da pilha de chamadas recursivas.

## 5. O que o grupo aprendeu ao resolver esse problema?
Aprendemos a aplicar a programação dinâmica como ferramenta para dividir e resolver problemas complexos, e também a usar backtracking para reconstruir soluções completas a partir de uma estrutura de apoio. Aprendemos a importância de:

Tratar eficientemente estruturas de dados, como conjuntos (set) para eliminar duplicações.

Comparar abordagens com base em desempenho e consumo de memória, aplicando medição com psutil e time.

Desenvolver uma interface gráfica com tkinter que integra entrada, processamento e saída de forma intuitiva para o usuário.
