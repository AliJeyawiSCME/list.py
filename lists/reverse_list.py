def reverse(list):
    result = []

    for element in list:
        result.insert(0, element)

    return result

list1 = [7,8,9,2,3]
list1.reverse()
print(list1)