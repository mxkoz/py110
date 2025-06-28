# Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

def halvises(lst):
    lst1 = []
    lst2 = []
    for index in range(0, len(lst)):
        if index >= (len(lst)/2):
            lst2.append(lst[index])
        else:
            lst1.append(lst[index])
    return [lst1, lst2]


print(halvises([1, 2, 3]))

