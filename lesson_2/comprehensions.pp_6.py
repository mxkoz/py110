lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print([{key: value} for element in lst for key, value in element.items()])
