import input, lesson

def algorithm(classes):
    number_of_students = len(classes[0][3]) + len(classes[0][4]) + len(classes[0][5])
    good_classes = []
    unavailable = []
    unavail_final = []

    #good_classes_limit
    if len(classes) <= 4:
        good_classes_limit = 4
    else:
        good_classes_limit = max(len(classes)//2, 4)

    # Looking at all classes that everyone can do and ranking based on how many don't not prefer it
    ranking = []
    potential_good_classes = []
    for i in range(len(classes)):
        if len(classes[i][5]) > 0:
            continue
        else:
            ranking_score = 0
            ranking_score += len(classes[i][4])* 0.75
            ranking_score += len(classes[i][5])
            # ranking_score + 0.0(i)
            potential_good_classes.append(ranking_score + i * 0.001)

    if len(potential_good_classes) <= good_classes_limit:
        for i in range(len(potential_good_classes)):
            good_classes.append(potential_good_classes[1])
    else:
        potential_good_classes.sort()
        for i in range(good_classes_limit):
            if potential_good_classes[i] > 10:
                index = int(str(potential_good_classes[i])[5])
            else:
                index = int(str(potential_good_classes[i])[4])
            good_classes.append(potential_good_classes[index])

    if len(good_classes) >= good_classes_limit:
        return good_classes


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