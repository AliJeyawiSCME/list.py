def reverse(list):
    result = []

    for element in list:
        result.insert(0, element)

    return result

list1 = [1,2,3,4,5,6]
list2 = reverse(list1)
print(list2)