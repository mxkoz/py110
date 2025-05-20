def swap_name(name):
    name_list = name.split()
    first, last = name_list
    name_reformatted = f'{last}, {first}'
    return name_reformatted

print(swap_name('Karl Oskar Henriksson Ragvals'))  # True