import psutil              # Biblioteca para monitorar o uso de recursos do sistema (memória, CPU etc)
import os                  # Biblioteca para interagir com o sistema operacional (pegar PID do processo)
import time                # Biblioteca para medir tempo de execução

# Função que imprime o uso atual de memória do processo em megabytes (MB)
def print_memory_usage(stage):
    process = psutil.Process(os.getpid())               # Pega o processo atual usando seu PID
    mem = process.memory_info().rss / 1024**2           # Pega a memória usada (rss = resident set size) e converte para MB
    print(f"[{stage}] Uso de memória: {mem:.2f} MB")    # Imprime o valor formatado com 2 casas decimais

# Função que constrói a tabela DP para o problema da LCS (backtracking)
def build_dp_table(seq1, seq2):
    m, n = len(seq1), len(seq2)                          # Tamanhos das sequências
    dp = [[0]*(n+1) for _ in range(m+1)]                 # Inicializa matriz (m+1 x n+1) com zeros
    
    # Preenche a matriz dp conforme algoritmo clássico da LCS
    for i in range(m):
        for j in range(n):
            if seq1[i] == seq2[j]:                       # Se caracteres iguais, incrementa o valor diagonal
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                # Se diferentes, pega o máximo entre cima e esquerda
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp                                            # Retorna a tabela preenchida

# Função recursiva para fazer backtracking na tabela dp e gerar todas as LCS possíveis
def backtrack(dp, seq1, seq2, i, j, path, results):
    if i == 0 or j == 0:                                # Caso base: chegou à borda da tabela
        results.add(''.join(reversed(path)))           # Adiciona a LCS construída (revertida) no conjunto resultados
        return
    if seq1[i-1] == seq2[j-1]:                         # Se os caracteres são iguais, inclui no caminho
        path.append(seq1[i-1])
        backtrack(dp, seq1, seq2, i-1, j-1, path, results)
        path.pop()                                      # Remove para explorar outras possibilidades (backtracking)
    else:
        # Se caracteres diferentes, explora o caminho com maior valor na tabela dp
        if dp[i-1][j] >= dp[i][j-1]:
            backtrack(dp, seq1, seq2, i-1, j, path, results)
        if dp[i][j-1] >= dp[i-1][j]:
            backtrack(dp, seq1, seq2, i, j-1, path, results)

# Função que executa o processo completo do método backtracking
def lcs_backtracking(seq1, seq2):
    dp = build_dp_table(seq1, seq2)                    # Constroi a tabela dp
    results = set()                                    # Conjunto para armazenar as LCS sem repetições
    backtrack(dp, seq1, seq2, len(seq1), len(seq2), [], results)  # Executa backtracking
    print_memory_usage("Depois")  
    return sorted(results)                             # Retorna as LCS ordenadas alfabeticamente


# Função que resolve o problema usando somente programação dinâmica armazenando conjuntos de subsequências
def all_lcs_dp(seq1, seq2):
    m, n = len(seq1), len(seq2)                        # Tamanhos das sequências
    # Cria matriz dp onde cada posição guarda um conjunto de strings (subsequências)
    dp = [[set() for _ in range(n+1)] for _ in range(m+1)]
    
    # Inicializa a primeira coluna com conjunto contendo string vazia
    for i in range(m+1):
        dp[i][0] = {""}
    # Inicializa a primeira linha com conjunto contendo string vazia
    for j in range(n+1):
        dp[0][j] = {""}
    
    # Preenche a tabela dp, armazenando todas as LCS parciais
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                # Se caracteres iguais, acrescenta o caractere atual a todas as LCS diagonais anteriores
                dp[i][j] = {lcs + seq1[i-1] for lcs in dp[i-1][j-1]}
            else:
                # Se diferentes, verifica qual conjunto tem LCS maior
                len_top = len(next(iter(dp[i-1][j])))    # Tamanho de uma LCS do conjunto superior
                len_left = len(next(iter(dp[i][j-1])))   # Tamanho de uma LCS do conjunto esquerdo
                
                if len_top > len_left:
                    dp[i][j] = dp[i-1][j]               # Usa o conjunto de cima
                elif len_top < len_left:
                    dp[i][j] = dp[i][j-1]               # Usa o conjunto da esquerda
                else:
                    # Se empatados, une os dois conjuntos (evitando duplicatas)
                    dp[i][j] = dp[i-1][j].union(dp[i][j-1])
    print_memory_usage("Depois")  
    return sorted(dp[m][n])                            # Retorna as LCS ordenadas da última célula

# Sequências grandes para testar os dois métodos
seq1 = "abcbdab" * 30                               # Sequência seq1 repetida n vezes (n*7)
seq2 = "bdcababc" * 30                              # Sequência seq2 repetida n vezes (n*8)

print("Teste Backtracking:")
print_memory_usage("Início")                         # Imprime uso de memória antes do processamento
start = time.time()                                  # Marca o tempo inicial
res_bt = lcs_backtracking(seq1, seq2)                # Executa o método backtracking
end = time.time()                                    # Marca o tempo final
print_memory_usage("Depois")                          # Imprime uso de memória após processamento
print(f"Tempo: {end - start:.4f} segundos")          # Imprime tempo total gasto
print(f"Número de LCS encontradas: {len(res_bt)}\n") # Imprime quantidade de LCS encontradas

print("Teste DP com conjuntos:")
print_memory_usage("Início")                         # Imprime uso de memória antes do processamento
start = time.time()                                  # Marca o tempo inicial
res_dp = all_lcs_dp(seq1, seq2)                      # Executa o método só com programação dinâmica
end = time.time()                                    # Marca o tempo final
print_memory_usage("Depois")                          # Imprime uso de memória após processamento
print(f"Tempo: {end - start:.4f} segundos")          # Imprime tempo total gasto
print(f"Número de LCS encontradas: {len(res_dp)}\n") # Imprime quantidade de LCS encontradas
