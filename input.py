import string


# students saved as (student_name, list of lists)
def input(Students, Units, Unit_name):
    # Units saved as [[Class name(WS1 1), day, time], [Class name (WS2 1), day, time]]
    row_num = 0
    file = open(str(Units), "r", encoding="UTF-8-sig")
    for line in file:
        line = line.split(',')
        if line[0] != str(Unit_name):
            row_num += 1
        else:
            break
    skip_line = 0
    full_class_list = []
    single_class_list = []
    single_class_list_counter = 0
    for word in line:
        if word == '':
            break
        if skip_line == 0:
            skip_line += 1
            continue
        if single_class_list_counter == 3:
            full_class_list.append(single_class_list)
            single_class_list_counter = 0
            single_class_list = []
        # strips punctuation and \n
        single_class_list.append(word.translate(str.maketrans('', '', string.punctuation)).strip())
        single_class_list_counter += 1
    full_class_list.append(single_class_list)
    file.close()

    # turn student input into python readable list of lists
    student_table = []
    for i in range(13):
        student_table.append([])
    file = open(str(Students), "r", encoding="UTF-8-sig")
    line_num = -1
    for line in file:
        line_num += 1
        line = line.split(',')
        for word in line:
            if word != '':
                try:
                    int(word)
                except ValueError:
                    # run new function


            if word == '':
                student_table[line_num].append(None)
            else:
                student_table[line_num].append(word.strip())
    return student_table


print(input('test student.csv', 'Class input.csv', 'FIT2014'))





