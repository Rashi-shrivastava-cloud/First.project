n = int(input())
student = []
for i in range(n):
    name = input()
    grades = float(input())
    student.append([name,grades])

print(student)
grades =[ student[1] for  student in student ]
unique_grade = sorted(set(grades))
print(unique_grade)


second_lowest = grades[1]
print(second_lowest)

name = [student[0] for student in student if student[1] == second_lowest]
name.sort()
# print(name)

for a in name:
    print(a)