def gradingStudents(grades):
    for i in range(len(grades)):
        nr=(((grades[i]//5)+1)*5)
        df=nr-grades[i]
        if df<3 and grades[i]>=38:
            grades[i]=nr
    return grades

if __name__ == "__main__":
    # grades_count=int(input().strip())

    # grades=[int(input().strip()) for _ in range(grades_count)]
    grades=[73,67,38,33]
    
    # for _ in range(grades_count):
    #     grades.append()
    
    print(gradingStudents(grades))
    