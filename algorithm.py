import input


def algorithm(classes):
    number_of_students = len(classes[0][3]) + len(classes[0][4]) + len(classes[0][5])
    good_classes = []
    unavailable = []
    unavail_final = []
    for i in range(len(classes)):

        # Situation 1 Irrespective of preferences
        if len(classes[i][3]) == number_of_students:
            good_classes.append(classes[i])

        # Situation 3 Only One student is available for a class
        if len(classes[i][3]) == 1:
            print("Cannot be done, not enough friends! :(")

        # Situation 4 Most preferred class
        preferred_no = max(len(classes[i][3]))
        for j in range(len(classes)):
            if preferred_no == len(classes[i][3]):
                good_classes.append(classes[i])

        # Situation 5 If a student is unavailable for everything
        if classes[i][5] is not None:
            unavailable.extend(classes[i][5])
        student = input.lesson1.names_list
        for j in range(len(student)):
            if unavailable.count(student[j]) == len(classes):
                unavail_final.append(student[j])  # Students who can't do anything

        # Splitting groups
        combos = [[]]
        for item in student:
            new_combos = [subset + [item] for subset in combos]
            combos.extend(new_combos)





# available, not preferred, unavailable
classes1 = [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []]]


# currently = [[w1 1], [w1 2], [t1], [t2], [l1], [w2 1]]
# maybe???? = [[#w1 [w1 1], [w1 2], [w1 3]], [[#w2 [w2 1], [w2 2], [w2 3]], [#l1 [l1]]]
# class.workshop1 == [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []], ['W2', 'Mon', '6 - 7', ['Bob', 'John'], [], []]]
# [['W1', 'Mon', '8 - 9', [names of students who are available], [names of students who do not prefer it], [names of students who are UNavailable]]]