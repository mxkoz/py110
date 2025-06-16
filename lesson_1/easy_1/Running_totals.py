def running_total(list):
    running_total_list = []
    running_total = 0
    for item in list:
        running_total += item
        running_total_list.append(running_total)
    return running_total_list
    
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True