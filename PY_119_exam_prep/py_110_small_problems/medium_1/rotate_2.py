#input is two integers, output is an integer shifted according to the second integer
#convert to string, iterate through using a for loop; if index = the length minus the count, add it to the end

def rotate_rightmost_digits(number, count):
    string_number = str(number)
    final_digit = ''
    main_number = ''
    for index in range(0,len(string_number)):
        if index == (len(string_number) - count):
            final_digit = string_number[index]
        else:
            main_number += string_number[index]
    final_number = main_number + final_digit
    return int(final_number)

print(rotate_rightmost_digits(735291, 6))