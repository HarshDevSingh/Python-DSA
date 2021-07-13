arr = [3, 4, -1, -2, -1, 5, -4, -1, 8, 7, 6]


def sorted_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def threesum_zero(arr):
    arr = sorted_arr(arr)
    l = len(arr)
    res = []
    for i in range(l):
        start = i
        left = i + 1
        right = l - 1
        while left < right:
            total = arr[start] + arr[left] + arr[right]
            if total == 0:
                res.append([arr[start], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
            elif total < 0:
                left += 1
            elif total > 0:
                right -= 1
    return res


print(threesum_zero(arr))
