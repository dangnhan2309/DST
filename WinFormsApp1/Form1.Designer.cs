namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            Tao3Dbutton = new Button();
            phantichButton = new Button();
            richTextBox1 = new RichTextBox();
            label3 = new Label();
            txt_Shape = new TextBox();
            labledolon = new Label();
            txt_dolon = new TextBox();
            labeltime = new Label();
            txt_time = new TextBox();
            label = new Label();
            txt_soluongdrone = new TextBox();
            combobox_request = new ComboBox();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(57, 123);
            label1.Name = "label1";
            label1.Size = new Size(62, 20);
            label1.TabIndex = 0;
            label1.Text = "Request";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI", 16.2F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label2.Location = new Point(118, 26);
            label2.Name = "label2";
            label2.Size = new Size(492, 38);
            label2.TabIndex = 0;
            label2.Text = "Generate 3D shape partical as drone";
            // 
            // Tao3Dbutton
            // 
            Tao3Dbutton.Location = new Point(251, 285);
            Tao3Dbutton.Name = "Tao3Dbutton";
            Tao3Dbutton.Size = new Size(144, 117);
            Tao3Dbutton.TabIndex = 2;
            Tao3Dbutton.Text = "Tao";
            Tao3Dbutton.UseVisualStyleBackColor = true;
            Tao3Dbutton.Click += Tao3Dbutton_Click;
            // 
            // phantichButton
            // 
            phantichButton.Location = new Point(12, 156);
            phantichButton.Name = "phantichButton";
            phantichButton.Size = new Size(128, 120);
            phantichButton.TabIndex = 3;
            phantichButton.Text = "Phan tich";
            phantichButton.UseVisualStyleBackColor = true;
            phantichButton.Click += phantichButton_Click;
            // 
            // richTextBox1
            // 
            richTextBox1.Location = new Point(158, 156);
            richTextBox1.Name = "richTextBox1";
            richTextBox1.Size = new Size(249, 120);
            richTextBox1.TabIndex = 4;
            richTextBox1.Text = "";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(430, 116);
            label3.Name = "label3";
            label3.Size = new Size(50, 20);
            label3.TabIndex = 0;
            label3.Text = "Shape";
            // 
            // txt_Shape
            // 
            txt_Shape.Location = new Point(531, 116);
            txt_Shape.Name = "txt_Shape";
            txt_Shape.Size = new Size(125, 27);
            txt_Shape.TabIndex = 1;
            // 
            // labledolon
            // 
            labledolon.AutoSize = true;
            labledolon.Location = new Point(430, 186);
            labledolon.Name = "labledolon";
            labledolon.Size = new Size(57, 20);
            labledolon.TabIndex = 0;
            labledolon.Text = "Độ Lớn";
            // 
            // txt_dolon
            // 
            txt_dolon.Location = new Point(531, 186);
            txt_dolon.Name = "txt_dolon";
            txt_dolon.Size = new Size(125, 27);
            txt_dolon.TabIndex = 1;
            // 
            // labeltime
            // 
            labeltime.AutoSize = true;
            labeltime.Location = new Point(430, 259);
            labeltime.Name = "labeltime";
            labeltime.Size = new Size(115, 20);
            labeltime.TabIndex = 0;
            labeltime.Text = "Thoi gian (phut)";
            // 
            // txt_time
            // 
            txt_time.Location = new Point(531, 259);
            txt_time.Name = "txt_time";
            txt_time.Size = new Size(125, 27);
            txt_time.TabIndex = 1;
            // 
            // label
            // 
            label.AutoSize = true;
            label.Location = new Point(430, 330);
            label.Name = "label";
            label.Size = new Size(111, 20);
            label.TabIndex = 0;
            label.Text = "So luong drone";
            // 
            // txt_soluongdrone
            // 
            txt_soluongdrone.Location = new Point(531, 330);
            txt_soluongdrone.Name = "txt_soluongdrone";
            txt_soluongdrone.Size = new Size(125, 27);
            txt_soluongdrone.TabIndex = 1;
            // 
            // combobox_request
            // 
            combobox_request.FormattingEnabled = true;
            combobox_request.Location = new Point(145, 122);
            combobox_request.Name = "combobox_request";
            combobox_request.Size = new Size(151, 28);
            combobox_request.TabIndex = 5;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(788, 450);
            Controls.Add(combobox_request);
            Controls.Add(richTextBox1);
            Controls.Add(phantichButton);
            Controls.Add(Tao3Dbutton);
            Controls.Add(txt_soluongdrone);
            Controls.Add(txt_time);
            Controls.Add(label);
            Controls.Add(txt_dolon);
            Controls.Add(labeltime);
            Controls.Add(txt_Shape);
            Controls.Add(labledolon);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Button Tao3Dbutton;
        private Button phantichButton;
        private RichTextBox richTextBox1;
        private Label label3;
        private TextBox txt_Shape;
        private Label labledolon;
        private TextBox txt_dolon;
        private Label labeltime;
        private TextBox txt_time;
        private Label label;
        private TextBox txt_soluongdrone;
        private ComboBox combobox_request;
    }
}
