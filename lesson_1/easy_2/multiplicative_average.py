def multiplicative_average(list):
    running_total = 0
    for digit in list:
        if running_total == 0:
            running_total += digit
        elif running_total != 0:
            running_total *= digit
    result = running_total/len(list)
    return result

# All of these examples should print True
print(multiplicative_average([3, 5]))
print(multiplicative_average([2, 5, 8]))
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")