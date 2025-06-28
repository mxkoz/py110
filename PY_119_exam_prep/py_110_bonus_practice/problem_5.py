def most_common_char(string):
    string = string.casefold()
    most_common_char = ''
    most_common_char_count = 0
    for char in string:
        if char.isalpha():
            char_count = string.count(char)
            if char_count > most_common_char_count:
                most_common_char = char
                most_common_char_count = char_count
    return most_common_char 

print(most_common_char('Hello World'))
print(most_common_char('Mississippi'))
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')