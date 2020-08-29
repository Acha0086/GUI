

def algorithm(classes):
    good_classes = []

    #good_classes_limit
    if len(classes) <= 4:
        good_classes_limit = 4
    else:
        good_classes_limit = max(len(classes)//2, 4)

    # Looking at all classes that everyone can do and ranking based on how many don't not prefer it
    potential_good_classes = []
    for i in range(len(classes)):
        if len(classes[i][5]) > 0:
            continue
        else:
            ranking_score = 0
            ranking_score += len(classes[i][4]) * 0.75
            ranking_score += len(classes[i][3])
            # ranking_score + 0.00(i)
            potential_good_classes.append(ranking_score + (i+1) * 0.001)

    if len(potential_good_classes) <= good_classes_limit:
        for i in range(len(potential_good_classes)):
            if potential_good_classes[i] > 10:
                index = int(str(potential_good_classes[i])[5])-1
            else:
                index = int(str(potential_good_classes[i])[4])-1
            good_classes.append(classes[index])
    else:
        potential_good_classes.sort()
        for i in range(good_classes_limit):
            if potential_good_classes[i] > 10:
                index = int(str(potential_good_classes[i])[5])-1
            else:
                index = int(str(potential_good_classes[i])[4])-1
            good_classes.append(classes[index])

    if len(good_classes) >= good_classes_limit:
        return good_classes

    # not everyone is in the class
    potential_alright_classes = []
    for i in range(len(classes)):
        if len(classes[i][3]) == 0:
            continue
        else:
            ranking_score = 0
            ranking_score += len(classes[i][4]) * 0.75
            ranking_score += len(classes[i][3])
            # ranking_score + 0.00(i)
            potential_alright_classes.append(ranking_score + (i+1) * 0.001)

    if len(potential_alright_classes) <= (good_classes_limit - len(good_classes)):
        for i in range(len(potential_alright_classes)):
            if potential_alright_classes[i] > 10:
                index = int(str(potential_alright_classes[i])[5])-1
            else:
                index = int(str(potential_alright_classes[i])[4])-1
            good_classes.append(classes[index])
    else:
        potential_alright_classes.sort()
        for i in range(good_classes_limit - len(good_classes)):
            if potential_alright_classes[i] > 10:
                index = int(str(potential_alright_classes[i])[5])-1
            else:
                index = int(str(potential_alright_classes[i])[4])-1
            good_classes.append(classes[index])

    return good_classes

print(algorithm([['T 1', 'Fri', ['16', '17'], ['Sue'], ['Bob', 'John'], ['Joe']], ['T 2', 'Tue', ['16', '17'], ['Sue'], ['Bob', 'John'], ['Joe']], ['T 3', 'Mon', ['12', '13'], ['Bob', 'Joe'], ['John'], ['Sue']]]))
#print(algorithm([['L1', 'Wed', ['8', '9'], ['Sue'], ['Joe'], ['Bob', 'John']], ['L2', 'Thu', ['19', '20'], ['Sue'], [], ['Bob', 'Joe', 'John']]]))



    # Splitting groups
#    combos = [[]]
#    for item in student:
#        new_combos = [subset + [item] for subset in combos]
#        combos.extend(new_combos)

# Situation 5 If a student is unavailable for everything
#    if classes[i][5] is not None:
#        unavailable.extend(classes[i][5])
#    student = input.lesson1.names_list
#    for j in range(len(student)):
#        if unavailable.count(student[j]) == len(classes):
#            unavail_final.append(student[j])  # Students who can't do anything

# available, not preferred, unavailable
#classes1 = [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []]]


# currently = [[w1 1], [w1 2], [t1], [t2], [l1], [w2 1]]
# maybe???? = [[#w1 [w1 1], [w1 2], [w1 3]], [[#w2 [w2 1], [w2 2], [w2 3]], [#l1 [l1]]]
# class.workshop1 == [['W1', 'Mon', '8 - 9', ['Bob', 'John'], [], []], ['W2', 'Mon', '6 - 7', ['Bob', 'John'], [], []]]
# [['W1', 'Mon', '8 - 9', [names of students who are available], [names of students who do not prefer it], [names of students who are UNavailable]]]