



def repeater(string):
    doubled_chars = [(letter + letter) for letter in string]
    return "".join(doubled_chars)

print(repeater('hello'))

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True