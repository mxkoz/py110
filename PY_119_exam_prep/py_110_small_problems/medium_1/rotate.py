def rotate_list(input):
    if type(input) != list:
        return None
    if len(input) == 1 or len(input) == 0:
        return input
    result = [input[-1:],input[1:-1], input[0]]
    return result


print(rotate_list([7, 3, 5, 2, 9, 1]))
# All of these examples should print True




# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])