n = list(map(float,input().split()))
def func(array):
    sum1 = sum(array)
    avg = sum1/len(array)

    print(f"{sum1:.1f}")
    print(f"{avg:.1f}")

func(n)