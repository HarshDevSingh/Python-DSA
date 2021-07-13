def selection_sort(A):
    if len(A) < 2:
        return A
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


print(selection_sort([10, 3, 3, 2, 99, 37, -5, -7]))
