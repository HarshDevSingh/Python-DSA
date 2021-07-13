def bubble_sort1(arr=[]):
    if len(arr)<2:
        return arr
    for i in range(len(arr)-1):
        for j in range (len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def bubble_sort(arr=[]):
    if len(arr)<2:
        return arr
    for i in range(len(arr)):
        for j in range (len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubble_sort([5,3,9,10,2,14]))
