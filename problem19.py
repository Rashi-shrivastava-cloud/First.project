a = "I Love python and python loves me."
vowels ="aeiouAEIOU"
count = {}.fromkeys(vowels,0)
for i in a:
    if i in count:
        count[i] +=1

print(count)