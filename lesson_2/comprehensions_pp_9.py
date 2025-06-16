lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

#Proble

def is_even(dict):
    for letter, numbers in dict.items():
        for number in numbers:
            if number % 2 != 0:
                return False
    return True
        
print([element for element in lst if is_even(element)])