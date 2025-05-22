munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

#Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.



#Ordinary for loop
# def age_summer(dict):
#     total_age = 0
#     for member in dict.items():
#         if member['gender'] == 'male':
#             total_age += member['age']
#     return total_age
# print(age_summer(munsters))

#Comprehension

total_male_age = [((member['age'])) for member in munsters.values() if member['gender'] == 'male']
print(sum(total_male_age))