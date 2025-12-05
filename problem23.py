# if __name__ == '__main__':
#     # N = int(input())
#     N = int(input())
# l1= []
# l1.insert(0,5)
# l1.insert(1,10)
# l1.insert(0,6)
# print(l1)
# l1.remove(6)
# l1.insert(0,9)
# l1.append(1)
#
# l1.sort()
# print(l1)
# l1.sort(reverse = True)
# print(l1)
# l1.pop(3)
# print(l1)
# l1.sort(reverse = True)
# print(l1)


# n = int(input())
# l1 =set(map(int,input().split()))
# m = int(input())
# l2 =set(map(int,input().split()))
# # print(len(l1.difference(l2)))
# print(l1.difference(l2))


n = int(input())
l1 =set(map(int,input().split()))
m = int(input())
l2 =set(map(int,input().split()))
s1 = len(l1.difference(l2))
s2 = len(l2.difference(l1))

s3 = s1+ s2
print(s3)