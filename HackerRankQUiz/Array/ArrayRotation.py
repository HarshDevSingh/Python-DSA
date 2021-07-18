def arr_rot(arr, d):
    temp_arr = arr
    return temp_arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5, 6, 7]
print(arr_rot(arr, 4))
