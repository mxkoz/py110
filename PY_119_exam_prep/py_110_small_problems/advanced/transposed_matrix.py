
#Input is a list of lists (3 lists to be exact)
#Ouput is the same matrix but transposed. The horizontal rows are now translated to vertical columns

#Algorithm:
# - new_matrix = []
# - if it's in row 1 (index 0[X]), move it to column 1 

def new_matrix(matrix):
    new_matrix = [[], [], []]
    for index in range(0, 3):
        #in first row, should be in first column now
        if index == 0:
            for nested_index in range(0, 3):
                value = (matrix[index][nested_index])
                new_matrix[0].append(value)
        if index == 1:
            for nested_index in range(0, 3):
                value = matrix[index][nested_index]
                new_matrix[1].append(value)
        if index == 2:
            for nested_index in range(0, 3):
                value = matrix[index][nested_index]
                new_matrix[2].append(value)
    return new_matrix


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

print(new_matrix(matrix))
# == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True