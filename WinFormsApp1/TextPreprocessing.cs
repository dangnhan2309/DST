using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp1
{
    public class TextPreprocessing
    {
        private static List<string> stopWords = new List<string> { "và", "hoặc", "là", "để", "của", "theo" }; // Danh sách từ không quan trọng

        // Tokenization: Tách câu thành các từ
        public static List<string> Tokenize(string sentence)
        {
            return sentence.Split(new char[] { ' ', '.', ',', ';', '!', '?' }, StringSplitOptions.RemoveEmptyEntries)
                           .Select(word => word.ToLower())
                           .Where(word => !stopWords.Contains(word))  // Loại bỏ từ không quan trọng
                           .ToList();
        }
    }
}
