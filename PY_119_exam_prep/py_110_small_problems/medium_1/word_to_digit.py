def word_to_digit(message):
    key = {'one':'1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9',
           'zero': '0'}
    word_list = message.split()
    result = []
    for word in word_list:
        if word in key:
            result.append(key[word])
        else:
            result.append(word)
    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message))
# Should print True