def triangle(side1, side2, side3):
    triange_list = [side1, side2, side3]
    triange_list.sort()
    if triange_list[0] + triange_list[1] <= triange_list[2]:
        return 'invalid'
    if triange_list[0] == triange_list[1] and triange_list[1] == triange_list[2]:
        return 'equilateral'
    if triange_list[0] == triange_list[1] or triange_list[1] == triange_list[2] or triange_list[0] == triange_list[2]:
        return 'isosceles'
    return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True