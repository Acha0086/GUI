import input


def algorithm(classes):
    number_of_students = len(classes[0][3]) + len(classes[0][4]) + len(classes[0][5])
    good_classes = []
    unavailable = []
    for i in range(len(classes)):

        # Situation 1
        if len(classes[i][3]) == number_of_students:
            good_classes.append(classes[i])

        # Situation 3
        if len(classes[i][3]) > number_of_students:
            return False

        # Situation 4
        preferred_no = max(len(classes[i][3]))
        for j in range(len(classes)):
            if preferred_no == len(classes[i][3]):
                good_classes.append(classes[i])

        # Situation 5
        unavail_final = []
        if classes[i][5] is not None:
            unavailable.extend(classes[i][5])
        unavailable.sort()
        student = input.lesson1.names_list
        for i in range(len(student)):
            if unavailable.count(student[i]) == len(classes):
                unavail_final.append(student[i])  # Students who can't do anything

        # Splitting groups




# available, not preferred, unavailable
classes1 = [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []]]


# currently = [[w1 1], [w1 2], [t1], [t2], [l1], [w2 1]]
# maybe???? = [[#w1 [w1 1], [w1 2], [w1 3]], [[#w2 [w2 1], [w2 2], [w2 3]], [#l1 [l1]]]
# class.workshop1 == [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []], ['W2', 'Mon', '6 - 7', ['Bob', 'John'], [], []]]
# [['W1', 'Mon', '8 - 9', [names of students who are available], [names of students who do not prefer it], [names of students who are UNavailable]]]