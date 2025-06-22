# Autores: Guilherme Machado, Diogo Palhares, Ana Clara, Ana Flavia e Davi Junio Roccha
# Data: Junho de 2025
# Versão: 1.0
# Descrição: Programação Dinâmica + Backtracking para listar todas as maiores subsequências comuns em ordem alfabética e GUI


import tkinter as tk                             # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import messagebox, scrolledtext   # Importa módulos para caixas de diálogo e áreas de texto com scroll


def build_dp_table(seq1, seq2):
    # Guarda o tamanho das duas sequências de entrada
    m, n = len(seq1), len(seq2)
    # Cria uma matriz (lista de listas) com dimensões (m+1) x (n+1) preenchida com zeros
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Preenche a tabela DP para calcular o tamanho da maior subsequência comum (LCS)
    for i in range(m):
        for j in range(n):
            if seq1[i] == seq2[j]:
                # Se os caracteres nas posições i e j são iguais, incrementa o valor da diagonal anterior em 1
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                # Se não, pega o maior valor entre o da linha acima ou da coluna à esquerda
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    # Retorna a tabela DP completa
    return dp


def backtrack(dp, seq1, seq2, i, j, path, results):
    # Caso base: se chegou ao início de alguma das sequências
    if i == 0 or j == 0:
        # Junta os caracteres do caminho atual (invertidos, pois backtracking vai do fim ao início)
        # e adiciona no conjunto de resultados para evitar duplicatas
        results.add(''.join(reversed(path)))
        return
    
    if seq1[i-1] == seq2[j-1]:
        # Se os caracteres atuais são iguais, adiciona no caminho
        path.append(seq1[i-1])
        # Move diagonalmente para cima e para esquerda (reduz os índices)
        backtrack(dp, seq1, seq2, i-1, j-1, path, results)
        # Remove o último caractere para tentar outras possibilidades (backtracking)
        path.pop()
    else:
        # Se os caracteres não são iguais, decide o caminho baseado nos valores da tabela DP
        if dp[i-1][j] >= dp[i][j-1]:
            # Vai para cima se o valor acima é maior ou igual ao da esquerda
            backtrack(dp, seq1, seq2, i-1, j, path, results)
        if dp[i][j-1] >= dp[i-1][j]:
            # Vai para esquerda se o valor da esquerda é maior ou igual ao de cima
            backtrack(dp, seq1, seq2, i, j-1, path, results)


def find_all_lcs(seq1, seq2):
    # Constrói a tabela DP para as duas sequências
    dp = build_dp_table(seq1, seq2)
    # Cria um conjunto para armazenar os resultados únicos
    results = set()
    # Inicia o backtracking no fim da tabela DP para encontrar todas as LCS possíveis
    backtrack(dp, seq1, seq2, len(seq1), len(seq2), [], results)
    # Retorna os resultados ordenados alfabeticamente
    return sorted(results)


def process_multiple_datasets(datasets):
    # Lista que armazenará a saída de cada par de sequências
    outputs = []
    for seq1, seq2 in datasets:
        # Para cada par, calcula todas as LCS
        lcs_list = find_all_lcs(seq1, seq2)
        # Junta as LCS com quebras de linha e adiciona na lista outputs
        outputs.append('\n'.join(lcs_list))
    # Junta os resultados de todos os pares com uma linha em branco entre eles
    return '\n\n'.join(outputs)




def on_submit():
    try:
        # Lê o texto da caixa de entrada, remove espaços em branco nas bordas e separa em linhas
        raw = input_box.get("1.0", tk.END).strip().splitlines()
        # Se a entrada estiver vazia, mostra mensagem de erro e sai
        if not raw:
            messagebox.showerror("Erro", "Entrada vazia.")
            return

        # Converte a primeira linha para inteiro, que representa o número de pares (d)
        d = int(raw[0])

        # Calcula o número esperado de linhas: 1 para d + 2 linhas por par de sequências
        expected_lines = 1 + 2 * d
        # Verifica se o número de linhas da entrada bate com o esperado
        if len(raw) != expected_lines:
            messagebox.showerror("Erro", f"Número de linhas inválido. Esperado {expected_lines} linhas, mas recebido {len(raw)}.")
            return

        # Cria a lista de pares (datasets), pegando linhas em pares a partir da segunda linha
        datasets = [(raw[i], raw[i+1]) for i in range(1, 2*d + 1, 2)]
        # Processa os pares para gerar as LCS
        output = process_multiple_datasets(datasets)
        # Limpa a caixa de saída
        output_box.delete("1.0", tk.END)
        # Insere o resultado na caixa de saída
        output_box.insert(tk.END, output)
    except ValueError:
        # Caso a conversão para inteiro falhe (primeira linha não for número), exibe erro amigável
        messagebox.showerror("Erro", "O primeiro valor deve ser um número inteiro representando o número de conjuntos.")
    except Exception as e:
        # Para outros erros, exibe a mensagem do erro
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


# Configuração da interface gráfica (GUI)

# Cria a janela principal
root = tk.Tk()
# Define o título da janela
root.title("LCS - Subsequência Comum Mais Longa")

# Adiciona um label explicativo para o campo de entrada
tk.Label(root, text="Entrada (1º número D, depois pares de sequências):").pack()
# Cria uma caixa de texto com barra de rolagem para entrada, tamanho 60x10 caracteres
input_box = scrolledtext.ScrolledText(root, width=60, height=10)
input_box.pack(padx=10, pady=5)

# Cria um botão para processar, que chama a função on_submit quando clicado
tk.Button(root, text="Processar", command=on_submit).pack(pady=10)

# Adiciona um label para a saída
tk.Label(root, text="Saída:").pack()
# Cria uma caixa de texto com barra de rolagem para mostrar o resultado, tamanho 60x15 caracteres
output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(padx=10, pady=5)

# Inicia o loop principal da GUI, que mantém a janela aberta e responde a eventos
root.mainloop()
