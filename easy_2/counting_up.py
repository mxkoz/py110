def sequence(integer):
    integer_list = []
    for i in range(1,(integer+1)):
        integer_list.append(i)
    return integer_list


print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

