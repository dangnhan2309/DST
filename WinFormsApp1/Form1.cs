using System;
using System.Collections.Generic;
using System.Windows.Forms;
using OpenAI;
using Newtonsoft.Json;
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Text.RegularExpressions;
using static System.Net.Mime.MediaTypeNames;
namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        private List<Particle> particles;

        //private const string apiKey =
        //    "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"; // Thay YOUR_API_KEY bằng API Key của bạn

        public Form1()
        {
            InitializeComponent();

            // Tạo danh sách yêu cầu thuê drone
            List<string> yêuCầuThuêDrone = new List<string>
            {
                "Thuê drone để chiếu chuỗi chữ 'Grand Opening' trong 5 phút trên không trung với độ lớn 15m.",
                "Thuê drone để chiếu khẩu hiệu 'Together We Achieve' trong 3 phút trên không trung với độ lớn 12m.",
                "Thuê drone để chiếu đồng hồ đếm ngược từ '10' đến '1' trong 5 phút trên không trung với độ lớn 10m.",
                "Thuê drone để chiếu số '2025' trong 2 phút trên không trung với độ lớn 20m.",
                "Thuê drone để chiếu chuỗi chữ 'Charity Event - 1000 Attendees' trong 4 phút trên không trung với độ lớn 18m."

            };

            // Gán danh sách vào ComboBox
            combobox_request.DataSource = yêuCầuThuêDrone;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Thêm mã khởi tạo nếu cần khi Form được tải
        }


        //public async Task<string> GetChatGPTResponse(string prompt)
        //{
        //    using (var client = new HttpClient())
        //    {
        //        client.DefaultRequestHeaders.Add("Authorization", "Bearer " + apiKey);

        //        var requestData = new
        //        {
        //            model = "gpt-3.5-turbo", // Hoặc GPT-4 tùy theo yêu cầu của bạn
        //            messages = new[]
        //            {
        //        new { role = "system", content = "You are a helpful assistant." },
        //        new { role = "user", content = prompt }
        //    },
        //            max_tokens = 150
        //        };

        //        string jsonRequest = JsonConvert.SerializeObject(requestData);
        //        var content = new StringContent(jsonRequest, Encoding.UTF8, "application/json");

        //        HttpResponseMessage response = await client.PostAsync("https://api.openai.com/v1/chat/completions", content);

        //        if (response.StatusCode == System.Net.HttpStatusCode.TooManyRequests)
        //        {
        //            // Nếu gặp lỗi "Too Many Requests", kiểm tra tiêu đề Retry-After
        //            var retryAfter = response.Headers.RetryAfter?.Delta?.TotalSeconds ?? 10;
        //            MessageBox.Show($"Too many requests. Please wait {retryAfter} seconds before trying again.");
        //            await Task.Delay(TimeSpan.FromSeconds(retryAfter)); // Chờ lại một khoảng thời gian
        //            return await GetChatGPTResponse(prompt); // Thử lại yêu cầu sau khi chờ
        //        }

        //        if (response.IsSuccessStatusCode)
        //        {
        //            string jsonResponse = await response.Content.ReadAsStringAsync();
        //            var responseObj = JsonConvert.DeserializeObject<dynamic>(jsonResponse);
        //            return responseObj.choices[0].message.content;
        //        }
        //        else
        //        {
        //            throw new Exception("API call failed: " + response.StatusCode);
        //        }
        //    }
        //}


        private void phantichButton_Click(object sender, EventArgs e)
        {
            string sentence = combobox_request.Text;
            //txt_Shape.Text = ExtractValue(sentence, @"chuỗi chữ '([^']+)'");
            //// Extract txt_độ lớn
            //txt_dolon.Text = ExtractValue(sentence, @"độ lớn (\d+)");
            //// Extract txt_thời gian2
            //txt_time.Text = ExtractValue(sentence, @"trong (\d+)");
            var match = Regex.Match(sentence, @"'([^']+)' trong (\d+) phút trên không trung với độ lớn (\d+)m.");
            if (match.Success)
            {
                txt_Shape.Text = match.Groups[1].Value;
                txt_time.Text = match.Groups[2].Value;
                txt_dolon.Text = match.Groups[3].Value;
            }
            double droneArea = 1;
            double timeFactor = 1;
            double shapeAere = double.Parse(txt_dolon.Text);
            if (int.Parse(txt_time.Text) > 20)
            {
                droneArea = int.Parse(txt_time.Text) / 20;
            }


            txt_soluongdrone.Text = Math.Ceiling((shapeAere / droneArea) * timeFactor).ToString();
        }
        static string ExtractValue(string text, string pattern)
        {
            Match match = Regex.Match(text, pattern);
            return match.Success ? match.Groups[1].Value : "Not Found";
        }
        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Tao3Dbutton_Click(object sender, EventArgs e)
        {
            // Get the text from the txt_shape TextBox
            string shapeText = txt_Shape.Text;

            // Ensure text is not empty before opening the OpenTK window
            if (string.IsNullOrEmpty(shapeText))
            {
                MessageBox.Show("Please enter a shape or text.");
                return;
            }

            // Create and show the OpenTK window with the entered shape
            using (var openTKWindow = new OpenTKWindow(800, 600, shapeText))
            {
                openTKWindow.Run(60.0);  // Run the window with 60 FPS
            }
        }


        //{
        //    try
        //    {
        //        // Tạo prompt theo định dạng yêu cầu
        //        string prompt = "Tóm gọn và chỉ đưa ra các chỉ số, theo format \"{hình dạng},{độ lớn},{thời gian},{số lượng drone cần thiết}\"; yêu cầu là: " + combobox_request.Text;
        //        txt_Shape.Text = combobox_request.Text;
        //        // Thực hiện phân tích và trả về kết quả từ API
        //        string result = await GetChatGPTResponse(prompt);

        //        // Hiển thị kết quả trả về trong RichTextBox
        //        richTextBox1.Text = result;
        //    }
        //    catch (Exception ex)
        //    {
        //        MessageBox.Show("Error: " + ex.Message);
        //    }
        //}
    }

}
