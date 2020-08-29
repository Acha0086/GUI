import string, algorithm, lesson


def class_input(Units, Unit_name):
    # Input is csv file of units (see 'class input.csv' for example), and the name of the unit the student wants
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
    # Units saved as [[Class name(WS1 1), day, time], [Class name (WS2 1), day, time]]
    return full_class_list


def student_input(Students):
    # Input csv file in the format of the example 'test student.csv'
    student_table = []
    single_student_hour = []
    single_student_table = []
    student_names = []
    file = open(str(Students), "r", encoding="UTF-8-sig")

    for line in file:
        line = line.split(',')
        for word in line:
            try:
                int(word)
            except ValueError:
                if len(single_student_table) > 0:
                    student_table.append(single_student_table)
                    single_student_table = []
                student_names.append(word)

                break

            single_student_hour.append(word.strip())
        if len(single_student_hour) == 5:
            single_student_table.append(single_student_hour)
            single_student_hour = []
    student_table.append(single_student_table)
    file.close()
    # None = Available, 1 = Unavailable, 2 = Not preferred
    # Outputs in format of (list of student names, [[[student 1 availibilities 8-9], [student 1 availabilies 9-10]], [[student 2 availabilities 8-9],[student 2 availabilities 9-10]])
    return student_names, student_table


if __name__ == '__main__':
    class_table = class_input('Class input.csv', 'FIT2014')
    print(class_table)
    student_table = student_input('test student.csv')
    print(student_table)
    lesson1 = lesson.Lessons(class_table, student_table)
    lesson1.set_up()
    lesson1.workshop()
    print(lesson1.workshop_list_final)
    lesson1.availability('Tue', '13  14')
    print(lesson1.workshop_list_final)




