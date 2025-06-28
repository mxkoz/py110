# Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.


#I/o: list of numbers & a return list corresponding to the # of unique numbers in the list are smaller than it.
#Algorithm
# - take a unique list of numbers (maybe a set?)
#- iterate through the list for each number
# - for each number, check how many numbers in the unique set it's greater than


def smaller_numbers_than_current(number_list):
    unique_numbers = list(set(number_list))
    return_list = []
    for number in number_list:
        greater_than_count = 0
        for index in range (0, len(unique_numbers)):
             if number > unique_numbers[index]:
                 greater_than_count += 1
        return_list.append(greater_than_count)
    return return_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)