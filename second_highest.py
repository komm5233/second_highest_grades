def second_highest(students):
	grade = [] # grades = [line[1] for line in students] #只把成績拿出來
	for line in students:
		grade.append(line[1])
		grade = sorted(grade, reverse=True)
	second = grade[1]

	second_high_students = [s[0] for s in students if s[1] == second]
	for student in second_high_students:
		print(student)

	# second_highest_students = []	
	# for s in students:
	# 	if s[1] == second:	

second_highest([['Jerry', 88], ['Justin', 84], ['Tom', 95], ['Akriti', 90], ['Harsh', 90]])