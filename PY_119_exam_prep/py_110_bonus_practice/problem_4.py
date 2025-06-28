# Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

def closest_numbers(number_list):
    for number in number_list:
        smallest_difference_pair = (number_list[0], number_list[1])
        smallest_difference = abs(number_list[0] - number_list[1])
        for index in range(0, len(number_list)):
            difference = abs(number - number_list[index])
            if difference < smallest_difference:
                smallest_difference = difference
                smallest_difference_pair = (number, number_list[index])
    return smallest_difference_pair

print(closest_numbers([5, 25, 15, 11, 20]))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))