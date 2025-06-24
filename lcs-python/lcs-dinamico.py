# Autores: Guilherme Machado, Diogo Palhares, Ana Clara, Ana Flavia e Davi Junio Roccha
# Data: Junho de 2025
# Versão: 1.0
# Descrição: Programação Dinâmica e GUI



import tkinter as tk                             # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import messagebox, scrolledtext   # Importa módulos para caixas de diálogo e áreas de texto com scroll


def all_lcs_dp(seq1, seq2):
    m, n = len(seq1), len(seq2)                 # Guarda os comprimentos das duas sequências
    # Cria uma matriz dp de tamanho (m+1) x (n+1) onde cada célula guarda um conjunto de strings (as LCS possíveis)
    dp = [[set() for _ in range(n+1)] for _ in range(m+1)]
    
    # Inicializa a primeira coluna (dp[i][0]) com conjunto contendo string vazia
    for i in range(m+1):
        dp[i][0] = {""}
    # Inicializa a primeira linha (dp[0][j]) com conjunto contendo string vazia
    for j in range(n+1):
        dp[0][j] = {""}
    
    # Percorre as sequências caracter por caracter para preencher a tabela dp
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:                 # Se os caracteres atuais são iguais
                # Acrescenta o caractere atual a todas as LCS da posição diagonal anterior (i-1,j-1)
                dp[i][j] = {lcs + seq1[i-1] for lcs in dp[i-1][j-1]}
            else:
                # Se caracteres diferentes, pega o conjunto com as LCS de maior comprimento entre cima e esquerda
                len_top = len(next(iter(dp[i-1][j])))   # Tamanho de uma LCS do conjunto acima
                len_left = len(next(iter(dp[i][j-1])))  # Tamanho de uma LCS do conjunto da esquerda
                
                if len_top > len_left:
                    dp[i][j] = dp[i-1][j]             # Se topo maior, copia conjunto do topo
                elif len_top < len_left:
                    dp[i][j] = dp[i][j-1]             # Se esquerda maior, copia conjunto da esquerda
                else:
                    # Se iguais, une os dois conjuntos para considerar todas as LCS possíveis
                    dp[i][j] = dp[i-1][j].union(dp[i][j-1])
    # Retorna a lista das LCS ordenadas alfabeticamente na última célula dp[m][n]
    return sorted(dp[m][n])

def process_multiple_datasets(datasets):
    outputs = []                                  # Lista para armazenar os resultados de cada par de sequências
    for seq1, seq2 in datasets:
        lcs_list = all_lcs_dp(seq1, seq2)        # Calcula todas as LCS para o par atual
        outputs.append('\n'.join(lcs_list))      # Junta as LCS com quebras de linha e adiciona ao output
    return '\n\n'.join(outputs)                   # Junta os resultados de todos os pares, separados por linha em branco

def on_submit():
    try:
        # Obtém o texto da caixa de entrada, remove espaços nas bordas e separa por linhas
        raw = input_box.get("1.0", tk.END).strip().splitlines()
        
        if not raw:
            messagebox.showerror("Erro", "Entrada vazia.")   # Exibe erro se entrada estiver vazia
            return

        d = int(raw[0])                                       # Converte primeira linha para inteiro (número de pares)

        expected_lines = 1 + 2 * d                            # Calcula o número esperado de linhas: 1 + 2 linhas por par
        if len(raw) != expected_lines:
            # Se número de linhas for diferente do esperado, exibe erro com detalhes
            messagebox.showerror("Erro", f"Número de linhas inválido. Esperado {expected_lines} linhas, mas recebido {len(raw)}.")
            return

        # Cria uma lista de tuplas (pares de sequências) a partir das linhas seguintes
        datasets = [(raw[i], raw[i+1]) for i in range(1, 2*d + 1, 2)]
        output = process_multiple_datasets(datasets)           # Processa todos os pares para obter as LCS
        output_box.delete("1.0", tk.END)                       # Limpa a caixa de saída
        output_box.insert(tk.END, output)                      # Insere o resultado na caixa de saída

    except ValueError:
        # Caso erro na conversão para inteiro da primeira linha
        messagebox.showerror("Erro", "O primeiro valor deve ser um número inteiro representando o número de conjuntos.")
    except Exception as e:
        # Para outros erros inesperados, exibe a mensagem do erro
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da janela principal da GUI
root = tk.Tk()
root.title("LCS - Subsequência Comum Mais Longa (Programação Dinâmica)")

