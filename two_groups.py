def stacc_and_relacc(papi_lesson, lesson_type):
	pressure_students = []
	essential_sessions = []
	nonessential_sessions = []
	unallocated_students = papi_lesson.names_list

	# Finding essential sessions
	for session0 in lesson_type:
		for student in unallocated_students:
			if session0[0][3].count(student)  > 0 or session0[0][4].count(student)  > 0:
				if STUDENT_NO_AVAILABILITIES == 1:
					pressure_students.append(student)
					if essential_sessions.count(session0) == 0:
						unallocated_students.remove(student)
						nonessential_sessions.remove(session0)

	if len(essential_sessions) > 2:
		print("L?")
	
	# Culling students who are available in the essential sessions
	for session1 in essential_sessions:
		for student in unallocated_students:
			if session1[0][3].count(student)  > 0 or session1[0][4].count(student)  > 0:
				unallocated_students.remove(student)

	if len(unallocated_students) > 0:
		# We are not done :(!
        for session2 in nonessential_sessions:
			 # TODO: Finish
	else:
		# We are done!
		print("Hello sailor!")
