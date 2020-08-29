using System;
using System.CodeDom;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Windows.Forms;
using CsvHelper;
using CsvHelper.Configuration;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        List<String> units_added = new List<String>();
        List<Button> all_buttons = new List<Button>();
        List<List<int>> friends_list_data = new List<List<int>>();
        List<String> friends_names = new List<string>();
        List<int> list_times = new List<int>();
        public Form1()
        {
            InitializeComponent();
            all_buttons = new List<Button>() { button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40, button41, button42, button43, button44, button45, button46, button47, button48, button49, button50, button51, button52, button53, button54, button55, button56, button57, button58, button59, button60, button61, button62, button63, button64, button65 };
            friends_list_data = new List<List<int>>();
            friends_names = new List<string>();
        }
        private void time_Click(object sender, EventArgs e)
        {
            PictureBox pic = (PictureBox)sender;
            if (pic.BackColor == Color.Aqua)
            {
                pic.BackColor = Color.White;
            }
            else
            {
                pic.BackColor = Color.Aqua;
            }
        }

        private void button_Click(object sender, EventArgs e)
        {
            Button b = (Button)sender;
            if (b.BackColor == Color.White)
            {
                b.BackColor = Color.Yellow;
            }
            else if (b.BackColor == Color.Yellow)
            {
                b.BackColor = Color.Red;
            }
            else
            {
                b.BackColor = Color.White;
            }
            label1.Focus();
        }

        private void button66_Click(object sender, EventArgs e)
        {
            if (comboBox1.SelectedItem != null)
            {
                listBox1.Items.Add(comboBox1.Text);
                comboBox1.Text = "";
            }
        }

        private void button67_Click(object sender, EventArgs e)
        {
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void button68_Click(object sender, EventArgs e)
        {
            var csv = new StringBuilder();
            for (int i = 0; i < friends_names.Count; i++)
            {
                csv.Append(friends_names[i] + "\n");
                var data = "";
                for (int j = 0; j < 65; j++)
                {
                    if (j % 5 == 4)
                    {
                        data += friends_list_data[i][j] + "\n";
                    }
                    else
                    {
                        data += friends_list_data[i][j] + ",";
                    }
                }
                csv.Append(data);
                File.WriteAllText("C:\\Users\\Allan Chan\\source\\repos\\GUI\\WindowsFormsApp1\\test.csv", csv.ToString());
            }
            
            // save to CSV file
        }

        private void button73_Click(object sender, EventArgs e)
        {
            listBox2.Items.Remove(listBox2.SelectedItem);
        }

        private void button74_Click(object sender, EventArgs e)
        {
            // output data
        }

        private void button_submit_Click(object sender, EventArgs e)
        {
            if (listBox1.Items.Count > 0)
            {
                list_times = new List<int>();
                friends_names.Add(textBox1.Text);
                for (int i = 0; i < all_buttons.Count; i++)
                {
                    list_times.Add(button_value(all_buttons[i]));
                }
                friends_list_data.Add(list_times);
                listBox2.Items.Add(textBox1.Text);
                textBox1.Text = "";
                listBox1.Items.Clear();
                for (int i = 0; i < all_buttons.Count; i++)
                {
                    all_buttons[i].BackColor = Color.White;
                }
            }
        }

        private int button_value(Button a)
        {
            if (a.BackColor == Color.White)
            {
                return 2;
            }
            else if (a.BackColor == Color.Yellow)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
    }
}
