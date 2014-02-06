using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntToBinary
{
    class Program
    {

        public static void convert_to_binary(int n)
        {
            // Write your code here
            // To print results to the standard output you can use Console.WriteLine()
            // Example: Console.WriteLine("Hello world!");
        Console.Write(    Convert.ToString(n, 2));

        }
        static void Main(string[] args)
        {
            convert_to_binary(2);
        }
    }
}
