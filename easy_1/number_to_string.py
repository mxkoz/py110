DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    if find_sign(number) == 'Positive':
        while number > 0:
            number, remainder = divmod(number, 10)
            result = DIGITS[remainder] + result

        return result or '0'
    
    if find_sign(number) == 'Negative':
        number *= -1
        while number > 0:
            number, remainder = divmod(number, 10)
            result = DIGITS[remainder] + result
        result = "-" + result
        return result or '0'

def find_sign(number):
    if number < 0:
        return 'Negative'
    if number >= 0:
        return 'Positive'
    
print(integer_to_string(-123))