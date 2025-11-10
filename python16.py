# n = int(input())
# l1 = list(map(int,input().split()))
# l1.sort()
# print(l1[0])



# n = int(input())
# l1 = list(map(int,input().split()))
# l1.sort(reverse = True)
# print(l1)


def fun(num):
    num_set =set(num)
    longest = []

    for i in (num_set):
        if (i - 1 not in num_set):
            current = []
            x = i
        while (x in num_set):
             current.append(x)
             x += 1

        if len(current) > len(longest):
            longest = current
    return tuple(longest)

t = tuple(map(int,input().split()))
arr= fun(t)
print(arr)