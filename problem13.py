# l1 = [12 , 23 , 45 , 67 ]
# # for i in range(len(l1)):
# #     print(l1[i] , end = " ")
# sum = (l1[0] + l1[1] + l1[2] +l1[3])
# print(sum)
#
# # another way
# print(sum(l1))


n = int(input("enter the number:"))
if (n<1 or n>9):
    print("Invalid Input")

else:
    choice = input()

    if (choice == "n"):
        print(n)

    elif(choice == "y"):
        operation = input()
        n2 = int(input("enter the another number:"))

        if (operation == "+"):
            result = n + n2
            print(result)

        elif(operation == "-"):
            result = n - n2
            print(result)

        elif(operation == "*"):
            result = n * n2
            print(result)

        else:
            print("Invalid operation .")