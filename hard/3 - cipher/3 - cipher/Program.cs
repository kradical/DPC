using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace _3___cipher
{
    class Program
    {

        public static string checkList(string de, string[] wordlist)
        {
            int charTotal1 = 0;
            int charTotal2 = 0;
            foreach (char e in de)
            {
                charTotal2 += Convert.ToInt32(e);
            }
            foreach (string lel in wordlist)
            {
                charTotal1 = 0;
                foreach (char d in lel)
                {
                    charTotal1 += Convert.ToInt32(d);
                }
                if (charTotal1 == charTotal2)
                {
                    return lel;
                }
            }
            Console.WriteLine(charTotal1);
            Console.WriteLine(charTotal2);
            return "not found";
        }

        static void Main(string[] args)
        {
            string[] wordlist = System.IO.File.ReadAllLines(@"C:\Users\Mike\Documents\GitHub\DPC\hard\3 - cipher\3 - cipher\wordlist.txt");
            string[] dscramble = { "mkeart", "edcudls", "iragoge", "usrlsle", "nalraoci", "nsdeuto", "amrhat", "inknsy", "iferkna" };
            foreach (string d in dscramble)
            {
                Console.WriteLine(checkList(d, wordlist));
            }
            Console.WriteLine();
        }
    }
}
