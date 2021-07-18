arr=[10, 3, 3, 2, 99, 37, -5, -7]

def quick_sort(arr):
    if (len(arr))<2:
        return arr
    pivot=arr.pop()
    lower=[]
    greater=[]
    for i in arr:
        if i > pivot:
            greater.append(i)
        else :
            lower.append(i)
    return quick_sort(lower)+[pivot]+quick_sort(greater)

print(quick_sort(arr))