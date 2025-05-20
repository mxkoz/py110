def double_odd_numbers(numbers):
    doubled_nums = []
    for idx in range(0,len(numbers)):
        if idx % 2 == 1:
            doubled_nums.append(numbers[idx] * 2)
        else:
            doubled_nums.append(numbers[idx])
    return doubled_nums