def lowercase_finder(string):
    lower_case_counter = 0
    for letter in string:
        if ord(letter) > 96 and ord(letter) < 122:
            lower_case_counter += 1
    return lower_case_counter

def uppercase_finder(string):
    upper_case_counter = 0
    for letter in string:
        if ord(letter) > 64 and ord(letter) < 91:
            upper_case_counter += 1
    return upper_case_counter

def letter_percentages(string):
    uppercase_letters = uppercase_finder(string)
    uppercase_percentage = round((uppercase_letters / len(string)) * 100, 4)
    lowercase_letters = lowercase_finder(string)
    lowercase_percentage = round((lowercase_letters / len(string)) * 100, 4)
    neither = 1 - (uppercase_percentage + lowercase_percentage)
    result = {'lowercase': lowercase_percentage,
              'uppercase': uppercase_percentage,
              'neither': neither}
    return result

print(letter_percentages('abCdef 123'))