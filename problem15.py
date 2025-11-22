# n = int(input())
# l1 = list(map(str,input().split()))
# m = int(input())
# l2 = list(map(str,input().split()))
# s1 = set(l1)
# s2 = set(l2)
# difference = s1.difference(s2)
# print(difference)
#

#
# str1 = input()
# str2 = input()
# str3 = str1 + str2
# print(str3)
# vowels = "aeiouAEIOU"
# for ch in vowels:
#     str3 = str3.replace(ch , "")
# print(str3)
#
# str4 = str3[::-1]
# print(str4)
# str5 = str4.swapcase()
# print(str5)



if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end = "")