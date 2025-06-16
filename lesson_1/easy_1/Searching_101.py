# Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

list = []
first_number = int(input('Please enter the first number'))
list.append(first_number)
second_number = int(input('Please enter the second number'))
list.append(second_number)
third_number = int(input('Please enter the third number'))
list.append(third_number)
fourth_number = int(input('Please enter the fourth number'))
list.append(fourth_number)
fifth_number = int(input('Please enter the fifth number'))
list.append(fifth_number)
sixth_number = int(input('Please enter the sixth and final number'))
if sixth_number in list:
    print(f'{sixth_number} is in {list}')
else:
    print(f'{sixth_number} is not in {list}')