namespace programacaoDinamica
{
    internal class LcsDinamica
    {
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

                int[,] tabela = new int[helena.Length + 1, marcus.Length + 1];

                // Preenchimento da tabela usando Programação Dinâmica
                for (int i = 1; i <= helena.Length; i++)
                {
                    for (int j = 1; j <= marcus.Length; j++)
                    {
                        if (helena[i - 1] == marcus[j - 1])
                            tabela[i, j] = tabela[i - 1, j - 1] + 1;
                        else
                            tabela[i, j] = Math.Max(tabela[i - 1, j], tabela[i, j - 1]);
                    }
                }

                Console.WriteLine("Tamanho da maior subsequência comum: " + tabela[helena.Length, marcus.Length]);
                Console.WriteLine();
            }
        }
    }
}
