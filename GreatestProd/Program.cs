using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GreatestProd
{
    class Program
    {

        public static void max_prod(int[] v)
        {
            // Write your code here
            // To print results to the standard output you can use Console.WriteLine()
            // Example: Console.WriteLine("Hello world!");
            
            Array.Sort(v);
            for (int i = v.Length - 1; i >= 0;i-- )
                for (int k = i-1; k >= 0; k--)
                {
                    if (v[i] % 3 * v[k] % 3  == 0)
                    {
                        Console.WriteLine(v[i] * v[k]);
                        i = -1;
                        k = -1;
                    }
                }

        }
        static void Main(string[] args)
        {
            max_prod(new int[]{6,8,8,7,2,5});
        }
    }
}
