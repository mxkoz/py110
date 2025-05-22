# Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odds(item):
    odd_total = 0
    for element in item:
        if element % 2 != 0:
            odd_total += element
    return odd_total

new_list = sorted([item for item in lst],key=sum_odds)
print(new_list)