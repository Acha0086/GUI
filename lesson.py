import input


class Lessons:

    def __init__(self, class_table, student_table):
        self.class_table = class_table
        self.number_of_students = len(student_table[0])
        self.workshop_list = []
        self.tutorial_list = []
        self.lecture_list = []
        self.names_list = student_table[0]
        self.input_availability = student_table[1]

    def set_up(self):
        self.__workshop_setup()
        self.__tutorial_setup()
        self.__lecture_setup()

    def __workshop_setup(self):
        for i in range(len(self.class_table)):
            if self.class_table[i][0][0] == 'W':
                self.workshop_list.append(self.class_table[i])

    def __tutorial_setup(self):
        for i in range(len(self.class_table)):
            if self.class_table[i][0][0] == 'T':
                self.tutorial_list.append(self.class_table[i])

    def __lecture_setup(self):
        for i in range(len(self.class_table)):
            if self.class_table[i][0][0] == 'L':
                self.lecture_list.append(self.class_table[i])

    def workshop(self):
        for i in range(len(self.workshop_list)):
            pass





def class_design(student_names, student_avail, class_times):
    times = ['8  9', '9  10', '10  11', '11  12', '12  13', '13  14', '14  15', '']
    all_classes = []
    single_class = []
    for instance in class_times:
        single_class.append(instance[0])
        single_class.append(instance[1])
        single_class.append(instance[2])


