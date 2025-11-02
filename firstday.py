n = int(input("enter the number:"))
fact = 1
i = 1
for i in range(1, n + 1):
    fact = fact * i

    i += 1

print(fact)

# n = int(input("enter the number:"))
# sum = 0
# i = 0
# while i in range(n):
#     sum += i
#     # print(f"sum of {n} is {sum}")
#     i += 1
# print(f"sum of {n} is {sum}")

# or
n = int(input("enter the number:"))
sum = 0
i = 1
while(i<=n):
    sum += i
    i += 1
print(sum)


n = int(input())

# if (n <= 1):
#     print("it is not a prime number.")

# elif (n % 2 == 0 or  n % 3 == 0  or n % 5 == 0  or n % 5 == 0 ):
#     print("it is not a prime number")

# elif (n % n == 0):
#       print("it is a prime number")


# or

for i in range(2, n):
    if(n%i) == 0:
        print("number is not prime") # in order to avoid repetition we use break statement.
        break

    else:
        print("number is prime")


n = int(input())
i = 1
while i<11:
    print(f"{n}  *  {i}  = {n*i}")
    i += 1


l = ["Harry" ,"Sohan" , "Sachin" , "Rahul"]
for name in l:
    if (name[0] == "S"):
        print(f"Hello{name}" , end = " ")


        #or
    # if (name.startswith("S")):
    #     print(f"Hello {name}")



n = int(input("enter the number :"))
# i = 0
for i in range(1, 11):
    # n1 = n * i
    # i += 1
    # print(n1)
    # or
    print(f" {n}  *  {i}  = {n*i}")


