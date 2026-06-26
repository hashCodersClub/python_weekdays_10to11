marks_student  = [15,-10,30,"hasib",65,74]


# print(marks_student)
#output -> [65,15,-10,30,"hasib",74]

#individual values [elements] access

# print(marks_student[1])
# print(marks_student)
# marks_student.pop(3)
# print(marks_student)

marks_student.insert(0,marks_student[-2])
marks_student.pop(-2)
print(marks_student)
