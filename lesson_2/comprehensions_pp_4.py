# Given the following data structure, write some code that uses comprehensions to define a dictionary where the key is the first item in each sublist, and the value is the second.

import pprint
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# new_dict = {element[0]: element[1] for element in lst}
# pprint.pprintprint(new_dict)

print(dict(lst))