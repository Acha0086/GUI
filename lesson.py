import input, re


class Lessons:

    def __init__(self, class_table, student_table):
        self.class_table = class_table
        self.number_of_students = len(student_table[0])
        self.workshop_list_setup = []
        self.tutorial_list_setup = []
        self.lecture_list_setup = []
        self.names_list = student_table[0]
        self.input_availability = student_table[1]
        self.workshop_list_final = []
        self.tutorial_list_final = []
        self.lecture_list_final = []

    def set_up(self):
        self.__workshop_setup()
        self.__tutorial_setup()
        self.__lecture_setup()

    def __workshop_setup(self):
        for i in range(len(self.class_table)):
            if self.class_table[i][0][0] == 'W':
                self.workshop_list_setup.append(self.class_table[i])

    def __tutorial_setup(self):
        for i in range(len(self.class_table)):
            if self.class_table[i][0][0] == 'T':
                self.tutorial_list_setup.append(self.class_table[i])

    def __lecture_setup(self):
        for i in range(len(self.class_table)):
            if self.class_table[i][0][0] == 'L':
                self.lecture_list_setup.append(self.class_table[i])

    # [class_type/name/number, day, times, [available students], [unavailable students], [students who don’t prefer it]]
    def workshop(self):
        for i in range(len(self.workshop_list_setup)):
            single_w = []
            single_w.append(self.workshop_list_setup[i][0])
            single_w.append(self.workshop_list_setup[i][1])
            time = re.findall(r'([0-9][0-9]?)[ ]*([0-9][0-9]?)', self.workshop_list_setup[i][2])
            single_w.append(time[0])
            single_w.append([])
            single_w.append([])
            single_w.append([])
            self.workshop_list_final.append(single_w)

    def availability(self, day, time):
        """
        Time should be in a tuple (start, end)
        """
        # gets the column
        if day == 'Mon':
            column = 0
        elif day == 'Tue':
            column = 1
        elif day == 'Wed':
            column = 2
        elif day == 'Thu':
            column = 3
        elif day == 'Fri':
            column = 4

        # gets the row
        rows = []
        start_time = time[0]
        end_time = time[1]
        number_of_rows = int(end_time) - int(start_time)
        for i in range(number_of_rows):
            rows.append(int(start_time) - 8 + i)
        row = int(start_time)-8
        for i in range(len(self.input_availability)):
            name = self.names_list[i]
            if self.input_availability[i][row][column] == 0:
                self.workshop_list_final[i].append(name)
                print(name)
            elif self.input_availability[i][row][column] == 1:
                self.workshop_list_final[i].append(name)
            else:
                self.workshop_list_final[i].append(name)
        






