def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = min(lst[i : ])
        currentMinIndex = i + lst[i: ].index(currentMin)
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
    return lst

lst = [13,52,91,74,59]
selectionSort(lst)
print((lst))