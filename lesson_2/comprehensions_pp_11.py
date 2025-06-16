# The following dictionary has list values that contains strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

# print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']


def is_vowel(letter):
    if letter in 'aeiou':
        return True
    else:
        return False

print([letter for values in dict1.values() 
       for string in values 
       for letter in string if letter in 'aeiou'])
