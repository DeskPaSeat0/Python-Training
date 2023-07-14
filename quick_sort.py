nums = [34, 1, 22, 98, 100, -1, 4, 18]

def quickSort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    L = [x for x in list[1:] if x < pivot]
    R = [x for x in list[1:] if x >= pivot]
    return quickSort(L) + [pivot] + quickSort(R)

sorted_array = quickSort(nums)

print(sorted_array)