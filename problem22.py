# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# 
# coordinates = [[i,j,k]
# for i in range(x+1)
# for j in range(y+1)
# for k in range(z+1)]
# 
# print(coordinates)

n = int(input())
arr = list(map(int,input().split()))
a = list(set(arr))
a.sort(reverse = True)
print(a[1])