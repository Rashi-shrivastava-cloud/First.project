a = "I Love python and python loves me."
vowels ="aeiouAEIOU"
count = {}.fromkeys(vowels,0)
for i in a:
    if i in count:
        count[i] +=1

print(count)


l1 = ["rashi" , "anumita" , "vanshu" , "ram"]
name = input("Enter your name:")
if (name in l1):
    print("yes name is present in the list" , name)

else:
    print("no it is not present in the list " , name)
