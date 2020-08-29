def find_good_sessions_for_group(students, lesson_type)
	good_list = []

	available = []
	not_pref  = []
	index = 0
	no_students = len(students)
	for session in lesson_type:
		for student in students:
			else if session[0][3].count(student) == 1:
				available[index].append(student)
			else if session[0][4].count(student) == 1:
				not_pref[index].append(student)
		index += 1

	max_avail_pref = 0;
	all_available = 0;
	max_available = 0;
	for i in len(available):
		no_available = len(available[i] + not_pref[i])
		if no_available == no_students:
			entry = [ session[0][0], session[0][1], session[0][2], available, not_pref, []]
			good_list.append(entry)
		# else if no_available > max_available:
		#	good_list = []
		#	good_list.append()

	return good_list

def generate_move_lists(length_difference,  group_a, no_to_move):
	# TODO
	return 0

def brute(length_difference, group_a, group_b, lesson_type):
	for index in (length_difference - 1):	
		move_list = generate_move_list(group_a, index)
		# TODO

def stacc_and_relacc(lesson_class, lesson_type) :
	pressure_students = []
	essential_sessions = []
	nonessential_sessions = []
	final_sessions = []
	unallocated_students = lesson_class.names_list

# 	# Finding essential sessions
# 	for session0 in lesson_type:
# 		for student in unallocated_students:
# 			if session0[0][3].count(student) > 0 or session0[0][4].count(student) > 0:
#
# 				student_no_availabilities = 0
# 				for session01 in lesson_type:
# 					student_no_availabilities += session01[0][3].count(student) + session01[0][4].count(student)
#
# 				if student_no_availabilities == 1:
# 					pressure_students.append(student)
# 					if essential_sessions.count(session0) == 0:
# 						unallocated_students.remove(student)
# 						nonessential_sessions.remove(session0)

	# Finding pressure student
	available_counts = []
	counting_index = 0
	for student in lesson_class.names_list:
		for session in lesson_type:
			available_counts[counting_index] += session[0][3].count(student) + session[0][4].count(student)
	
	min_availablity : int = 100000000000000
	min_index = -1
	for i in len(available_counts):
		value = available_counts[i]
		if value < min_availability:
			min_availability = value
			min_index = i
		
	# Surely not, would be truly wack
	if min_index == -1:
		print("Wack")

	# Picking the A group, pretending that the pressure student only has one availability
	pressure_student = lesson_class.names_list[min_index]
	group_a = []
	for session7 in lesson_type:
		if session7[0][3].count(pressure_student) or session7[0][4].count(pressure_student):
			group_a = session7
			break

	group_a_students = [ pressure_student ]
	group_b_students = []
	for student1 in lesson_class.names_list:
		if group_a[0][3].count(student1) == 1 or group_a[0][4].count(student1) == 1:
			group_a_students.append(student1)
		else:
			group_b_students.append(student1)

	no_extra_a = len(group_a_students) - 1
	length_difference = no_extra_a + 1 - len(group_b_students)
	if length_difference > 0:
		brute(length_difference, group_a_students, group_b_students, lesson_type)
	else:
		good_list = find_good_sessions_for_group(group_b_students, lesson_type)

# 	if len(essential_sessions) > 2:
# 		print("L?")
#
# 	# Culling students who are available in the essential sessions
# 	for session1 in essential_sessions:
# 		for student in unallocated_students:
# 			if session1[0][3].count(student) > 0 or session1[0][4].count(student) > 0:
# 				unallocated_students.remove(student)
#
# 	# TODO: Finish
# 	for session2 in essential_sessions:
#
# 	if len(unallocated_students) > 0:
# 		for session3 in nonessential_sessions:
# 			# TODO: Finish
# 			a = 0
#
# 	print(pressure_students)

