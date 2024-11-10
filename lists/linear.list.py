def linearSearch(lst, key):
    for i in range(0, len(lst)):
        if key == lst[i]:
            return i
    return -1

list1 = [1,2,3,4,5,6,7,8,9]
print(linearSearch(list1, 2))