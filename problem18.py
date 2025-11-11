user_input= input().split()
for i in (user_input):
    if i.isalpha():
        print(f"yes it is an alphabet{i}")
    elif i.isdigit():
        print(f"yes it is a digit{i}")

    else:
        print("invalid input")