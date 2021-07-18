def linear_search(arr, value):
    for i in arr:
        if value == i:
            return True
    return False


print(linear_search([1, 2, 5, 3, 9, 24], 24))
