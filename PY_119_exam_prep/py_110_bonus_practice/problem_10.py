def even_substrings(string):
    result = 0
    for index in range(0, len(string)):
       if int(string[index]) % 2 == 0:
        result += 1
        while index <= len(string):
            if int(string[index:(index + 1)]) % 2 == 0:
                result += 1
            index += 1
    print(result)

even_substrings('1432')
