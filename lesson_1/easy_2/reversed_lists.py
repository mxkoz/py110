# Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

def reverse_list(list):
    for index in range(0,len(list)):
       list.insert((list.pop(index)),0)
    return list

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)
