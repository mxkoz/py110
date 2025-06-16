
# Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [tou for item in lst for number in item if ((number % 3) == 0)]
    
print(new_lst)