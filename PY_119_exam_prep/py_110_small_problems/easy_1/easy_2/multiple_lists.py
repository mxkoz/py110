def multiply_list(lst1, lst2):
    result = []
    for i in range(0,len(lst1)):
        result.append(lst1[i] * lst2[i])
    return result


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True