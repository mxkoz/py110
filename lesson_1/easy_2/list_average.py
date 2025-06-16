def average(list):
    running_total = 0
    for digit in list:
        running_total += digit
    return (running_total//len(list))

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True