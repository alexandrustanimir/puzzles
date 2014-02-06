using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BalancedBrackets
{
    class Program
    {


         public static  void balanced_brackets(string s) {
        // Write your code here
        // To print results to the standard output you can use Console.WriteLine()
        // Example: Console.WriteLine("Hello world!");
        int idx = 0;
        int i =0 ;

        while (idx >= 0 && i < s.Length)
        {
            switch(s[i])
            {
                case ')' :
                    {
                         idx--;
                         i++;
                        break;
                    }
                case '(':
                    {
                        idx++;
                        i++;
                        break;
                    }
            };
      
            
        }
             if( idx != 0)
             {
                 Console.WriteLine("Unbalanced");
             }
             else
             {
                 Console.WriteLine("Balanced");
             }
        
    }
        static void Main(string[] args)
        {



        }
    }
}
