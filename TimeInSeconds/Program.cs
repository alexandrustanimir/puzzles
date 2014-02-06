using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TimeInSeconds
{
    class Program
    {

        public static void convert_seconds(int seconds)
        {
            // Write your code here
            // To print results to the standard output you can use Console.WriteLine()
            // Example: Console.WriteLine("Hello world!");
            int hour =seconds/3600;
            int minutes = (seconds %3600 )/ 60;
            int sec = ((seconds % 3600) % 60);

            Console.WriteLine(string.Format("{0}:{1}:{2}",hour.ToString("00"),minutes.ToString("00"),sec.ToString("00")));
        }
        static void Main(string[] args)
        {
            convert_seconds(34565);
        }
    }
}
