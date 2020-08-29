import input

def class_design(student_names, student_avail, class_times):
    times = ['8  9', '9  10', '10  11', '11  12', '12  13', '13  14', '14  15', '']
    all_classes = []
    single_class = []
    for instance in class_times:
        single_class.append(instance[0])
        single_class.append(instance[1])
        single_class.append(instance[2])


