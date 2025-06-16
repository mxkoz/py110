dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

#Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

result = []

for outer_dict, outer_value in dict1.items():
    if dict1[outer_dict]['type'] == 'fruit':
        
        result.append(dict1[outer_dict]['colors'])
    elif dict1[outer_dict]['type'] == 'vegetable':
        result.append(dict1[outer_dict]['size'].upper())

print(result)



# def extract_elements(sub_dict):
#     [[key['colors'], key['size'].upper()] for key, value in sub_dict.items()]

# lst = [extract_elements(sub_dicts) for sub_dicts in dict1]
# print(lst)