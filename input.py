

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
    skip_line = 
    for word in line:
        print(word)



input('asda', 'Class input.csv', 'FIT2014')





