def remove_non_letters(string):
    result = ''
    for char in string:
        if char.isalpha():
            result += char
    return result

def word_sizes(string):
    word_list = string.split()
    final_dict = {}
    for word in word_list:
        cleaned_word = remove_non_letters(word)
        cleaned_word_length = len(cleaned_word)
        final_dict[cleaned_word_length] = final_dict.get(cleaned_word_length, 0) + 1
    return final_dict

# All of these examples should print True

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})