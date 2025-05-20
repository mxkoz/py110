statement = "The Flintstones Rock"
cleaned_statement = statement.replace(' ','')
index_dict = {}
for letter in cleaned_statement:
    if letter not in index_dict:
        index_dict[letter] = 1
    else:
        index_dict[letter] += 1
print(index_dict)