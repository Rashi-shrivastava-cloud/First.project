# n = int(input())
# student = []
# for i in range(n):
#     name = input()
#     grades = float(input())
#     student.append([name,grades])
#
# print(student)
# grades =[ student[1] for  student in student ]
# unique_grade = sorted(set(grades))
# print(unique_grade)
#
#
# second_lowest = grades[1]
# print(second_lowest)
#
# name = [student[0] for student in student if student[1] == second_lowest]
# name.sort()
#
# for a in name:
#     print(a)


# include <stdio.h>

int main()
{
int a, b;
    printf("enter the number(a)");
    scanf("%d", & a);
    printf("enter the number(b)");
    scanf("%d", & b);
    printf("%d", a + b);

    return 0;
}