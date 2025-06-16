# Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

def halvsies(list):
    list_1 = []
    list_2 = []
    mid_point = (len(list)/2)
    for index in range(0, len(list)):
        if index < mid_point:
            list_1.append(list[index])
        elif index >= mid_point:
            list_2.append(list[index])
    combined = [list_1, list_2]
    return combined

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])