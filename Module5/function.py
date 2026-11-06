import grade_management

grades = [85,75,96,74]

average = grade_management.calculateGrade(grades)
status = grade_management.defineStatus(average)



print("The average is : " , average)
print("The status is : " + status)  