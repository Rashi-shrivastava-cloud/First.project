
# l1 = ["rashi" , "anumita" , "vanshu" , "ram"]
# name = input("Enter your name:")
# if (name in l1):
#     print("yes name is present in the list" , name)
#
# else:
#     print("no it is not present in the list " , name)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


avg_marks = sum(student_marks[query_name])/3
print("{:.2f}".format(avg_marks))