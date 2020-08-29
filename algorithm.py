import input


def algorithm(classes):
    number_of_students = len(classes[0][3]) + len(classes[0][4]) + len(classes[0][5])
    good_classes = []
    for i in range(len(classes)):

        # Situation 1
        if len(classes[i][3]) == number_of_students:
            good_classes.append(classes[i])

        # Situation 3





# available, not preferred, unavailable
classes1 = [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []]]


# currently = [[w1 1], [w1 2], [t1], [t2], [l1], [w2 1]]
# maybe???? = [[#w1 [w1 1], [w1 2], [w1 3]], [[#w2 [w2 1], [w2 2], [w2 3]], [#l1 [l1]]]