# Label explicativo para o campo de entrada
tk.Label(root, text="Entrada (1º número D, depois pares de sequências):").pack()
# Caixa de texto para entrada com barra de rolagem
input_box = scrolledtext.ScrolledText(root, width=60, height=10)
input_box.pack(padx=10, pady=5)

# Botão que chama a função on_submit ao ser clicado
tk.Button(root, text="Processar", command=on_submit).pack(pady=10)
# Autores: Guilherme Machado, Diogo Palhares, Ana Clara, Ana Flavia e Davi Junio Roccha
# Data: Junho de 2025
# Versão: 1.0
# Descrição: Programação Dinâmica e GUI

import tkinter as tk
from tkinter import messagebox, scrolledtext

def all_lcs_dp(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[set() for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = {""}
    for j in range(n+1):
        dp[0][j] = {""}

    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = {lcs + seq1[i-1] for lcs in dp[i-1][j-1]}
            else:
                len_top = len(next(iter(dp[i-1][j]), ""))
                len_left = len(next(iter(dp[i][j-1]), ""))

                if len_top > len_left:
                    dp[i][j] = dp[i-1][j]
                elif len_top < len_left:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j].union(dp[i][j-1])

    return sorted(dp[m][n])

def process_multiple_datasets(datasets):
    outputs = []
    for seq1, seq2 in datasets:
        lcs_list = all_lcs_dp(seq1, seq2)
        outputs.append('\n'.join(lcs_list))
    return '\n\n'.join(outputs)

def on_submit():
    try:
        raw = input_box.get("1.0", tk.END).strip().splitlines()
        if not raw:
            messagebox.showerror("Erro", "Entrada vazia.")
            return

        d = int(raw[0])
        if d > 10:
            messagebox.showerror("Erro", "O número de conjuntos (D) deve ser no máximo 10.")
            return
        expected_lines = 1 + 2 * d
        if len(raw) != expected_lines:
            messagebox.showerror("Erro", f"Número de linhas inválido. Esperado {expected_lines} linhas, mas recebido {len(raw)}.")
            return

        datasets = [(raw[i], raw[i+1]) for i in range(1, 2*d + 1, 2)]

        # Validação das sequências
        for idx, (s1, s2) in enumerate(datasets, 1):
            for seq in (s1, s2):
                if not seq.islower() or not seq.isalpha():
                    messagebox.showerror("Erro", f"Sequência inválida no conjunto {idx}. Use apenas letras minúsculas sem acentos ou símbolos.")
                    return
                if len(seq) > 80:
                    messagebox.showerror("Erro", f"Sequência muito longa no conjunto {idx}. Máximo permitido é 80 caracteres.")
                    return

        output = process_multiple_datasets(datasets)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)

    except ValueError:
        messagebox.showerror("Erro", "O primeiro valor deve ser um número inteiro representando o número de conjuntos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title("LCS - Subsequência Comum Mais Longa (Programação Dinâmica)")

tk.Label(root, text="Entrada (1º número D, depois pares de sequências):").pack()
input_box = scrolledtext.ScrolledText(root, width=60, height=10)
input_box.pack(padx=10, pady=5)

tk.Button(root, text="Processar", command=on_submit).pack(pady=10)

tk.Label(root, text="Saída:").pack()
output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(padx=10, pady=5)

root.mainloop()
# Label para a área de saída
tk.Label(root, text="Saída:").pack()
# Caixa de texto para saída com barra de rolagem
output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(padx=10, pady=5)

# Inicia o loop principal da interface para exibir a janela e tratar eventos
root.mainloop()
