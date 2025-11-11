# n = list(map(float,input().split()))
# def func(array):
#     sum1 = sum(array)
#     avg = sum1/len(array)
#
#     print(f"{sum1:.1f}")
#     print(f"{avg:.1f}")
#
# func(n)


l1 =[] # empty list
n = int(input())
l= list(map(int,input().split()))
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
       l1.append(l[i+1])

    else:
        l1.append(l[i])

print(l1)