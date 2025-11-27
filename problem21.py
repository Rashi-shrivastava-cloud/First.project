
# l1 = ["rashi" , "anumita" , "vanshu" , "ram"]
# name = input("Enter your name:")
# if (name in l1):
#     print("yes name is present in the list" , name)
#
# else:
#     print("no it is not present in the list " , name)

#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#
# avg_marks = sum(student_marks[query_name])/3
# print("{:.2f}".format(avg_marks))

# # m = []
# m = [i for i in range(11)]
# print(m)


l1 = ["rashi" ,"anas" , "raj" ,"anumita"]
l2 = [i.upper() for i in l1]
print(l2)