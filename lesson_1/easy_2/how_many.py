# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

def count_occurrences(list):
    new_dict = {}
    for item in list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    for item, count in new_dict.items():
        print(f'{item}==> {count}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
