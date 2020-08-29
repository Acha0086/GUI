
# students saved as (student_name, list of lists)
def input(Student, Units, Unit_name):
    # Units saved as [[Class name(WS1 1), day, time], [Class name (WS2 1), day, time]]
    row_num = 0
    file = open(str(Units), "r", encoding="UTF-8-sig")
    for line in file:
        line = line.split(',')
        print(line)
        if line[0] != str(Unit_name):
            row_num += 1
        else:
            break
    print(line)
    skip_line = 0
    full_class_list = []
    single_class_list = []
    single_class_list_counter = 0
    for word in line:
        if skip_line == 0:
            skip_line += 1
            continue
        while word != '':
            if single_class_list_counter == 3:
                full_class_list.append(single_class_list)
                single_class_list_counter = 0
            single_class_list.append(word)
            single_class_list_counter += 1
    full_class_list.append(single_class_list)



input('asda', 'Class input.csv', 'FIT2014')





