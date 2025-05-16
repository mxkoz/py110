# Try coding a function that lets you multiply every list element by a specified value. As with double_numbers, don't mutate the list, but return a new list instead.

def multiply_elements(list, multiplier):
    multiplied_elements = []
    for item in list:
        multiplied_elements.append(item*multiplier)
    return multiplied_elements

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply_elements(my_numbers, 5))