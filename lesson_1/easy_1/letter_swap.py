def letter_swap(string):
    first_letter = string[0]
    last_letter = string[-1]
    swapped_string = ''
    for index in range(0, len(string)):
        if index == 0:
            swapped_string += last_letter
        elif index == (len(string) -1):
            swapped_string += first_letter
        else:
            swapped_string += string[index]
    return swapped_string

def swap(phrase):
    words = phrase.split()
    result = ''
    for word in words:
        if result:
            result += ' '
        result += letter_swap(word)
    return result

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True