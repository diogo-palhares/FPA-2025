namespace programacaoDinamicaBacktracking
{
/*
* Autores: Davi Junio Roccha e grupo
* Data: Junho de 2025
* Versão: 2.0
* Descrição: Programação Dinâmica + Backtracking para listar todas as maiores subsequências comuns em ordem alfabética
*/

    using System;
    using System.Collections.Generic;
    using System.Linq;

    internal class LcsCompleto
    {
        static HashSet<string> resultados = new HashSet<string>();

        static void Main(string[] args)
        {

            Console.WriteLine("Digite o número de conjuntos de dados:");
            int conjuntos = int.Parse(Console.ReadLine());

            for (int d = 0; d < conjuntos; d++)
            {
                Console.WriteLine($"Conjunto {d + 1} - Digite a sequência de Helena:");
                string helena = Console.ReadLine();

                Console.WriteLine($"Conjunto {d + 1} - Digite a sequência de Marcus:");
                string marcus = Console.ReadLine();

                int[,] tabela = ConstruirTabela(helena, marcus);

                resultados.Clear();
                Backtrack(helena, marcus, helena.Length, marcus.Length, "", tabela);

                var listaFinal = resultados.ToList();
                listaFinal.Sort();

                foreach (var s in listaFinal)
                    Console.WriteLine(s);

                if (d < conjuntos - 1)
                    Console.WriteLine();

            }

        }

        // Constrói a tabela de DP
        static int[,] ConstruirTabela(string a, string b)
                {
                    int[,] tabela = new int[a.Length + 1, b.Length + 1];

                    for (int i = 1; i <= a.Length; i++)
                    {
                        for (int j = 1; j <= b.Length; j++)
                        {
                            if (a[i - 1] == b[j - 1])
                                tabela[i, j] = tabela[i - 1, j - 1] + 1;
                            else
                                tabela[i, j] = Math.Max(tabela[i - 1, j], tabela[i, j - 1]);
                        }
                    }

                    return tabela;
                }

        // Backtracking para reconstruir todas as subsequências mais longas
        static void Backtrack(string a, string b, int i, int j, string atual, int[,] tabela)
        {
            if (i == 0 || j == 0)
            {
                resultados.Add(new string(atual.Reverse().ToArray()));
                return;
            }

            if (a[i - 1] == b[j - 1])
            {
                Backtrack(a, b, i - 1, j - 1, a[i - 1] + atual, tabela);
            }
            else
            {
                if (tabela[i - 1, j] >= tabela[i, j - 1])
                    Backtrack(a, b, i - 1, j, atual, tabela);
                if (tabela[i, j - 1] >= tabela[i - 1, j])
                    Backtrack(a, b, i, j - 1, atual, tabela);
            }


        }
    }
}

