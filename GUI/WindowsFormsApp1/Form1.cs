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
using System.Diagnostics;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        List<String> units_added = new List<String>();
        List<Button> all_buttons = new List<Button>();
        List<List<int>> friends_list_data = new List<List<int>>();
        List<String> friends_names = new List<string>();
        List<String> friends_subjects = new List<string>();
        List<int> list_times = new List<int>();
        List<lesson> lesson_output = new List<lesson>();
        bool outputMode = false;
        public Form1()
        {
            InitializeComponent();
            all_buttons = new List<Button>() { button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40, button41, button42, button43, button44, button45, button46, button47, button48, button49, button50, button51, button52, button53, button54, button55, button56, button57, button58, button59, button60, button61, button62, button63, button64, button65 };
            friends_list_data = new List<List<int>>();
            friends_names = new List<string>();
            friends_subjects = new List<string>();
            label16.Hide();
            listBox3.Hide();
            label17.Hide();
        }
        private void button_Click(object sender, EventArgs e)
        {
            Button b = (Button)sender; 
            if (outputMode == false)
            {
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
            else
            {
                if (b.Tag != null)
                {
                    var temp = lesson_output[Int16.Parse(b.Tag.ToString())];
                    listBox3.Items.Clear();
                    String name_to_add = "";
                    if (temp.classname.Substring(0, 1) == "W")
                    {
                        name_to_add += "Workshop ";
                    }
                    else if (temp.classname.Substring(0, 1) == "L")
                    {
                        name_to_add += "Lecture ";
                    }
                    else
                    {
                        name_to_add += "Tutorial ";
                    }
                    name_to_add += temp.classname.Substring(1);
                    listBox3.Items.Add(name_to_add);
                    listBox3.Items.Add("Available:");
                    for (int i = 0; i < temp.available.Count; i++)
                    {
                        listBox3.Items.Add(temp.available[i]);
                    }
                    listBox3.Items.Add("Not preferred:");
                    for (int i = 0; i < temp.not_preferred.Count; i++)
                    {
                        listBox3.Items.Add(temp.not_preferred[i]);
                    }
                    listBox3.Items.Add("Unavailable:");
                    for (int i = 0; i < temp.unavailable.Count; i++)
                    {
                        listBox3.Items.Add(temp.unavailable[i]);
                    }
                }
            }
        }

        private void button66_Click(object sender, EventArgs e)
        {
            if (comboBox1.SelectedItem != null && outputMode == false)
            {
                listBox1.Items.Add(comboBox1.Text);
                comboBox1.Text = "";
            }
        }

        private void button67_Click(object sender, EventArgs e)
        {
            if (outputMode == false)
            {
                listBox1.Items.Remove(listBox1.SelectedItem);
            }
        }

        private void button68_Click(object sender, EventArgs e)
        {
            if (outputMode == false)
            {
                var csv = new StringBuilder();
                for (int i = 0; i < friends_names.Count; i++)
                {
                    csv.Append(friends_names[i] + "," + friends_subjects[i] + "\n");
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
                    File.WriteAllText(@"A:\Documents\DLCT\teststudent.csv", csv.ToString());
                }
                run_cmd();
            }
        }

        private void button73_Click(object sender, EventArgs e)
        {
            if (outputMode == false)
            {
                int index_name = friends_names.FindIndex(a => a.Contains(listBox2.SelectedItem.ToString()));
                if (index_name >= 0 && index_name < friends_names.Count)
                friends_list_data.RemoveAt(index_name);
                friends_subjects.RemoveAt(index_name);
                friends_names.RemoveAt(index_name);
                listBox2.Items.Remove(listBox2.SelectedItem);
            }
        }

        private void button_output(object sender, EventArgs e)
        {
            for (int i = 0; i < all_buttons.Count; i++)
            {
                all_buttons[i].BackColor = Color.White;
            }

            var lines = File.ReadLines(@"A:\Documents\DLCT\test1.csv");
            foreach (string line in lines)
            {
                var sub_array = line.Split(',');
                var local_temp = new lesson();
                local_temp.classname = sub_array[0];
                local_temp.day = sub_array[1];
                local_temp.startTime = sub_array[2];
                local_temp.endTime = sub_array[3];
                local_temp.available = new List<string>();
                local_temp.not_preferred = new List<string>();
                local_temp.unavailable = new List<string>();
                List<String> is_Available = new List<string>();
                List<String> is_not_preferred = new List<string>();
                List<String> is_unavailable = new List<string>();

                var counter = 4;
                while ((counter <= sub_array.Count() - 1) && sub_array[counter] != "~".ToString())
                {
                    is_Available.Add(sub_array[counter]);
                    counter += 1;
                }
                counter += 1;
                while ((counter <= sub_array.Count() - 1) && sub_array[counter] != "~".ToString())
                {
                    is_not_preferred.Add(sub_array[counter]);
                    counter += 1;
                }
                counter += 1;
                while ((counter <= sub_array.Count() - 1) && sub_array[counter] != "~".ToString())
                {
                    is_unavailable.Add(sub_array[counter]);
                    counter += 1;
                }

                if (is_Available.Count > 0)
                {
                    for (int i = 0; i < is_Available.Count; i++)
                    {
                        local_temp.available.Add(is_Available[i]);
                    }
                    
                }
                if (is_not_preferred.Count > 0)
                {
                    for (int i = 0; i < is_not_preferred.Count; i++)
                    {
                        local_temp.not_preferred.Add(is_not_preferred[i]);
                    }

                }
                if (is_unavailable.Count > 0)
                {
                    for (int i = 0; i < is_unavailable.Count; i++)
                    {
                        local_temp.unavailable.Add(is_unavailable[i]);
                    }

                }
                lesson_output.Add(local_temp);
            }
            String[] button_number = new String[lesson_output.Count];
            int[] day_no = new int[lesson_output.Count];
            for (int i = 0; i < lesson_output.Count; i++)
            {
                button_number[i] = lesson_output[i].startTime;
                day_no[i] = day(lesson_output[i].day);
                all_buttons[Int16.Parse(lesson_output[i].startTime) * 5 - 40 + day(lesson_output[i].day)].BackColor = Color.Green;
                all_buttons[Int16.Parse(lesson_output[i].startTime) * 5 - 40 + day(lesson_output[i].day)].Tag = i;
            }
            outputMode = true;
            hide_on_output();
        }


        private void hide_on_output()
        {
            if (outputMode == true)
            {
                label19.Hide();
                label12.Hide();
                label16.Hide();
                label15.Hide();
                label14.Hide();
                button73.Hide();
                button66.Hide();
                button67.Hide();
                button68.Hide();
                textBox1.Hide();
                comboBox1.Hide();
                listBox1.Hide();
                listBox2.Hide();
                listBox3.Show();
                label17.Show();
                listBox3.Items.Clear();
            }
            else
            {
                label19.Show();
                label12.Show();
                label15.Show();
                label14.Show();
                button73.Show();
                button66.Show();
                button67.Show();
                button68.Show();
                textBox1.Show();
                comboBox1.Show();
                listBox1.Show();
                listBox2.Show();
                listBox3.Hide();
                label17.Hide();
            }
        }


        private void run_cmd()
        {
            String fileName = AddQuotesIfRequired(@"A:\Documents\DLCT\input.py");

            Process p = new Process();
            p.StartInfo = new ProcessStartInfo(@"C:\Users\Allan Chan\AppData\Local\Programs\Python\Python38-32\python.exe", fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();

            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();

            Console.WriteLine(output);

            Console.ReadLine();
        }

        public string AddQuotesIfRequired(string path)
        {
            return !string.IsNullOrWhiteSpace(path) ?
                path.Contains(" ") && (!path.StartsWith("\"") && !path.EndsWith("\"")) ?
                    "\"" + path + "\"" : path :
                    string.Empty;
        }

        private void button_submit_Click(object sender, EventArgs e)
        {
            if (outputMode == false)
            {
                if (textBox1.Text == "")
                {
                    label16.Text = "Please enter a name";
                    label16.Show();
                }
                else
                {
                    if (listBox1.Items.Count > 0)
                    {
                        label16.Hide();
                        list_times = new List<int>();
                        friends_names.Add(textBox1.Text);
                        foreach (var item in listBox1.Items)
                        {
                            friends_subjects.Add(item.ToString());
                            break;
                        }
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
                    else
                    {
                        label16.Text = "Please enter a unit";
                        label16.Show();
                    }
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

        private int day(String a)
        {
            if (a == "Mon")
            {
                return 0;
            }
            else if (a == "Tue")
            {
                return 1;
            }
            else if (a == "Wed")
            {
                return 2;
            }
            else if (a == "Thu")
            {
                return 3;
            }
            else
            {
                return 4;
            }
        }

        private void button69_Click(object sender, EventArgs e)
        {
            outputMode = false;
            hide_on_output();
            for (int i = 0; i < all_buttons.Count; i++)
            {
                all_buttons[i].Tag = null;
                all_buttons[i].BackColor = Color.White;
            }
        }
    }
}
