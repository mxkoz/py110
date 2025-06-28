def minimum_sum(numbers):
    if len(numbers) <5:
        return None
    min_sum = 100000
    for number in range(0, len(numbers)-4):
        summed_range = sum(numbers[number:(number+5)])
        if summed_range < min_sum:
            min_sum = summed_range
    return min_sum

print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
