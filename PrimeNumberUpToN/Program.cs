using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PrimeNumberUpToN
{
    class Program
    {



        bool IsPrime(int n)
        {
            if (n == 1) return true;
            if (n == 2) return true;
            for (int k = 2; k <= Math.Ceiling(Math.Sqrt(n)); k++)
            {
                if (n % k == 0)
                {
                    return false;
                }
            }

            return true;
        }
        public void get_prime_numbers(int n)
        {
            // Write your code here
            // To print results to the standard output you can use Console.WriteLine()
            // Example: Console.WriteLine("Hello world!");
            for (int i = 2; i < n; i++)
            {
                if (IsPrime(i))
                {
                    Console.Write(i);
                    Console.Write(
                        " ");
                }
            }


        }

       
        static void Main(string[] args)
        {
        }
    }
}
