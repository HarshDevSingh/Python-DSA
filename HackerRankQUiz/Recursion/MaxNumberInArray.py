arr = [3, 1, 6, 5, 9, 10, 45, 23]


def max_num(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], max_num(arr, n - 1))


print(max_num(arr, 8))
