# Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

#Input: string argument
#Output: a copy of the string with every second character in every third word converted to uppercase...
#Algorithm
# - split the string into a list based on spaces (divide by word)
# - outerloop selects every third word
# - innerloop changes every other character in the word

def inner_loop_char_change(word):
    new_word = ''
    for index in range(0, len(word)):
        if index % 2 == 1:
            new_word += word[index].upper()
        else:
            new_word += word[index]
    return new_word

def to_weird_case(string):
    words = string.split()
    weird_case = []
    if len(words) <3:
        return words
    for index in range(0, len(words)):
        if (index + 1) % 3 == 0:
            weird_case.append(inner_loop_char_change(words[index]))
        else:
            weird_case.append(words[index])
    return ' '.join(weird_case)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original))

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case("Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"))