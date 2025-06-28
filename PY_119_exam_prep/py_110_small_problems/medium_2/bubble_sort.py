def bubble_sort(lst):
    swap_count = 1
    while swap_count > 0:    
        swap_count = 0
        for i in range(0, len(lst)):
            if i == (len(lst) - 1):
                continue
            if lst[i] > lst[i + 1]:
                removed_item = lst.pop(i)
                lst.insert((i + 1), removed_item)
                swap_count += 1
    return lst


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True