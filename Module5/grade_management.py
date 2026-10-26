def calculateGrade(grade):
    if not grade:
        return 0
    return sum(grade) / len(grade)

def defineStatus(grade):
    if(grade >= 75):
        return "Passed"
    else:
        return "Failed"