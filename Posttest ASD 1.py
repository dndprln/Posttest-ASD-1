def flatten(arr):
    list_flat = []

    for item in arr:
        if isinstance(item, list):
            list_flat.extend(flatten(item))

        else:
            list_flat.append(item)

    return list_flat

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)

        else:
            result.append(right[0])
            right.pop(0)

    result.extend(left)
    result.extend(right)
    return result

Variable = [12,1,[22,3,[8,14]],2,6,[11],90]
Variable = mergeSort(flatten(Variable))

print(Variable)