# Autores: Guilherme Machado, Diogo Palhares, Ana Clara, Ana Flavia e Davi Junio Roccha
# Data: Junho de 2025
# Versão: 1.0
# Descrição: Programação Dinâmica + Backtracking para listar todas as maiores subsequências comuns em ordem alfabética e GUI

import tkinter as tk
from tkinter import messagebox, scrolledtext

def build_dp_table(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if seq1[i] == seq2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp

def backtrack(dp, seq1, seq2, i, j, path, results):
    if i == 0 or j == 0:
        results.add(''.join(reversed(path)))
        return

    if seq1[i-1] == seq2[j-1]:
        path.append(seq1[i-1])
        backtrack(dp, seq1, seq2, i-1, j-1, path, results)
        path.pop()
    else:
        if dp[i-1][j] >= dp[i][j-1]:
            backtrack(dp, seq1, seq2, i-1, j, path, results)
        if dp[i][j-1] >= dp[i-1][j]:
            backtrack(dp, seq1, seq2, i, j-1, path, results)

def find_all_lcs(seq1, seq2):
    dp = build_dp_table(seq1, seq2)
    results = set()
    backtrack(dp, seq1, seq2, len(seq1), len(seq2), [], results)
    return sorted(results)

def process_multiple_datasets(datasets):
    outputs = []
    for seq1, seq2 in datasets:
        lcs_list = find_all_lcs(seq1, seq2)
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
root.title("LCS - Subsequência Comum Mais Longa")

tk.Label(root, text="Entrada (1º número D, depois pares de sequências):").pack()
input_box = scrolledtext.ScrolledText(root, width=60, height=10)
input_box.pack(padx=10, pady=5)

tk.Button(root, text="Processar", command=on_submit).pack(pady=10)

tk.Label(root, text="Saída:").pack()
output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(padx=10, pady=5)

root.mainloop()

# Exemplos com muitas subsequencias:

# ajsifbasijbfsaijfbiasj
# ggijfaugauf9bgafio

# faspfsapiniposngaiasngapsighapsigh
# sagsaighjpqwihgpiqwhaspghsapgasgjp

# ijkijkii
# ikjikji