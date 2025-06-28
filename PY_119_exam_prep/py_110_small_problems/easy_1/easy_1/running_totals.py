# Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

# ExamplesCopy Code

def running_total(list):
    new_list = []
    running_total = 0
    for number in list:
        running_total += number
        new_list.append(running_total)
    return new_list


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True